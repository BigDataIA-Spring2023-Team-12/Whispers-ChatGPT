from diagrams import Diagram, Cluster
from diagrams.onprem.client import Client
from diagrams.onprem.compute import Server
from diagrams.onprem.container import Docker
from diagrams.onprem.iac import Airflow
from diagrams.programming.language import Python

with Diagram("Architecture Diagram", show=False):
    with Cluster("Services"):
        streamlit = Client("Streamlit")
        whisper_api = Server("Whisper API")
        chatgpt_api = Docker("ChatGPT API")
    airflow = Airflow("Airflow")
    
    streamlit >> whisper_api >> chatgpt_api
    chatgpt_api >> whisper_api
    chatgpt_api >> Python("ChatGPT model")
    Python("Training data") >> chatgpt_api
    airflow >> whisper_api
