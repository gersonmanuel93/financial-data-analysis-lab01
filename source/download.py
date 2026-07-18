import yfinance as yf

ATIVOS = ["HPE", "MRNA", "PCG"]

DATA_INICIO = "2019-01-01"
DATA_FIM = "2019-12-31"


def baixar_dados():
    dados = {}

    for ativo in ATIVOS:
        print(f"Baixando dados de {ativo}...")

        dados[ativo] = yf.download(
            ativo,
            start=DATA_INICIO,
            end=DATA_FIM,
            auto_adjust=True,
            progress=False
        )

    return dados