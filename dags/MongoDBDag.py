'''
from datetime import datetime
from airflow.models import DAG, Variable
from airflow.operators.python_operator import PythonOperator
from bots.MongodbHelper import get_connection, insert_document, get_document, update_document

default_args={
    #Este atributo indica el propietario o responsable del DAG. 
    'owner':'Pato',
    #Indica la fecha y hora a partir de la cual se puede programar la ejecución de las tareas del DAG.
    'start_date':datetime(2023,7,9)
}


with DAG(
    dag_id='MongoDBDag',
    description='Un DAG para ejecutar funciones relacionadas con MongoDB',
    default_args=default_args,
    schedule_interval=None,
    catchup=False) as dag:

    insert_task = PythonOperator(
        task_id='insert_task',
        python_callable=lambda: insert_document("MentalHealthCollection", {"Indicator": "Toma medicamento las ultimas tres semanas", "Group": "By Age", "State": "Bolivia", "Subgroup": "20 - 27 years", "Time Period": 10, "Time Period Start Date": "02/07/2023", "Time Period Start Date": "09/07/2023"}),
        dag=dag
    )

    get_task = PythonOperator(
        task_id='get_task',
        python_callable=lambda: get_document("MentalHealthCollection", {"Indicator": "Toma medicamento las ultimas dos semanas", "Group": "By Age", "State": "Ecuador", "Subgroup": "20 - 25 years", "Time Period": 12, "Time Period Start Date": "01/07/2023", "Time Period Start Date": "09/07/2023"}),
        dag=dag
    )

    update_task = PythonOperator(
        task_id='update_task',
        python_callable=lambda: update_document("MentalHealthCollection", {"Indicator": "Toma medicamento las ultimas dos semanas", "Group": "By Age", "State": "Ecuador", "Subgroup": "20 - 25 years", "Time Period": 12, "Time Period Start Date": "01/07/2023", "Time Period Start Date": "09/07/2023"}),
        dag=dag
    )

    get_task.set_upstream(insert_task)
    update_task.set_upstream(get_task)
'''