import datetime

from airflow import DAG
from kubernetes.client import models as k8s
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import (
    KubernetesPodOperator,
)


# set K8S resource limits, requests
resources = k8s.V1ResourceRequirements(
    limits={"memory": "1Gi", "cpu": "1"},
    requests={"memory": "500Mi", "cpu": "0.5"},
)

# create DAG
with DAG(
    "example_kubernetes_python",
    schedule_interval=None,
    start_date=datetime.datetime(2020, 2, 2),
    tags=["example"],
) as dag:

    run_python = KubernetesPodOperator(
        task_id="run_python_script",
        name="run_python_script",
        namespace="insighter-prod",
        image="python:3.10-slim",  # docker image name for the dependent python3 image
        is_delete_operator_pod=True,
        cmds=["python", "-c"],
        arguments=[
            'print("Hello, World!")'
        ],  # Provide either python scripts or path of the python scripts to execute on the k8s pod here
        get_logs=True,
        resources=resources,
        dag=dag
    )
