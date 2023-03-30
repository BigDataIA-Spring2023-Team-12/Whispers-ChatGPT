from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from utils.s3 import upload_audio_to_s3, upload_text_file_to_s3
from utils.openai import string_to_txt, generate_text

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 3, 30),
    'retries': 1,
}

dag_1 = DAG('upload_audio_to_s3_dag', default_args=default_args)

upload_audio_task = PythonOperator(
    task_id='upload_audio_to_s3_task',
    python_callable=upload_audio_to_s3,
    op_kwargs={
        'audio_file_path': 'path/to/audio/file',
        's3_bucket_name': 'the-data-guys',
        's3_object_key': 'path/to/s3'
    },
    dag=dag_1,
)

dag_2 = DAG('string_to_txt_dag', default_args=default_args)

transcript_to_txt_task = PythonOperator(
    task_id='string_to_txt_task',
    python_callable=string_to_txt,
    op_kwargs={
        'response': 'transcript string',
        'filename': 'output_file_name.txt'
    },
    dag=dag_2,
)

dag_3 = DAG('upload_text_file_to_s3_dag', default_args=default_args)

upload_txt_task = PythonOperator(
    task_id='upload_text_file_to_s3_task',
    python_callable=upload_text_file_to_s3,
    op_kwargs={
        'file_path': 'path/to/txt/file',
        'bucket_name': 'your-bucket-name',
        'object_name': 'path/to/s3'
    },
    dag=dag_3,
)

dag_4 = DAG('generate_text_dag', default_args=default_args)


generate_text_task = PythonOperator(
    task_id='generate_text_task',
    python_callable=generate_text,
    op_kwargs={
        'prompt': 'prompt string'
    },
    dag=dag_4,
)
