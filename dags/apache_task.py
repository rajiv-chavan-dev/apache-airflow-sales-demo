from airflow import DAG    
from airflow.operators.python_operator import PythonOperator
from datetime import datetime,timedelta
import task

#creating Default arguments here
default_args = {
    "owner":"rajiv.chavan",
    "depends_on_past":False,
    "start_date":datetime(2023,9,7),
    "retries":0,
    "retry_delay":timedelta(minutes=5),
}


#creating DAG here
dag = DAG('csv_to_postgresql',default_args = default_args,schedule_interval = timedelta(days=1))

#Creating task here
task1 = PythonOperator(
    task_id = "csv_to_postgresql_task",
    python_callable = task.main,
    dag = dag
)

task1
