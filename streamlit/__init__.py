# main home page for streamlit application

import streamlit as st
import sqlite3
from _utils import upload_file_to_s3_batch,get_files_from_s3_bucket, upload_file_to_s3, write_generic_question_to_database, create_tables,get_response_from_db

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

    st.header('Meeting Intelligence Application :bulb:')

    # Set AWS credentials
    access_key = 's3_access_key'
    secret_key = 's3_secret_key'
    bucket_name = 's3_bucket_name'

    # File upload
    file = st.file_uploader('Select an audio file')

    if file is not None:
        upload_file_to_s3(file, bucket_name, access_key, secret_key)
        upload_file_to_s3_batch(file, bucket_name, access_key, secret_key)
        filename = file.name
        write_generic_question_to_database(filename, 'questions.db')
    else:
        st.warning("Please select an audio file to upload.")

    # Connect to SQLite database
    conn = sqlite3.connect('questions.db')
      
    # Create tables
    create_tables(conn)
    
    st.markdown("---")

    files_list = get_files_from_s3_bucket(bucket_name, access_key, secret_key)

    # Display selectbox with file names
    selected_file = st.selectbox("Select a processed audio file", files_list)

    if selected_file:
        st.title('Generic Quentionaire')
        # c.execute("SELECT questions1, question2 from general_questions WHERE filename=?", (selected_file,))
        # result = c.fetchall()
        st.write('Question 1 : What was the main purpose or objective of the meeting?')
        st.write('Question 2: Were all the agenda items discussed and resolved?')
        st.write('Question 3: Was there any conflict or disagreement among the members during the meeting?')
        st.markdown("---")
        st.title('Answers -')
        """
        
        TODO: function to get answers to generic questions

        """
    else:
        st.warning("Please select a file.")

    st.markdown("---")

    # Question input box and submit button
    user_question = st.text_input('Ask a question related to the meeting!')
    if st.button('Submit') and user_question and selected_file:

        selected_filename, user_response = gpt_response() #update with the function name from below TODO
        get_response_from_db(selected_filename, user_response)
        
        """
        TODO: function to take user input and give response using chatgpt api
        
        """
        # c = conn.cursor()
        # c.execute("INSERT INTO questions (question) VALUES (?)", (user_question,))
        # conn.commit()
        # st.write(f'You submitted the question: {user_question}')


    # Close SQLite database connection
    conn.close()



if __name__ == "__main__":
    main()
