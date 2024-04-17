# Exemplo 01. Pipeline rodando a cada dez segundos. 
# Dá para 'dar o play' automaticamente sem airflow? Dá...

from time import sleep

def primeira_atividade():
    print("Minha primeira atividade.")
    sleep(2)

def segunda_atividade():
    print("Minha segunda atividade.")
    sleep(2)

def terceira_atividade():
    print("Minha terceira atividade.")
    sleep(2)

def pipeline():
    primeira_atividade()
    segunda_atividade()
    terceira_atividade()
    print("Pipeline finalizada")

if __name__ == "__main__":
    # Rodar função a cada 10 segundos por tempo indefinido.
    
    while True:
        pipeline()
        sleep(10) 