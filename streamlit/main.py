# main home page for streamlit application

import streamlit as st
import sqlite3
import boto3
from botocore.exceptions import NoCredentialsError

# Set background image
page_bg_img = '''
<style>
body {
background-image: url("https://www.ai-cube.eu/wp-content/uploads/2021/03/AI_Getty-1179477351-scaled-e1611778221405.jpg") !important;
background-size: cover;
}
</style>
'''

st.set_page_config(page_title='Meeting Intelligence Application', page_icon=':microphone:', layout='wide')
st.markdown(page_bg_img, unsafe_allow_html=True)

# Set up S3 credentials
AWS_ACCESS_KEY_ID = 'your_access_key'
AWS_SECRET_ACCESS_KEY = 'your_secret_key'
BUCKET_NAME = 'your_bucket_name'
s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

# Connect to SQLite database
conn = sqlite3.connect('questions.db')
c = conn.cursor()

# Create table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS questions
             (id INTEGER PRIMARY KEY AUTOINCREMENT, question text)''')

# Create UI
st.title('Meeting Intelligence Application')

# Button to select file
file = st.file_uploader('Select an audio file')

# Button to upload file
if st.button('Upload to S3') and file is not None:
    # Upload file to S3
    try:
        s3.upload_fileobj(file, BUCKET_NAME, file.name)
        st.success(f'{file.name} uploaded to {BUCKET_NAME} bucket')
    except NoCredentialsError:
        st.error('AWS credentials not available')
    except Exception as e:
        st.error(f'Error uploading {file.name}: {e}')

st.markdown("---")

# Get list of files from S3 bucket
files = []
try:
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)
    for obj in response['Contents']:
        files.append(obj['Key'])
except NoCredentialsError:
    st.error('AWS credentials not available')
except Exception as e:
    st.error(f'Error accessing S3 bucket: {e}')

# Dropdown to select file
if len(files) > 0:
    selected_file = st.selectbox('Select a file', files)
else:
    st.warning('No files found in S3 bucket')

st.markdown("---")

# Define the questions as a tuple
questions_list = {
    "What was the main purpose or objective of the meeting?",
    "Were all the agenda items discussed and resolved?",
    "Was there any conflict or disagreement among the members during the meeting?",
    "Were there any significant changes or decisions made during the meeting that will impact the organization or "
    "community?",
    "Was everyone given the opportunity to participate and voice their opinions or concerns during the meeting?"
}

# Create a Streamlit app
st.header("Generic Questionaire:")
for question in questions_list:
    st.text(question)

st.markdown("")

# Question input box and submit button
question = st.text_input('Enter a question')
if st.button('Submit') and question:
    # Write question to SQLite database
    c.execute("INSERT INTO questions (question) VALUES (?)", (question,))
    conn.commit()
    st.write(f'You submitted the question: {question}')

# Close SQLite database connection
conn.close()
