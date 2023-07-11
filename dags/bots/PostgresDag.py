from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import smtplib
import logging

# Definir los argumentos del DAG
default_args = {
    'owner': 'pato',
    'start_date': datetime(2023, 7, 11),
    'retries': 1,
}

# Definir la función de extracción
def extraccion():
    import psycopg2

    conexion = psycopg2.connect(
        host='172.18.0.2',
        port=5432,
        database='postgres',
        user='airflow',
        password='airflow'
    )

    # Crear un cursor para la consulta
    cursor = conexion.cursor()
    query = "SELECT gender, age, course, marital_status, depression, anxiety, specialist_for_a_treatment FROM student_mental_health"
    # Ejecutar la consulta
    cursor.execute(query)
    # Resultado de la consulta
    resultado = cursor.fetchall()

    # Cerrar el cursor y la conexión a la base de datos
    cursor.close()
    conexion.close()
    return resultado

# Definir la función de transformación
# Definir la función de transformación
def transformacion():
    datos = extraccion()
    # Obtener la columna "age"
    ages = [row[1] for row in datos if row[1] is not None]

    if len(ages) > 0:
        # Calcular la media
        media = sum(ages) / len(ages)

        # Calcular la mediana
        sorted_ages = sorted(ages)
        n = len(sorted_ages)
        if n % 2 == 0:
            mediana = (sorted_ages[n // 2 - 1] + sorted_ages[n // 2]) / 2
        else:
            mediana = sorted_ages[n // 2]

        # Calcular la moda
        conteo_edades = {}
        for age in sorted_ages:
            if age in conteo_edades:
                conteo_edades[age] += 1
            else:
                conteo_edades[age] = 1
        moda = max(conteo_edades, key=conteo_edades.get)

        # Imprimir los resultados
        logging.info("Media de edad: %s", media)
        logging.info("Mediana de edad: %s", mediana)
        logging.info("Moda de edad: %s", moda)
    else:
        logging.info("No se encontraron valores válidos en la columna 'age'.")



# Definir la función de carga
def carga():
    import psycopg2

    # Conectar a la base de datos
    conexion = psycopg2.connect(
        host='172.18.0.2',
        port=5432,
        database='postgres',
        user='airflow',
        password='airflow'
    )

    # Obtener los datos de extraccion()
    datos = extraccion()

    # Crear un cursor para la consulta
    cursor = conexion.cursor()

    # Crear la nueva tabla
    cursor.execute("CREATE TABLE nueva_tabla (gender VARCHAR(255), age INT4, course VARCHAR(50), marital_status VARCHAR(50), depression VARCHAR(50), anxiety VARCHAR(50), specialist_for_a_treatment VARCHAR(50))")

    # Insertar los datos en la nueva tabla
    for fila in datos:
        cursor.execute("INSERT INTO nueva_tabla (gender, age, course, marital_status, depression, anxiety, specialist_for_a_treatment) VALUES (%s, %s, %s, %s, %s, %s, %s)", fila)

    # Confirmar los cambios en la base de datos
    conexion.commit()

    # Cerrar el cursor y la conexión a la base de datos
    cursor.close()
    conexion.close()

def send():
    try:
        x=smtplib.SMTP('smtp.gmail.com',587)
        x.starttls()
        #conig_data=get_document("MentalHealthCollection",{"Indicator":"Toma medicamento las ultimas dos semanas"})
        #print(conig_data)
        x.login("patriciobazantes@gmail.com","jmlfuhvvxwjzrher")
        subject="Deber Airflow"
        body_text="El ETL fue satisfactorio"
        message="subject: {}\n\n{}".format(subject, body_text)
        x.sendmail("patriciobazantes@gmail.com","jpbazantes@espe.edu.ec",message)
        print("Success")
    except Exception as exception:
        print(exception)
        print("Failure")

# Crear el DAG
dag = DAG('carga_datos', default_args=default_args, schedule_interval=None)

# Definir la tarea de extracción utilizando PythonOperator
extraccion_operator = PythonOperator(
    task_id='extraccion_task',
    python_callable=extraccion,
    dag=dag
)

# Definir la tarea de transformación utilizando PythonOperator
transformacion_operator = PythonOperator(
    task_id='transformacion_task',
    python_callable=transformacion,
    dag=dag
)

# Definir la tarea de carga utilizando PythonOperator
carga_operator = PythonOperator(
    task_id='carga_task',
    python_callable=carga,
    dag=dag
)

send_operator = PythonOperator(
    task_id='send_task',
    python_callable=send,
    dag=dag
)

# Establecer las dependencias de las tareas
extraccion_operator >> transformacion_operator >> carga_operator >> send_operator
