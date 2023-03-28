## AIRFLOW WORKS ON UNIX/MAC ONLY
- cd in this folder

### set airflow home
- export AIRFLOW_HOME=$PWD/airflow

### verify AIRFLOW_HOME points to current_folder/airflow, printing its value in the terminal
- echo $AIRFLOW_HOME

### Initialize the db (to do only once, or the results will be overwritten): many config and logs files will be created under /airflow folder. In airflow.cfg, you can see the dags_folder variabl,e which defaults to ./airflow/dags. If you want, you can change it. 
- airflow db init

### If not present, create the dags folder, where the main files will be inserted
- mkdir dags

### Run airflow (it could take a couple of minutes)
- airflow standalone

### When this message appears in the terminal, airflow is ready
standalone | Airflow is ready \
standalone | Login with username: admin  password: UmcYmkrM8dk8hCUb \
standalone | Airflow Standalone is for development purposes only. Do not use this in production!

### Open the web UI in a browser (localhost:8080), insert credentials shown in the terminal (see above for an example) and search for the dag named 'test'. You can manually trigger it with the play button in the UI

# to exit airflow
- ctrl+c