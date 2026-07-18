from extract import*
import pandas as pd

"""Calculando a rentabilidade diária

A rentabilidade diária será calculada por:
Rt = Pt - Pt-1 / Pt-1
No Pandas isso corresponde ao método pct_change().
"""
# Sem uso da função;
retornos = pd.DataFrame()

for ativo in ativos:
    retornos[ativo] = dados[ativo]["Close"].pct_change()

retornos = retornos.dropna()

retornos.head()

"""Média das rentabilidades"""
media = retornos.mean()

print(media)

"""Encontrando a ação com maior média"""
melhor_acao = media.idxmax()

print(melhor_acao)

# Usando função:
def calcular_retornos(dados):

    retornos = pd.DataFrame()

    for ativo in dados.keys():

        retornos[ativo] = dados[ativo]["Close"].pct_change()

    retornos.dropna(inplace=True)

    return retornos