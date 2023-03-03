from datetime import timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago


_BASE = '/Users/yeonwoosung/Desktop/DevOpsMisc/airflow/db_to_s3/'

dag = DAG(
    'elt_pipeline_sample',
    description='A sample ELT pipeline from DB to S3',
    schedule_interval=timedelta(days=1),
    start_date = days_ago(1),
)

insert_mongodb = BashOperator(
    task_id='insert_mongodb',
    bash_command=f'set -e; python3 {_BASE}sample_mongodb.py',
    dag=dag
)

extract_extract_mysql_full = BashOperator(
    task_id='extract_mysql_incremental',
    bash_command=f'set -e; python3 {_BASE}extract_mysql_full.py',
    dag=dag
)

extract_mongodb = BashOperator(
    task_id='extract_mongodb',
    bash_command=f'set -e; python3 {_BASE}extract_mongodb.py',
    dag=dag
)

# Define the order of execution
insert_mongodb >> extract_mongodb >> extract_extract_mysql_full
