from datetime import datetime
from airflow.models import DAG, Variable
from airflow.operators.python_operator import PythonOperator
from bots.EmailHelper import send

default_args={
    #Este atributo indica el propietario o responsable del DAG. 
    'owner':'Pato',
    #Indica la fecha y hora a partir de la cual se puede programar la ejecución de las tareas del DAG.
    'start_date':datetime(2023,7,9)
}

with DAG(
    dag_id='PythonEmailDag',
    default_args=default_args,
    schedule_interval=None) as dag:
    
    start_dag=PythonOperator(
        task_id="start_dag",
        python_callable=send
    )
start_dag