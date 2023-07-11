from datetime import datetime
from airflow.models import DAG, Variable
from airflow.operators.bash_operator import BashOperator

default_args={
    #Este atributo indica el propietario o responsable del DAG. 
    'owner':'Pato',
    #Indica la fecha y hora a partir de la cual se puede programar la ejecución de las tareas del DAG.
    'start_date':datetime.now()
}

with DAG(
    dag_id="BashOperatorDemo1",
    default_args = default_args,
    schedule_interval=None) as dag:

    start_dag=BashOperator(
        task_id='start_dag',
        bash_command="date"
    )

    start_dag