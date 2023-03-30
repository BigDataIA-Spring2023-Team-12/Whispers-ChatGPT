from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from utils._s3 import upload_audio_to_s3, upload_text_file_to_s3
from utils._openai import transcribe_audio, string_to_txt, create_prompt, generate_text

def function_1():
    pass


def function_2():
    pass


def function_3():
    pass


def function_4():
    pass


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 3, 30),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('my_dag', default_args=default_args, catchup=False, schedule_interval=timedelta(days=1))

task_1 = PythonOperator(task_id='function_1', python_callable=function_1, dag=dag)
task_2 = PythonOperator(task_id='function_2', python_callable=function_2, dag=dag)
task_3 = PythonOperator(task_id='function_3', python_callable=function_3, dag=dag)
task_4 = PythonOperator(task_id='function_4', python_callable=function_4, dag=dag)


task_1 >> task_2 >> task_3 >> task_4
