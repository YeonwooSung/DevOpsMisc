from datetime import datetime, timedelta

from airflow import DAG
from kubernetes.client import models as k8s
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import (
    KubernetesPodOperator,
)


def custom_alert(message):
    #TODO send slack message, etc
    print(message)


resources = k8s.V1ResourceRequirements(
    limits={"memory": "1Gi", "cpu": "1"},
    requests={"memory": "500Mi", "cpu": "0.5"},
)
with DAG(
    "example_kubernetes_python",
    schedule_interval=None,
    start_date=datetime(2020, 2, 2),
    tags=["example"],
) as dag:

    pyspark_submit_sample = KubernetesPodOperator(
        task_id='pyspark_submit_sample',
        name='pyspark_submit_sample',
        namespace='airflow',
        image='spark_client_1:1.0',
        arguments=["pyspark","pyspark_sample.py"], # run pyspark_sample.py with pyspark
        hostnetwork=True,
        in_cluster=True,
        is_delete_operator_pod=True,
        startup_timeout_seconds=300,
        execution_timeout=timedelta(minutes=120),
        retries=2,
        retry_delay=timedelta(minutes=2),
        image_pull_policy='IfNotPresent',
        service_account_name='airflow',
        on_retry_callback=custom_alert("Retry Task"),
        dag=dag
    )
