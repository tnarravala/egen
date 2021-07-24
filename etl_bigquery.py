import os

from airflow import models
from airflow.providers.google.cloud.operators.bigquery import (
    BigQueryCreateEmptyDatasetOperator,
    BigQueryDeleteDatasetOperator,
)
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.utils.dates import days_ago

DATASET_NAME = os.environ.get("GCP_DATASET_NAME", 'airflow_test')
TABLE_NAME = os.environ.get("GCP_TABLE_NAME", 'gcs_to_bq_table')

dag = models.DAG(
    dag_id='example_gcs_to_bigquery_operator',
    start_date=days_ago(2),
    schedule_interval=None,
    tags=['example'],
)

create_test_dataset = BigQueryCreateEmptyDatasetOperator(
    task_id='create_airflow_test_dataset', dataset_id=DATASET_NAME, dag=dag
)

# [START howto_operator_gcs_to_bigquery]
load_csv = GCSToBigQueryOperator(
    task_id='gcs_to_bigquery',
    bucket='msft-data-bucket',
    source_objects=['msft.csv'],
    destination_project_dataset_table=f"{DATASET_NAME}.{TABLE_NAME}",
    schema_fields=[
        {'name': 'open', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'high', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'low', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'close', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'volume', 'type': 'STRING', 'mode': 'NULLABLE'},
    ],
    write_disposition='WRITE_TRUNCATE',
    dag=dag,
)


create_test_dataset >> load_csv