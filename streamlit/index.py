# main home page for streamlit application

import streamlit as st
import sqlite3
import boto3
from botocore.exceptions import NoCredentialsError



def main():
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


    
    # Set AWS credentials
    access_key = 's3_access_key'
    secret_key = 's3_secret_key'
    bucket_name = 's3_bucket_name'


    # File upload
    file = st.file_uploader('Select an audio file')
    
    if file is not None:
        upload_file_to_s3(file, bucket_name, access_key, secret_key)
    else:
        st.warning("Please select an audio file to upload.")

    # Connect to SQLite database
    conn = sqlite3.connect('questions.db')
    c = conn.cursor()

    st.markdown("---")

    files_list = get_files_from_s3_bucket(bucket_name, access_key, secret_key)

    # Display selectbox with file names
    selected_file = st.selectbox("Select a processed audio file", files_list)

    if selected_file:
        st.success(f"You selected: {selected_file}")
    else:
        st.warning("Please select a file.")
    


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
            


if __name__ == "__main__":
    main()
