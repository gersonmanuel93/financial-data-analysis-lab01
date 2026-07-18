from extract import*
from analise import*
from estatisticas import*

"""Gráfico da ação com maior retorno médio"""
plt.figure(figsize=(12,6))

dados[melhor_acao]["Close"].plot()

plt.title(f"Cotação diária - {melhor_acao}")

plt.xlabel("Data")

plt.ylabel("Preço")

plt.show()

"""Insight visualização:
Este gráfico mostra a evolução do preço da ação durante todo o ano de 2019."""


"""Boxplot da ação com maior retorno médio"""
plt.figure(figsize=(8,6))

sns.boxplot(
    y=retornos[melhor_acao]
)

plt.title(f"Boxplot dos retornos diários - {melhor_acao}")

plt.show()

"""
Insight visualização:
O boxplot apresenta:

mediana
quartis
dispersão
outliers
"""

"""Scatter Plot"""
x = menor[0]

y = menor[1]

plt.figure(figsize=(8,6))

plt.scatter(
    retornos[x],
    retornos[y],
    alpha=0.6
)

plt.xlabel(x)

plt.ylabel(y)

plt.title(f"Dispersão entre {x} e {y}")

plt.show()

"""
Explicação:
Este gráfico mostra a relação entre os retornos das duas ações.
Caso exista correlação positiva, os pontos tenderão a formar uma reta crescente.
"""
