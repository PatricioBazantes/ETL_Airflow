#ETL CON APACHE AIRFLOW

Este proyecto es un ejemplo de un ETL (Extract, Transform, Load) implementado utilizando Apache Airflow. El objetivo del proyecto es mostrar cómo se puede utilizar Airflow para programar y orquestar tareas de extracción, transformación y carga de datos.
Como Plus, se envia un correo electronico desde un correo origen el cual esta programado con un metodo el cual recibe un correo destino, con el mensaje de que el ETL fue satisfactorio

## Requisitos

- Docker
- docker-compose
- DBeaver
- Editor de codigo (Recomendado Visual Code)

## Instalación
**1. Forma ** Clic en Code y download Zip.
**2. Forma** Clona este repositorio:
   git clone https://github.com/PatricioBazantes/ETL_Airflow.git

##Configuración
El archivo docker-compose.yml contiene la configuración de los servicios del proyecto. Puedes personalizar los siguientes parámetros en el archivo:

POSTGRES_USER: Usuario de la base de datos PostgreSQL.
POSTGRES_PASSWORD: Contraseña del usuario de la base de datos PostgreSQL.
POSTGRES_DB: Nombre de la base de datos PostgreSQL.
AIRFLOW_CORE_SQL_ALCHEMY_CONN: Cadena de conexión a la base de datos de Airflow.
Además, puedes ajustar los límites de recursos (mem_limit y cpus) según tus necesidades.

Con esta configuracion, se puede acceder al postgres
[![Conexion2](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgVmlf-UjrJvbmW4Wqb_LINJJHSjOqROE9v44OVJ6RG5qLNlMUEZZr6QJL67MoOCJvZv1d68q-kTt3MgCW5sDpnr2QJb_Njg_k8GAgyTh7P_MhsT7CGmykloH0vjtr_xL1J6egEgAHaick9EKxP4pDDXMGSwPN87jVcKoOUR2Uu5ded9vJfTIazGAYgVBgT/s320/1.png "Conexion2")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgVmlf-UjrJvbmW4Wqb_LINJJHSjOqROE9v44OVJ6RG5qLNlMUEZZr6QJL67MoOCJvZv1d68q-kTt3MgCW5sDpnr2QJb_Njg_k8GAgyTh7P_MhsT7CGmykloH0vjtr_xL1J6egEgAHaick9EKxP4pDDXMGSwPN87jVcKoOUR2Uu5ded9vJfTIazGAYgVBgT/s320/1.png "Conexion2")
##Uso
Una vez que los contenedores estén en ejecución, puedes acceder a la interfaz de Airflow en tu navegador web visitando http://localhost:8090. Aquí podrás ver y administrar los DAGs y tareas programados.

Una vez ahi, se puede crear la conexion para postgres.
Se debe consultar la direccion del host con el siguiente comando
**docker inspect -f "{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}" airflow-docker-compose-master-postgres-1**

Una vez, se configura la conexion en el airflow, y posteriormente en codigo.
[![Conexion](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiFBhfhcWjTYpC1BYMpAPCZDwucn5JZm-UXPVGbkr6E_EoD5EXBqrwl9mcqXLQ5mMcDUeXVNibYaR3hNWuMCmvbgduGFihULpa07byfiqO7Asfacn-chj-omOPBI1hxK590PXyyPFnS0KvhbgEJlF63RZKjXmq1G6Hgp6xgg03ZQH2UBoWQDRvZxZ2eMw0N/s320/2.png "Conexion")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiFBhfhcWjTYpC1BYMpAPCZDwucn5JZm-UXPVGbkr6E_EoD5EXBqrwl9mcqXLQ5mMcDUeXVNibYaR3hNWuMCmvbgduGFihULpa07byfiqO7Asfacn-chj-omOPBI1hxK590PXyyPFnS0KvhbgEJlF63RZKjXmq1G6Hg::p6xgg03ZQH2UBoWQDRvZxZ2eMw0N/s320/2.png "Conexion")

##Base de datos
Se descarga Student Mental health.csv.
Se accede a la base de DBeaver
Se completa las credenciales y se importa los datos.

##Estructura del Proyecto
El proyecto sigue la siguiente estructura de carpetas:

- dags/: Contiene los archivos de definición de los DAGs de Airflow.
- plugins/: Carpeta opcional para agregar plugins personalizados de Airflow.
- docker-compose.yml: Archivo de configuración de Docker Compose.
- README.md: Documentación del proyecto.

###DAG: carga_datos
Este proyecto contiene un DAG llamado carga_datos que realiza el proceso de ETL. El DAG está definido en el archivo dags/carga_datos.py. A continuación se muestra una descripción de las tareas incluidas en el DAG:

####Tarea: extraccion_task
Esta tarea realiza la extracción de datos de una base de datos PostgreSQL. Utiliza la función extraccion() definida en el archivo dags/carga_datos.py.

####Tarea: transformacion_task
Esta tarea realiza la transformación de los datos extraídos. Utiliza la función transformacion() definida en el archivo dags/carga_datos.py. La transformación calcula la media, mediana y moda de la columna "age" de los datos extraídos.

####Tarea: carga_task
Esta tarea realiza la carga de los datos transformados en una nueva tabla en la base de datos PostgreSQL. Utiliza la función carga() definida en el archivo dags/carga_datos.py.

####Tarea: send_task
Esta tarea envía un correo electrónico para notificar que el ETL ha sido exitoso. Utiliza la función send() definida en el archivo dags/carga_datos.py.

##Resultados
###DAGS Corriendo
[![DAGS](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgbAsYhlXQKawonutQ7Raamby-Q_TLhPLFnhW9TqsWvcw0GxFNJIsq7ABhyO2yC7m8VJSK_dmVsMKiD9fVWzOlx1UwzYJpJZN2Fs1mqNzcI3Kipbq3Z-aBOPDz83CSbx4ljqs37hBVoO10szRJT6mk2oHIqFtNJcAYeWKRFI67TT1F4okaEsUgjfe5NrHpY/s320/3.png "DAGS")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgbAsYhlXQKawonutQ7Raamby-Q_TLhPLFnhW9TqsWvcw0GxFNJIsq7ABhyO2yC7m8VJSK_dmVsMKiD9fVWzOlx1UwzYJpJZN2Fs1mqNzcI3Kipbq3Z-aBOPDz83CSbx4ljqs37hBVoO10szRJT6mk2oHIqFtNJcAYeWKRFI67TT1F4okaEsUgjfe5NrHpY/s320/3.png "DAGS")

###Trees
[![Trees view](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhfVIvZ0pWsTVnKH9sH01-O_RFRnvNlJfgIA3EgpgNko76x6i2OC7eb_wHGjGG6L7kaTtClXW7Yy_rLhLbnbOPX1UDRRAUzzAOkvpR9_aORf_wcPZmI-6aURN1aL90Xc-F1dT-nT9RVtulfw8n0PMgbqhj20i3g89IEsXOWbYwwU-6UwtHh0KF0p6C9i0ms/s320/4.png "Trees view")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhfVIvZ0pWsTVnKH9sH01-O_RFRnvNlJfgIA3EgpgNko76x6i2OC7eb_wHGjGG6L7kaTtClXW7Yy_rLhLbnbOPX1UDRRAUzzAOkvpR9_aORf_wcPZmI-6aURN1aL90Xc-F1dT-nT9RVtulfw8n0PMgbqhj20i3g89IEsXOWbYwwU-6UwtHh0KF0p6C9i0ms/s320/4.png "Trees view")

###Correo
[![Correo](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5SqgDucsZOgw2a4dcqyDryMwfWaI59Yz7t1o3s8DjA1R5ykdB67NFEPf_u0Kk03S2D0j68h5IG5W-o9273Z_ZsWCNXuwv4_m7sPjssG47aqN47Hh3kahyjOBQ768oGAQe0ueH-mW3VGqxSRTU63S5k4PFlxSyDW5Me7nWAdzkbBbc0Ceuy5Feups__5zy/s320/5.png "Correo")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5SqgDucsZOgw2a4dcqyDryMwfWaI59Yz7t1o3s8DjA1R5ykdB67NFEPf_u0Kk03S2D0j68h5IG5W-o9273Z_ZsWCNXuwv4_m7sPjssG47aqN47Hh3kahyjOBQ768oGAQe0ueH-mW3VGqxSRTU63S5k4PFlxSyDW5Me7nWAdzkbBbc0Ceuy5Feups__5zy/s320/5.png "Correo")
