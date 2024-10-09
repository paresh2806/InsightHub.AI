from langchain_community.embeddings import HuggingFaceEmbeddings
import os
# from langchain.embeddings import GPT4AllEmbeddings
from langchain_community.embeddings import GPT4AllEmbeddings
from environs import Env

HC = {
    "endpoint" : "9c272423-17ca-4bee-9c1f-6b46cc5d5340.hana.trial-us10.hanacloud.ondemand.com",
    "port" : 443,
    "user": os.getenv('user'),
    "password": os.getenv('password')
}

# EMBEDDING_PATH = './embedding'
# MINILM_EMBEDDING = HuggingFaceEmbeddings(model_name=os.path.join(EMBEDDING_PATH, 'all-MiniLM-L6-v2'),
#                                         model_kwargs={'device': 'cpu'})
MINILM_EMBEDDING = GPT4AllEmbeddings()
JINA_EMBEDDING = 'jina'
DEFAULT_EMBEDDING_NAME = 'jina'

SCHEMA_FILE_PATH = 'schema'
TMP_FILE_PATH = './tmp'

env = Env()
env.read_env()
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    ENV = env("FLASK_ENV", "development")
    SECRET_KEY = os.getenv('SECRET_KEY')
    SEND_FILE_MAX_AGE_DEFAULT = env.int("SEND_FILE_MAX_AGE_DEFAULT", 0)
    CACHE_TYPE = env("CACHE_TYPE", "SimpleCache")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PORT = env.int("APP_PORT", 5000)