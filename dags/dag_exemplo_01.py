# DAG | Exemplo 1. Como se criavam DAGs antes.
import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="dag_exemplo_01",
    start_date=datetime.datetime(2021, 1, 1),
    schedule="@daily",
    catchup=False,
):
    EmptyOperator(task_id="tarefa_1")

    # Vantagens:
    # A DAG roda automaticamente e o contexto é passado para os operadores.
