# DAG | Exemplo 3 (mais moderna). Usar decoradores para criar DAGs.

from datetime import datetime

from airflow import DAG, task

from time import sleep


@DAG(
        dag_id="dag_exemplo_03",
        description="DAG de exemplo 03",
        schedule="0 0 * * *",
        start_date=datetime(2024, 4, 19),
        catchup=False
)
def minha_terceira_dag():
    @task
    def primeira_atividade():
        print("Minha primeira atividade.")
        sleep(2)
    
    @task
    def segunda_atividade():
        print("Minha segunda atividade.")
        sleep(2)
    
    @task
    def terceira_atividade():
        print("Minha terceira atividade.")
        sleep(2)
    
    @task
    def quarta_atividade():
        print("Minha quarta atividade.")
        sleep(2)

    t1 = primeira_atividade()
    t2 = segunda_atividade()
    t3 = terceira_atividade()
    t4 = quarta_atividade()

    t1 >> t2 >> t3 >> t4

minha_terceira_dag()

    