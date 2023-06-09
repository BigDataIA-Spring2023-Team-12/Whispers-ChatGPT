import boto3
import random
from botocore.exceptions import NoCredentialsError
import streamlit as st
import sqlite3
import os


def get_files_from_s3_bucket(bucket_name, access_key, secret_key):
    """
    Retrieves a list of file names from an AWS S3 bucket.

    Parameters:
        bucket_name (str): The name of the S3 bucket to retrieve file names from.
        access_key (str): The AWS access key ID.
        secret_key (str): The AWS secret access key.

    Returns:
        List[str]: A list of file names in the S3 bucket.

    Raises:
        NoCredentialsError: If AWS credentials are not available.
        Exception: If there was an error accessing the S3 bucket.
    """
    s3 = boto3.client("s3", aws_access_key_id=access_key, aws_secret_access_key=secret_key)
    files = []
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
        for obj in response['Contents']:
            files.append(obj['Key'])
    except NoCredentialsError:
        st.error('AWS credentials not available')
    except Exception as e:
        st.error(f'Error accessing S3 bucket: {e}')
    return files


def upload_file_to_s3(file, bucket_name, access_key, secret_key):
    """
    Uploads a file object to an AWS S3 bucket.

    Parameters:
        file (file object): The file object to upload.
        bucket_name (str): The name of the S3 bucket to upload to.
        access_key (str): The AWS access key ID.
        secret_key (str): The AWS secret access key.

    Returns:
        None

    Raises:
        NoCredentialsError: If AWS credentials are not available.
        Exception: If there was an error uploading the file to S3.
    """

    s3 = boto3.client("s3", aws_access_key_id=access_key, aws_secret_access_key=secret_key)
    # Button to upload file
    if st.button('Upload to S3') and file is not None:
        # Upload file to S3
        try:
            s3.upload_fileobj(file, bucket_name, file.name)
            st.success(f'{file.name} uploaded to {bucket_name} bucket')
        except NoCredentialsError:
            st.error('AWS credentials not available')
        except Exception as e:
            st.error(f'Error uploading {file.name}: {e}')


def write_generic_question_to_database(filename, db_path):
    """
    Writes a question and file name to a SQLite database.

    Parameters:
        question (str): The question to be written to the database.
        file_name (str): The name of the audio file.
        db_path (str): The file path of the SQLite database.

    Returns:
        None
        :param db_path:
        :param filename:
    """
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS general_questions
             (id INTEGER PRIMARY KEY, filename TEXT, question TEXT)''')

    questions = {
        "1": "What are the main takeaways from the meeting?",
        "2": "GIve a brief summary of the meeting?",
        "3": "What is the main topic being discussed in the meeting?",
        "4": "Which language is being spoken?",
        "5": "How long is the meeting duration?"
    }

    # Select two random questions
    question1, question2 = random.sample(questions.values(), 2)

    # Write question and file name to database
    c.execute("INSERT INTO questions (filename, question) VALUES (?, ?)", (filename, question1))
    c.execute("INSERT INTO questions (filename, question) VALUES (?, ?)", (filename, question2))
    conn.commit()
    # st.write(f'You submitted the question: {generic_question} for the file: {filename}')

    # Close SQLite database connection
    conn.close()



# Function to create tables
def create_tables(conn):
    c = conn.cursor()
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS questions (
            Id INTEGER PRIMARY KEY,
            Filename TEXT,
            transcript TEXT,
            general_questions TEXT,
            answers TEXT
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS user_questions (
            Id INTEGER PRIMARY KEY,
            Filename TEXT,
            user_question TEXT,
            answers TEXT
        )
    ''')




def upload_file_to_s3_batch(file, bucket_name, access_key, secret_key):
    """
    Uploads a file object to an AWS S3 bucket.

    Parameters:
        file (file object): The file object to upload.
        bucket_name (str): The name of the S3 bucket to upload to.
        access_key (str): The AWS access key ID.
        secret_key (str): The AWS secret access key.

    Returns:
        None

    Raises:
        NoCredentialsError: If AWS credentials are not available.
        Exception: If there was an error uploading the file to S3.
    """

    s3 = boto3.client("s3", aws_access_key_id=access_key, aws_secret_access_key=secret_key)
    folder_name = "batch"
    file_name = os.path.basename(file.name)
    s3_key = f"{folder_name}/{file_name}"
    
    # Button to upload file
    if st.button('Upload to S3') and file is not None:
        # Upload file to S3
        try:
            s3.upload_fileobj(file, bucket_name, s3_key)
            st.success(f'{file.name} uploaded to {bucket_name}/{folder_name} folder')
        except NoCredentialsError:
            st.error('AWS credentials not available')
        except Exception as e:
            st.error(f'Error uploading {file.name}: {e}')



def get_response_from_db(selected_filename, user_response):
    """
    This function takes in a filename and response returned by the gpt_response function,
    stores them in an SQLite database named "questions.db" with a table named "user_questions",
    and displays both fields as text boxes using Streamlit.

    Parameters:
    -----------
    filename : str
        The filename returned by the gpt_response function.
    response : str
        The response returned by the gpt_response function.

    Returns:
    --------
    None
    """

    # Connect to the SQLite database
    conn = sqlite3.connect('questions.db')
    c = conn.cursor()

    # Create the table if it doesn't already exist
    c.execute('''CREATE TABLE IF NOT EXISTS user_questions
                 (filename TEXT, response TEXT)''')

    # Insert the data into the table
    c.execute("INSERT INTO user_questions VALUES (?, ?)", (selected_filename, user_response))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    # Display the data using Streamlit text boxes
    st.text_input('Filename:', selected_filename)
    st.text_input('Response:', user_response)