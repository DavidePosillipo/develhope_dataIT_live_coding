"""
oss: THIS SCRIPT WORKS WHEN THE ROOT IS ONE LEVEL ABOVE THE 'airflow' FOLDER
preliminary steps from terminal
 cd in the root folder (above 'airflow')
export AIRFLOW_HOME=$PWD/airflow #set airflwo home
airflow db init # instantiate db (a lot of stuff is created under airflow folder)
 if not present, create airflow/dags folder; here you will insert your dags python files
airflow standalone # for dev only, instantiate scheduler, user and web ui. Open UI at localhost:8080 and use usr and pw shown in terminal. See https://airflow.apache.org/docs/apache-airflow/stable/start.html
 if you want to set users do
airflow users create \
        --username admin \
        --firstname FIRST_NAME \
        --lastname LAST_NAME \
        --role Admin \
        --email admin@example.org \
        --password admin
        
airflow scheduler && webserver
"""
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import datetime
from airflow.utils.dates import timedelta

import os


workdir = os.getcwd()


#only for PythonOperator
from airflow.decorators import  task
import sys
# di default il sys.path di airflow è solo airflow/config, airflow/plugins e airflow/dags, quindi al contrario di un interpreter python 'normale'
# non viene aggiunta di default in prima posizione la workdir (la dir da cui ho lanciato python, o meglio airflow)
# (vedi https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/modules_management.html)
#quindi se voglio fare import dalla cartella scripts devo aggiungere la workdir (che è un livello sopra scripts)
#in alternativa, a livello di terminale, avrei potuto settare l'env variable PYTHONPATH alla folder desiderata (export PYTHONPATH=path)
sys.path.insert(0,workdir) 
paths=sys.path
from scripts.python_script_for_python_operator import result
from airflow.operators.python import  PythonOperator

with DAG(
    dag_id='test',
    start_date=datetime(2023, 1, 31),
    description='An Airflow DAG to invoke simple dbt commands',
    schedule_interval=timedelta(days=1),
) as dag:
    
    #documentazione di dag: visible in Grap --> DAG docs
    dag.doc_md="""\
        ### Dag di prova
        mostra varie funzionalità
        """

    #pwd and ls commands won't be useful, since airflow is 'activated' inside a tmp directory (see logs in ariflow): if you want to retrieve , e.g., some scripts and run them
    #you can't use commands like ../ or ./, because you are in a tmp folder: you must use full paths, not relative ones
    pwd = BashOperator(
        task_id='pwd',
        bash_command='pwd'
    )

    #add documentation (visible, in the UI, in grid, pwd, task instance details)
    pwd.doc_md="""\
        ### titolo
        questa è una documentazione del task in markdown language
        """

    ls = BashOperator(
        task_id='ls',
        bash_command='ls'
    )
    
    #python CWD will work as expected: python cwd will be the path from which you run the airflow standalone (or scheduler) command
    cwd = BashOperator(
        task_id='cwd',
        bash_command=f'echo {workdir}'
    )

    #python CWD will work as expected: python cwd will be the path from which you run the airflow standalone (or scheduler) command
    syspath = BashOperator(
        task_id='syspath',
        bash_command=f'echo {paths}'
    )

    #the python used is the one from which you run airflow 
    which_python = BashOperator(
        task_id='which_python',
        bash_command='which python'
    )    

    #if I want to run a script in a specific folder (supposign the root, i.e. the folder from which i run airflow, is above the airflow folder), I can cd there && run the script
    #of course scripts can be also outside the airflow directory
    #OSS: since I'm running python from inside the directory where the python file is, eventual imports in the python files must be relative to that root
    #if I use a python operator (see later) I must use imports relative to AIRFLOW_PATH (aka workdir). See difference between python_script_bash_operator and python_script_python_operator 
    python_script = BashOperator(
        task_id='python_script',
        bash_command=f'python {workdir}/scripts/python_script_bash_operator.py'
    )   

    # PythonOperator: use python functions to define tasks, eventually importing from python scripts (not suggested anymore, better use task decorator, see below)
    #why **kwargs? The Airflow engine passes a few variables by default that are accessible in all templates (https://airflow.apache.org/docs/apache-airflow/stable/templates-ref.html)
    # spesso non mi servono, ma se, ad esempio, voglio far comunicare task diversi posso usare ti.xcom_pull() e ti.xcom_pull(), vedi example dag 'tutorial_dag'
    def funzione_python(a, **kwargs):
        new_result=result*a
        print('######## NEW RESULT = ################## = ', new_result)
        task_id = kwargs['ti']
        print('######## task instance = ################## = ', task_id)


    python_op = PythonOperator(
        task_id='python_op',
        python_callable=funzione_python,
        op_kwargs={"a":100} # dizionario coi parametri da passare alla funzione sopra definita
    ) 

    #this_python_op = python_op(a=100)
    # As pythonOperator, but using the task decorator syntax, suggested by official documentation
    @task(task_id="python_op2")
    def funzione_python2(a, **kwargs):
        new_result=result*a
        print('######## NEW RESULT = ################## = ', new_result)
        task_id = kwargs['ti']
        print('######## task instance = ################## = ', task_id)
    

    pwd >> ls >> cwd >> syspath
    which_python >> python_script  
    python_op >> funzione_python2(a=100)


