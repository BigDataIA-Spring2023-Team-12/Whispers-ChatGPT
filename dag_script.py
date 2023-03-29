import boto3
from s3_functions import upload_audio_to_s3, upload_text_file_to_s3
from whisper_chatgpt import transcribe_audio, create_prompt, generate_text, string_to_txt



# On the front end upload button saves audio file in adhoc folder then we call this script

def adhoc_script(audio_file_path,bucket_name,s3_path,file_name):
    # 1. upload file to s3
    upload_audio_to_s3(audio_file_path,bucket_name,s3_path)
    # 2. send file to whisper api
    transcript = transcribe_audio(audio_file_path,"whisper-1")
    # 3. convert transcript into txt file
    file_path = string_to_txt(transcript,file_name)
    print(file_path)
    # 5. upload txt file to s3
    upload_text_file_to_s3(file_path,bucket_name,file_path) 
    # 4. create prompt
    prompt = create_prompt(transcript)
    print(prompt)
    # 5. ask question to openai
    response = generate_text(prompt)

    return response


# def batch_script():


# res = adhoc_script("adhoc/steve-jobs-think-different.mp3","the-data-guys","adhoc/steve-jobs-think-different.mp3","steve-jobs-think-different")
# print(res)