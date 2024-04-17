# Exemplo 02. Pipeline com logs. 
# Dá para automatizar o fluxo de pipeline e retornar logs sem airflow? Dá...
from loguru import logger

from time import sleep

logger.add("logs/execution_logs.log", format="{time} - {message}", level="INFO", rotation="1 day")

def primeira_atividade():
    logger.info("Primeira atividade iniciada.")
    sleep(2)
    logger.info("Primeira atividade finalizada.")

def segunda_atividade():
    logger.info("Segunda atividade iniciada.")
    sleep(2)
    logger.info("Segunda atividade finalizada.")

def terceira_atividade():
    logger.info("Terceira atividade iniciada.")
    sleep(2)
    logger.info("Terceira atividade finalizada.")

def pipeline():
    primeira_atividade()
    segunda_atividade()
    terceira_atividade()
    logger.info("Pipeline finalizada")

if __name__ == "__main__":
    # Rodar função a cada 10 segundos por tempo indefinido.
    
    while True:
        pipeline()
        sleep(10) 