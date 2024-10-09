# InsightHub.AI

**AI-Optimized Natural Language to SQL Engine with SAP-HANA Cloud Execution**

## Introduction
In today's competitive landscape, SAP is essential for optimizing operations and driving strategic decisions. However, its complexity often hampers timely access to critical insights. As a decision-maker in a large organization, you shouldn't have to rely on IT teams for data queries, which can slow down your decision-making process.

**InsightHub.AI** empowers you to convert natural language queries into SQL effortlessly, enabling independent access to insights from your SAP-HANA Cloud data. With InsightHub.AI, you can make informed decisions quickly and effectively, without dependencies.

## How to Run the Demo

Running the demo involves several manual steps:

### 1. Prepare the Python Environment

Assuming you use **conda**, create and activate your environment named **insightao**:
``` bash
conda create --name insightao python=3.11  
conda activate insightao  
pip install -r requirements.txt  
```

### 2. Prepare the LLM

Use the **Groq API** for model inference. Ensure you have access to the Groq service and the necessary credentials.

Put this in ```.env```

```SECRET_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX```
### 3. Pull Embedding from GPT4All

Example of How to use GPT4ALL  ( You can choose th model though !!!)

```
from langchain_community.embeddings import GPT4AllEmbeddings
model_name = "all-MiniLM-L6-v2.gguf2.f16.gguf"
gpt4all_kwargs = {'allow_download': 'True'}
embeddings = GPT4AllEmbeddings(
    model_name=model_name,
    gpt4all_kwargs=gpt4all_kwargs
)
```

### 4. Prepare HANA Cloud Data

1. Create an HANA Cloud instance in a trial environment [SAP BTP Cockpit](https://cockpit.hanatrial.ondemand.com/trial/#/home/trial).
2. Download sample data from [SAP Sample Content](https://github.com/SAP-samples/datasphere-content/tree/main/SAP_Sample_Content/CSV) and import it into the HANA database.
 or
3. Use the `SAP-sample-Data` directory to access the required data.
4. Dump the data to the DB Instance / Data Lake Instance 
5. Verify the results using the `HANA-Connection.ipynb` notebook located in the `Notebook` directory.

### 5. Adjust the Schema File

Modify the schema files located in the `schema` folder to fit your database structure.


### 6. Configure HANA Cloud in config.py

Update the HANA Cloud instance details in config.py:
```
HC = {  
    "endpoint": "<Your HANA Cloud Instance Link>",  
    "port": 443,  
    "user": "<Your DB user>",  
    "password": "<Your DB password>"  
}  
```

## Run the InsightHub.AI

To run the InsightHub.AI, execute the following command:

```
python app.py  
```
Then, navigate to [http://localhost:5000](http://localhost:5000) to access the demo.
