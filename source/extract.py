import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from scipy.stats import gaussian_kde

import yfinance as yf
"""from pandas_datareader import data as pdr
yf.pdr_override()"""

plt.style.use("ggplot")


ativos = ["HPE", "MRNA", "PCG"]

inicio = "2019-01-01"
fim = "2019-12-31"

dados = {}

for ativo in ativos:
    dados[ativo] = yf.download(
        ativo,
        start=inicio,
        end=fim,
        progress=False
    )

print(dados["HPE"].head())
print(dados["HPE"].columns)

retornos = pd.DataFrame()

for ativo in ativos:
    retornos[ativo] = dados[ativo]["Close"].pct_change()

retornos = retornos.dropna()