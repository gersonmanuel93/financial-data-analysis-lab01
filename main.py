from source import*
from source import (
    baixar_dados,
    calcular_retornos
)
from source import (
    grafico_preco,
    boxplot,
    densidade,
    scatter
)

dados = baixar_dados()

retornos = calcular_retornos(dados)


"""while True:

    print("\n==============================")
    print(" LABORATÓRIO 1")
    print("==============================")
    print("1 - Mostrar Dados")
    print("2 - Estatísticas")
    print("3 - Gráfico de Preço")
    print("4 - Boxplot")
    print("5 - Densidade")
    print("6 - Scatter")
    print("0 - Sair")
    
    op = input("\nEscolha: ")"""

while True:

    print("="*50)
    print("LABORATÓRIO 01")
    print("="*50)

    print("1 - Download dos dados")
    print("2 - Estatísticas")
    print("3 - Gráfico")
    print("4 - Boxplot")
    print("5 - Densidade")
    print("6 - Scatter")
    print("0 - Sair")

    op = input("Escolha: ")