import os 

def criar_pastas():
    os.makedirs("../data/processed", exist_ok=True)
    os.makedirs("../outputs/tabelas", exist_ok=True)
    os.makedirs("../outputs/graficos", exist_ok=True)


def salvar_csv(df, caminho):
    df.to_csv(caminho, index=False)


def salvar_tabela(tabela, caminho):
    tabela.to_csv(caminho)