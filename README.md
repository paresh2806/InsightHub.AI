# InsightHub.AI

**AI-Optimized Natural Language to SQL Engine with SAP-HANA Cloud Execution**

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/paresh2806/InsightHub.AI) 
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)
[![Contributions](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](https://github.com/paresh2806/InsightHub.AI)
[![Buy Me A Coffee](https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow)](https://www.buymeacoffee.com/pareshmakwha)
[![LangChain](https://img.shields.io/badge/langchain-0.0.232-blue)](https://github.com/hwchase17/langchain)
[![ChromaDB](https://img.shields.io/badge/chromadb-0.3.22-red)](https://docs.trychroma.com/)
[![GPT4All](https://img.shields.io/badge/gpt4all-0.0.9-yellow)](https://github.com/nomic-ai/gpt4all)
[![Flask](https://img.shields.io/badge/flask-2.3.3-orange)](https://flask.palletsprojects.com/)


---
## Support
If you find this project helpful, feel free to support us!

<a href="https://www.buymeacoffee.com/pareshmakwha" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 40px !important;width: 140px !important;" ></a>

---

## Table of Contents
1. [🚀 Introduction](#introduction)
2. [💻 How to Run the Demo](#how-to-run-the-demo)
   - [🔧 1. Prepare the Python Environment](#1-prepare-the-python-environment)
   - [🤖 2. Prepare the LLM](#2-prepare-the-llm)
   - [📊 3. Pull Embedding from GPT4All](#3-pull-embedding-from-gpt4all)
   - [💾 4. Prepare HANA Cloud Data](#4-prepare-hana-cloud-data)
   - [📝 5. Adjust the Schema File](#5-adjust-the-schema-file)
   - [🔑 6. Configure HANA Cloud in config.py](#6-configure-hana-cloud-in-configpy)
3. [🚧 Run the InsightHub.AI](#run-the-insighthubai)
4. [🤝 Contributing](#contributing)
5. [📜 License](#license)

In today's competitive landscape, SAP is essential for optimizing operations and driving strategic decisions. However, its complexity often hampers timely access to critical insights. As a decision-maker in a large organization, you shouldn't have to rely on IT teams for data queries, which can slow down your decision-making process.

**InsightHub.AI** empowers you to convert natural language queries into SQL effortlessly, enabling independent access to insights from your SAP-HANA Cloud data. With InsightHub.AI, you can make informed decisions quickly and effectively, without dependencies.

---
## How to Run the Demo

Running the demo involves several manual steps:

### 1. Prepare the Python Environment

Assuming you use **conda**, create and activate your environment named **insightao**:
``` bash
conda create --name insightao python=3.11  
conda activate insightao  
pip install -r requirements.txt  
```

---
### 2. Prepare the LLM

Use the **Groq API** for model inference. Ensure you have access to the Groq service and the necessary credentials.

Put this in ```.env```

```SECRET_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX```

---

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

---
### 4. Prepare HANA Cloud Data

1. Create an HANA Cloud instance in a trial environment [SAP BTP Cockpit](https://cockpit.hanatrial.ondemand.com/trial/#/home/trial).
2. Download sample data from [SAP Sample Content](https://github.com/SAP-samples/datasphere-content/tree/main/SAP_Sample_Content/CSV) and import it into the HANA database.
 or
3. Use the `SAP-sample-Data` directory to access the required data.
4. Dump the data to the DB Instance / Data Lake Instance 
5. Verify the results using the `HANA-Connection.ipynb` notebook located in the `Notebook` directory.

---
### 5. Adjust the Schema File

Modify the schema files located in the `schema` folder to fit your database structure.

---

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

---
## Run the InsightHub.AI

To run the InsightHub.AI, execute the following command:

```
python app.py  
```
Then, navigate to [http://localhost:5000](http://localhost:5000) to access the demo.

---

## Contributing
We welcome contributions to InsightHub.AI! To get started:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and test them thoroughly.
4. Open a pull request, detailing your changes.

Feel free to raise issues or feature requests if you encounter any problems.

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
