from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import Ollama
from langchain_groq import ChatGroq
import os
import ollama

from intent_helper import topic_intent
from db import db_query
from config import SCHEMA_FILE_PATH
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_ENDPOINT'] = 'https://api.smith.langchain.com'
os.environ['LANGCHAIN_PROJECT'] = os.getenv('LANGCHAIN_PROJECT')
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')


class ChatBot:
    def __init__(self, host:str = 'localhost'):
        """
        Sample parameters for options could be as below:
          "options": {
                "num_keep": 5,
                "seed": 42,
                "num_predict": 100,
                "top_k": 20,
                "top_p": 0.9,
                "tfs_z": 0.5,
                "typical_p": 0.7,
                "repeat_last_n": 33,
                "temperature": 0.8,
                "repeat_penalty": 1.2,
                "presence_penalty": 1.5,
                "frequency_penalty": 1.0,
                "mirostat": 1,
                "mirostat_tau": 0.8,
                "mirostat_eta": 0.6,
                "penalize_newline": true,
                "stop": ["\n", "user:"],
                "numa": false,
                "num_ctx": 1024,
                "num_batch": 2,
                "num_gpu": 1,
                "main_gpu": 0,
                "low_vram": false,
                "f16_kv": true,
                "vocab_only": false,
                "use_mmap": true,
                "use_mlock": false,
                "num_thread": 8
            }
            I only use temperature and top_p here to ensure the minimum diversity.
        """
        self.host = host
        self.base_url = "http://%s:11434"%host
        #self.client = ollama.Client(host = self.host)


    def chat(self, question):
        intent = topic_intent(question=question)
        if intent['topic'] == 'General':
            return self.general_chat(question)
        else:
            return self.db_chat(intent=intent, question=question)

    def general_chat(self, question, model = "mistral", temperature=0.8, top_p=0.9):
        """
        Set temperature as 0.8 and top_p as 0.9 to increase the diversity of the result.
        """
        seed_prompt = """
        Answer the user question. 

        {question}

        Detect the language from the question.
        Response the answer in the same language detected from the question.
        """
        prompt = PromptTemplate.from_template(seed_prompt)
        # llm = Ollama(model=model, base_url = self.base_url, temperature=temperature, top_p=top_p)
        llm = ChatGroq(temperature=0, groq_api_key="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",
                       model_name="mixtral-8x7b-32768")
        chain = (
            prompt
            | llm
            | StrOutputParser()
        )
        return {"status": "Success", "type": "General", "msg": chain.invoke({"question": question})}
    
    def db_chat(self, intent, question, model="codellama", temperature=0, top_p=0, output_format="raw"):
        schema_columns = open(os.path.join(SCHEMA_FILE_PATH, intent['schema_file']), 'r').read()
        few_shot_file_path = os.path.join("data", "few_shot_examples.txt")
        with open(few_shot_file_path, 'r') as file:
            few_shot_examples = file.read()


        seed_prompt = f"""
        ### Instructions:
        You are an agent designed to interact with a SQL database at a company.
        Given an input question, create a syntactically correct SQL query to run, then look at the results of the query and return the answer.
       
        You can order the results by a relevant column to return the most interesting examples in the database.
        
        ### Few-shot Examples:
        Consider the following examples carefully when generating the SQL query for the current question:
        {few_shot_examples}
        
        ### Input:
        Generate a SQL query that answers the question `{question}`.
        This query will run on a database whose schema is represented in this string:
        {schema_columns}\n
        
        ### Important:
        - Never query for all the columns from a specific table unless specifically asked to. Only request the relevant columns based on the input question.
        - You MUST ensure the query is correct for execution in the HANA Cloud database environment.
        - Do not include backslashes in the query.
        - DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP, etc.) to the database.
        - Always check for tables and their available columns in the database before formulating a query.
        - Use the 'YYYYMMDD' date format where applicable.
        
        To start, you should ALWAYS inspect the tables in the database to see what you can query.
         ### Response:
         Write only the HANA CLOUD query and nothing else. 
         Do not wrap the SQL query in any other text, not even backticks as well as '''\\''' 



        SQL Query:

        """
        prompt = PromptTemplate.from_template(seed_prompt)
        # llm = Ollama(model=model, base_url = self.base_url, temperature = temperature, top_p = top_p)
        llm = ChatGroq(temperature=0, groq_api_key="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",
                       model_name="llama3-70b-8192")
        sql_response = (
            prompt
            | llm
            | StrOutputParser()
        )
        ret = sql_response.invoke({'question': question, 'schema_columns': schema_columns})
        sql = ret.split("```")[0].strip().split(";")[0] + ";"

        try:
            result = db_query(sql, output_format)
            messages = {"status": "Success", "sql": sql, "msg": ret, "data" : result}
        except Exception as e:
            msg = str(e)
            messages = {"status": "Error", "type": "DB", "sql": sql, "msg": msg}

        return messages
    
    def image_chat(self, question, images: list[str], temperature=0, top_p=0, model="llava"):
        """
        The images parameter can contain a list of image paths or a image byte
        """
        client = ollama.Client(host=self.host)
        options = {"temperature": temperature, "top_p": top_p}
        res = client.chat(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": question,
                    "images": images
                }
            ],
            options=options
        )
        return {"status": "Success", "type": "image", "msg": res['message']['content']}

