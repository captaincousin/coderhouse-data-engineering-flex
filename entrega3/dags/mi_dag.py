from airflow import DAG
from airflow.operators.docker_operator import DockerOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2023, 7, 1),
}

with DAG('mi_dag', schedule_interval='0 * * * *', default_args=default_args) as dag:
    tarea_docker = DockerOperator(
        task_id='ejecutar_docker',
        image='imagen_docker_entrega3',
        api_version='auto',
        auto_remove=True,
        command='python mi_script.py',
        docker_url='unix://var/run/docker.sock',
        network_mode='bridge',
        dag=dag
    )
