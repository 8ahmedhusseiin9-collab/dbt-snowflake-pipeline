FROM apache/airflow:3.3.2

RUN python -m venv /home/airflow/dbt_venv && \
    /home/airflow/dbt_venv/bin/pip install --no-cache-dir dbt-core dbt-snowflake