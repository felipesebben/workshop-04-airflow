# DAG | Exemplo 2. Ao inves de criar um conteto, cria-se uma instancia de DAG.
# Executa-se o método `dag` para criar os operadores.

import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator

minha_dag = DAG(
    dag_id="dag_exemplo_02",
    start_date=datetime.datetime(2024, 4, 19),
    schedule_interval="@daily",
    catchup=False,
)

EmptyOperator(task_id="tarefa_2", dag=minha_dag)