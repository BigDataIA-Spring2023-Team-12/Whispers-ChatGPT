# Assignement 4 : Model-as-a-Service


## About 

Model as a Service (MaaS) is a cloud computing service model that provides access to pre-built and trained machine learning models, usually through Application Programming Interfaces (APIs). With MaaS, businesses and developers can leverage the expertise of third-party providers to easily integrate machine learning capabilities into their products or services, without the need for extensive knowledge of machine learning or data science. MaaS enables organizations to accelerate the development of AI-powered solutions, reduce development costs and time-to-market, and benefit from the scalability and flexibility of cloud computing.<br><br>

In the scope of this assignment, we will be building a streamlit application for Meeting Intelligence, that interacts with state of the art models developed by OpenAI. <br>
The application will be used for processing audio files from a given meeting into a transcipt and to extract important information related to or discussed within the same.<br><br>

The service will use two popular APIs - Whisper and Chatgpt

1. Whisper:
(https://openai.com/research/whisper)
The Whisper system is an automatic speech recognition system technology that has been programmed using supervised data collected from the internet. This data comprises over 680,000 hours of multilingual and multitask information. By utilizing this vast and varied dataset, the system has demonstrated an increased ability to accurately transcribe speech regardless of accents, background noise or technical jargon. Additionally, the technology has the capability to transcribe multiple languages and translate them into English.<br>
For our service, we will use the whisper API to convert the audio file into processed transcripts which will be utilized by Chatgpt microservice to work upon the textual data.

2. ChatGPT
(https://platform.openai.com/docs/guides/chat)
ChatGPT API is an API (Application Programming Interface) based on the GPT (Generative Pre-trained Transformer) architecture developed by OpenAI. It allows developers to integrate state-of-the-art natural language processing (NLP) capabilities into their applications, such as chatbots, virtual assistants, and other conversational interfaces. The API can generate human-like responses to a wide variety of prompts, including text-based input and voice-based input, making it a powerful tool for building engaging and intelligent conversational applications.<br>
For our service, we will utilize the Chatgpt API which will give answers to pre-defined prompts and user-defined prompts. The API will take the processed audio transcript as produced by whisper and answer general and user-given question based on the provided context. 





## Links
* Codelab Documentation - [Codelab](https://codelabs-preview.appspot.com/?file_id=1CwPu13u5ciGguLL0QcZjw2f8TZfOqSlW74EaKc7tRBE/#2)
* GitHub Organization - [GitHub](https://github.com/BigDataIA-Spring2023-Team-12)
* Streamlit Application - [Streamlit]()


## LEARNINGS/TECH USED
Streamlit<br>
AWS<br>
SQLite<br>
WhisperAPI<br>
ChatGPT API<br>
AirFlow<br>
FastAPI<br>
Docker<br>
End-user testing<ur>
Git (Version Control)<br>
Documentation on Codelabs<br>


## Process Flow

1. Made public and private endpoints with JWT Token based authentication enabled for private endpoints.
2. Designed service plan as below:
- Free - 10 API request limit - reset everyhour
- Gold - 15 API request limit - reset everyhour
- Platinum - 20 API request limit  - reset everyhour
3. Created user registration page with functionality
- Registering as new user and choosing a plan
- Feature to change the password
4. Test the workflow using 3 users each created for a specific plan   
5. Enhanced the logging to capture all user activity request to check the API request count and compare with enrolled plan for the given user.
6. Designed dashboard within streamlit accessible by the admin/developers/owner only to track users’ activity
7. Designed a dashboard for user level analytics 
8. Created a CLI using typer1 to execute the functionality
9. Package the entire CLI as a python wheel package to access all endpoints 
10. Dockerize the microservices
11. Deploy on cloud


### Project Directory Structure

##### /airflow
This folder contains all the functions created for FastAPI endpoints and their respective functional dependencies.

##### /arch-diag
The folder contains a python file to update scape the metadata which will be used for daily scheduling of cron to keep the metadata updated.
##### /data
All the SQLite databases and present under this folder.
##### /streamlit
All the files related related to great-expectations data validation, such as validation suites, checkpoints and generated reports are contained under this folder.
##### /utils
The entire user-interface built using streamlit, the login/registration page, GEOS and Nexrad file downloads and dashboards.



## Run the project
1. Open terminal
2. Browse the location where you want to clone the repository
3. Write the following command and press enter 
````
 git clone https://github.com/BigDataIA-Spring2023-Team-12/Whispers-ChatGPT.git
 ````
 4. Create a virtual environment and activate
 ````
  python -m venv <Virtual_environment_name>
 ````
 5. Install the required dependencies using requirements.txt
 ````
  pip install -r /path/to/requirements.txt
 ````
6. Launch the application by firing up the index.py file in /streamlit




---
## Team Members
1. Harsh Shah - NUID: 002704406 - (shah.harsh7@northeastern.edu)
2. Parva Shah - NUID: 002916822 - (shah.parv@northeastern.edu)
3. Dev Shah - NUID: 002978981 - (shah.devs@northeastern.edu)



## Undertaking

> WE ATTEST THAT WE HAVEN’T USED ANY OTHER STUDENTS’ WORK IN OUR ASSIGNMENT AND ABIDE BY THE POLICIES LISTED IN THE STUDENT HANDBOOK
**Contribution**: 
*   Harsh Shah &emsp; :`33.33%`
*   Parva Shah &emsp; :`33.33%`
*   Dev Shah &emsp;   :`33.33%`
