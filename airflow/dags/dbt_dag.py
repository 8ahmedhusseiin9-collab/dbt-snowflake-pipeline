from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime, timedelta
import pendulum

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': pendulum.datetime(2026, 10, 1, tz='Africa/Cairo'),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

DBT_DIR = '/opt/airflow/dbt_project'
DBT = '/home/airflow/dbt_venv/bin/dbt'
PROFILES = '/home/airflow/.dbt'

with DAG(
    dag_id='dbt_snowflake_workflow',
    default_args=default_args,
    description='Run dbt models and tests on Snowflake',
    schedule='0 9 * * *',
    catchup=False,
) as dag:

    dbt_run = BashOperator(
        task_id='dbt_run',
        bash_command=f'cd {DBT_DIR} && {DBT} run --no-partial-parse --target-path /tmp/dbt_target --profiles-dir {PROFILES}',
    )

    dbt_test = BashOperator(
        task_id='dbt_test',
        bash_command=f'cd {DBT_DIR} && {DBT} test --no-partial-parse --target-path /tmp/dbt_target --profiles-dir {PROFILES}',
        
    )

    dbt_run >> dbt_test