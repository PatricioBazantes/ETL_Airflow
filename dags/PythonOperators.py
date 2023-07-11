from datetime import datetime
from airflow.models import DAG, Variable
from airflow.operators.python_operator import PythonOperator
from bots.Python_Helper import call

# en default_args se aplicarán a todas las tareas dentro del DAG, 
# a menos que se especifiquen valores diferentes de manera explícita en las tareas individuales.
default_args={
    #Este atributo indica el propietario o responsable del DAG. 
    'owner':'Pato',
    #Indica la fecha y hora a partir de la cual se puede programar la ejecución de las tareas del DAG.
    'start_date':datetime.now()
}

with DAG(
    dag_id="PythonOperatorDemo1",
    default_args = default_args,
    schedule_interval=None) as dag:

    start_dag=PythonOperator(
        task_id='start_dag',
        python_callable=call
    )

    start_dag