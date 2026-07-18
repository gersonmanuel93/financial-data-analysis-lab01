from extract import*
from analise import*

# Sem uso de recurso da função:
"""Encontrando a maior variância"""
variancias = retornos.var()

print(variancias)

acao_maior_var = variancias.idxmax()

print(acao_maior_var)

"""Densidade empírica"""
serie = retornos[acao_maior_var]

densidade = gaussian_kde(serie)

x = np.linspace(
    serie.min(),
    serie.max(),
    300
)

plt.figure(figsize=(10,6))

plt.plot(
    x,
    densidade(x),
    linewidth=3
)

plt.fill_between(
    x,
    densidade(x),
    alpha=0.4
)

plt.title(f"Densidade Empírica - {acao_maior_var}")

plt.xlabel("Retorno Diário")

plt.ylabel("Densidade")

plt.show()

"""
Explicação:
A densidade empírica permite visualizar como os retornos se distribuem.
Quanto maior o pico, maior a concentração de observações naquele intervalo.
"""

"""Matriz de covariância"""
cov = retornos.cov()

cov

"""Encontrando a menor covariância"""
cov2 = cov.copy()

np.fill_diagonal(cov2.values, np.nan)

cov2

menor = cov2.stack().idxmin()

print(menor)

"""Média das rentabilidades"""
media = retornos.mean()

print(media)

"""Encontrando a ação com maior média"""
melhor_acao = media.idxmax()

print(melhor_acao)

"""Estatísticas finais"""
estatisticas = pd.DataFrame({
    "Média": retornos.mean(),
    "Variância": retornos.var(),
    "Desvio Padrão": retornos.std()
})

estatisticas

"""print("Ação com maior retorno médio:", melhor_acao)

print("Ação com maior variância:", acao_maior_var)

print("Par com menor covariância:", menor)"""

# Usando função:
def estatisticas(retornos):

    print("\n========== MÉDIAS ==========\n")
    print(retornos.mean())

    print("\n========== VARIÂNCIAS ==========\n")
    print(retornos.var())

    print("\n========== DESVIO PADRÃO ==========\n")
    print(retornos.std())

    print("\n========== COVARIÂNCIA ==========\n")
    print(retornos.cov())