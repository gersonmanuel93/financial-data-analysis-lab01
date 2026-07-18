import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import gaussian_kde

# Usando função:
"""Gráfico da Acção:"""
def grafico_preco(dados, ativo):

    plt.figure(figsize=(12,6))

    plt.plot(
        dados[ativo]["Close"]
    )

    plt.title(f"Cotação da ação {ativo}")

    plt.xlabel("Data")

    plt.ylabel("Preço")

    plt.show()

"""Box Plot:"""
def boxplot(retornos, ativo):

    plt.figure(figsize=(7,5))

    sns.boxplot(y=retornos[ativo])

    plt.title(f"Boxplot - {ativo}")

    plt.show()

"""Gráfico da Densidade:"""
def densidade(retornos, ativo):

    serie = retornos[ativo]

    kde = gaussian_kde(serie)

    x = np.linspace(
        serie.min(),
        serie.max(),
        300
    )

    plt.figure(figsize=(10,6))

    plt.plot(x, kde(x))

    plt.fill_between(x, kde(x), alpha=0.3)

    plt.title(f"Densidade - {ativo}")

    plt.show()

"""Scatter Plot"""
def scatter(retornos, ativo1, ativo2):

    plt.figure(figsize=(8,6))

    plt.scatter(
        retornos[ativo1],
        retornos[ativo2]
    )

    plt.xlabel(ativo1)

    plt.ylabel(ativo2)

    plt.title(f"{ativo1} x {ativo2}")

    plt.show()