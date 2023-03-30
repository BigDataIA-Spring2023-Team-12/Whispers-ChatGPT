
# Project Title

A brief description of what this project does and who it's for

# Assignement 4 : Model-as-a-Service


## About 

Model as a Service (MaaS) is a cloud computing service model that provides access to pre-built and trained machine learning models, usually through Application Programming Interfaces (APIs). With MaaS, businesses and developers can leverage the expertise of third-party providers to easily integrate machine learning capabilities into their products or services, without the need for extensive knowledge of machine learning or data science. MaaS enables organizations to accelerate the development of AI-powered solutions, reduce development costs and time-to-market, and benefit from the scalability and flexibility of cloud computing.<br><br>

In the scope of this assignment, we will be building a streamlit application for Meeting Intelligence, that interacts with state of the art models developed by OpenAI. <br>
The application will be used for processing audio files from a given meeting into a transcipt and to extract important information related to or discussed within the same.<br><br>

The service will use two popular APIs - Whisper and Chatgpt

1. Whisper:<br>
(https://openai.com/research/whisper) <br>
The Whisper system is an automatic speech recognition system technology that has been programmed using supervised data collected from the internet. This data comprises over 680,000 hours of multilingual and multitask information. By utilizing this vast and varied dataset, the system has demonstrated an increased ability to accurately transcribe speech regardless of accents, background noise or technical jargon. Additionally, the technology has the capability to transcribe multiple languages and translate them into English.<br><br>
For our service, we will use the whisper API to convert the audio file into processed transcripts which will be utilized by Chatgpt microservice to work upon the textual data.

2. ChatGPT:<br>
(https://platform.openai.com/docs/guides/chat) <br>
ChatGPT API is an API (Application Programming Interface) based on the GPT (Generative Pre-trained Transformer) architecture developed by OpenAI. It allows developers to integrate state-of-the-art natural language processing (NLP) capabilities into their applications, such as chatbots, virtual assistants, and other conversational interfaces. The API can generate human-like responses to a wide variety of prompts, including text-based input and voice-based input, making it a powerful tool for building engaging and intelligent conversational applications.<br><br>
For our service, we will utilize the Chatgpt API which will give answers to pre-defined prompts and user-defined prompts. The API will take the processed audio transcript as produced by whisper and answer general and user-given question based on the provided context. 




## Architecture Diagram
![Untitled Diagram drawio (1)](https://user-images.githubusercontent.com/114712818/228984666-2e4f1cc6-6fc8-48e6-bef4-db0e3f3b12eb.png)


## Links
* Codelab Documentation - [Codelab](https://codelabs-preview.appspot.com/?file_id=1kgqo9YugHncpkeynNeNWf4kqK4DDCYWvnRxecByi8eU/#1)
* GitHub Repository - [GitHub](https://github.com/BigDataIA-Spring2023-Team-12/Whispers-ChatGPT)
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

Process Flow :-

1. Browse for an audio file from the system's local files.
2. An upload button will store the audio file to an Amazon S3 bucket's folder.
3. Use Whisper API to process the audio file and convert to a textual transcript.
4. The whisper API will fetch the audio fie from S3 bucket's folder and store the processed file output into another bucket of S3 and SQLite db.
5. Define a generic questionaire for the meetings audio.
6. Use chatgpt API to get answers to these generic questions (send both the transcript and questions to chatgpt).
7. Write the output into a database along with the associated filename.
8. A select box drop-down on the streamlit interface will get list of all the files from the processed folder in the S3 bucket.
9. On selecting a specific file, display the generic questions with answers, and a text box for user questions and a submit button.
10. The submit button should again trigger the chatgpt api to get an answer and write in into the db.
11. Log user activity by storing the question and their responses.
12. Use airflow to automate workflow. Create 2 dags - adhoc process and batch process.
13. Adhoc process will be triggered on the file upload to S3 button.
14. Batch process will run once a day, using cron. The dag will process all the file collectively.



## Project Directory Structure

##### /airflow
This folder contains all the airflow dags created for adhoc and batch processes and their respective functional dependencies.

##### /arch-diag
It includes the system architecture.

##### /data
The audio files of the meetings are stored here for reference.

##### /streamlit
Includes the streamlit application interface for the user to interact with the whisper and chatgpt functionalities. It consists of 2 files, __init__.py and utils.py. Launch the application by running "__init__". The dependent functions and utilities are written and imported from "utils". Also contains the SQLite db file initialized for storing questions data.  


##### /utils
The backend files which consists of the functions to execute the whisper and chat APIs. 



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
6. Launch the application by firing up the __init__.py file in /streamlit




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
