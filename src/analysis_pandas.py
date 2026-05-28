# %%
import pandas as pd
import matplotlib.pyplot as plt
from transform import (df_clientes,df_pedidos,df_vendedores,
                     df_produtos,df_avaliacao_do_pedido,
                     df_localizacao,df_itens_do_pedido,
                     df_categoria_do_produto,df_lista_de_pagamentos)
# %%
#df lista de pagamentos

#Faturamento total
def faturamento(df):
    faturamento_total = df["valor_do_pagamento"].sum()
    return faturamento_total
# %%
#Numero total de pedidos
def numero_pedidos(df):   
    numero_de_pedidos = df["ID_do_pedido"].nunique()
    return numero_de_pedidos

# %%
def valor_ticket_medio(df):
    ticket_medio = faturamento(df)/numero_pedidos(df)
    return ticket_medio

# %%

def quantidade_de_produtos_vendidos(df):
    quantidadade_produtos_vendidos = df.shape[0]
    return quantidadade_produtos_vendidos 


#%%

#df de clientes

#clientes que mais realizam pedidos
def distribuicao_pedidos_por_cliente(df):
    clientes_mais_pedidos = df.groupby("ID_do_cliente")["ID_do_pedido"].nunique().value_counts(ascending=False)
    return clientes_mais_pedidos
#Todos os clientes realizaram somente um pedido
#O dataset apresenta praticamente ausência de clientes recorrentes, indicando que a maioria realizou apenas um pedido.

# %%
#Estados com mais clientes
def estados_mais_clientes(df):
    estados_mais_cliente = df.groupby("estado_do_cliente")["ID_do_cliente"].count().sort_values(ascending=False)
    return estados_mais_cliente

def grafico_estados_mais_clientes(df):
    estados = estados_mais_clientes(df).head(10)

    plt.figure(figsize=(10,5))
    estados.plot(kind="bar")

    plt.title("Top 10 Estados com Mais Clientes")
    plt.xlabel("Estado")
    plt.ylabel("Quantidade de clientes")
    plt.tight_layout()
    plt.savefig("../outputs/graficos/grafico_estados_mais_clientes.png")
    plt.show()

#%%
#df produtos
#as que possuem sao df_itens_do_pedido
def merge_pedidos_categorias(df,df2):
    df_pedidos_e_categorias = df.merge(df2,how="left",on=["ID_do_produto"])
    return df_pedidos_e_categorias

#df = df_itens_do_pedido
#df2 = df_produtos

#%%
def categorias_mais_vendida(df,df2):
    df_pedidos_e_categorias = merge_pedidos_categorias(df,df2)
    categorias_mais_vendidas = df_pedidos_e_categorias["categoria_do_produto"].value_counts(ascending=False)
    return categorias_mais_vendidas


def grafico_categorias_mais_vendida(df, df2):

    categorias = categorias_mais_vendida(df, df2).head(10)

    plt.figure(figsize=(10,5))

    categorias.plot(kind="barh")

    plt.title("Top 10 Categorias mais vendidas")
    plt.xlabel("Quantidade de vendas")
    plt.ylabel("Categoria")
    plt.tight_layout()
    plt.savefig("../outputs/graficos/grafico_categorias_mais_vendida.png")
    plt.show()

# %%
def categorias_mais_fatura(df,df2):
    df_pedidos_e_categorias = merge_pedidos_categorias(df,df2)
    categorias_mais_faturam = df_pedidos_e_categorias.groupby("categoria_do_produto")["preco"].sum().sort_values(ascending=False)
    return categorias_mais_faturam


def grafico_categorias_mais_fatura(df, df2):

    categorias = categorias_mais_fatura(df, df2).head(10)
    plt.figure(figsize=(10,5))
    categorias.plot(kind="barh")
    plt.title("Top 10 Categorias por Faturamento")
    plt.xlabel("Faturamento")
    plt.ylabel("Categoria")
    plt.tight_layout()
    plt.savefig("../outputs/graficos/grafico_categorias_mais_fatura.png")
    plt.show()

# %%
#Produtos mais vendidos 

def produtos_mais_vendidos(df,df2):
    df_pedidos_e_categorias = merge_pedidos_categorias(df,df2)
    produtos_mais_vendidos = df_pedidos_e_categorias["ID_do_produto"].value_counts()
    return produtos_mais_vendidos

def grafico_produtos_mais_vendidos(df, df2):
    produtos = produtos_mais_vendidos(df, df2).head(10)

    plt.figure(figsize=(10,5))
    produtos.plot(kind="barh")

    plt.title("Top 10 Produtos mais Vendidos")
    plt.xlabel("Quantidade de vendas")
    plt.ylabel("ID do produto")
    plt.tight_layout()
    plt.savefig("../outputs/graficos/grafico_produtos_mais_vendidos.png")
    plt.show()


# %%

#produtos que mais geram receita
def produtos_mais_geram_receita(df,df2):
    df_pedidos_e_categorias = merge_pedidos_categorias(df,df2)
    produtos_mais_geram_receita_ = df_pedidos_e_categorias.groupby("ID_do_produto").agg({"preco":"sum"}).sort_values(by="preco",ascending=False)
    return produtos_mais_geram_receita_

def grafico_produtos_mais_geram_receita(df, df2):
    produtos = produtos_mais_geram_receita(df, df2).head(10)

    plt.figure(figsize=(10,5))
    produtos.plot(kind="barh")

    plt.title("Top 10 Produtos por Receita")
    plt.xlabel("Receita")
    plt.ylabel("ID do produto")
    plt.tight_layout()
    plt.savefig("../outputs/graficos/grafico_produtos_mais_geram_receita.png")
    plt.show()

# %%
#df itens_do_pedido 

#vendedores com mais vendas no sentidos de pedidos

def vendedores_mais_vendem(df):
    vendedores_mais_vendas = (df.groupby("ID_do_vendedor")["ID_do_pedido"].nunique().sort_values(ascending=False))
    return vendedores_mais_vendas

def grafico_vendedores_mais_vendem(df):
    vendedores = vendedores_mais_vendem(df).head(10)

    plt.figure(figsize=(10,5))
    vendedores.plot(kind="barh")

    plt.title("Top 10 Vendedores por Número de Pedidos")
    plt.xlabel("Quantidade de pedidos")
    plt.ylabel("ID do vendedor")
    plt.tight_layout()
    plt.savefig("../outputs/graficos/grafico_vendedores_mais_vendem.png")
    plt.show()


# %%
#vendedores com maior faturamento
def vendedores_faturamento_maior(df):
    vendendores_maior_faturamento = df.groupby("ID_do_vendedor").agg({"preco":"sum"}).sort_values(by="preco",ascending=False)
    return vendendores_maior_faturamento

def grafico_vendedores_faturamento_maior(df):

    vendedores = vendedores_faturamento_maior(df).head(10)

    plt.figure(figsize=(10,5))

    vendedores.plot(kind="barh")

    plt.title("Top 10 Vendedores por Faturamento")
    plt.xlabel("Faturamento")
    plt.ylabel("ID do vendedor")
    plt.tight_layout()
    plt.savefig("../outputs/graficos/grafico_vendedores_faturamento_maior.png")
    plt.show()
# %%

#estado com mais vendores
def estados_com_mais_vendedores_(df):
    estados_com_mais_vendedores = (df["estado_do_vendedor"].value_counts().sort_values(ascending=False))
    return estados_com_mais_vendedores

def grafico_estados_com_mais_vendedores(df):
    estados = estados_com_mais_vendedores_(df).head(10)

    plt.figure(figsize=(10,5))
    estados.plot(kind="bar")

    plt.title("Top 10 Estados com Mais Vendedores")
    plt.xlabel("Estado")
    plt.ylabel("Quantidade de vendedores")
    plt.tight_layout()
    plt.savefig("../outputs/graficos/grafico_estados_com_mais_vendedores.png")
    plt.show()

#%%
#KPIS mais fortes

def merge_itens_do_pedido_e_vendedores(df,df2):
    df_itens_e_vendedores = df.merge(df2,how="left",on="ID_do_vendedor")
    return df_itens_e_vendedores

#top 10 cidades com mais faturamento
def cidades_maior_faturamento_(df,df2):
    df_itens_e_vendedores = merge_itens_do_pedido_e_vendedores(df,df2)
    cidades_maior_faturamento = df_itens_e_vendedores.groupby("cidade_do_vendedor").agg({"preco":"sum"}).sort_values(by="preco",ascending=False).head(10)
    return cidades_maior_faturamento

def grafico_cidades_maior_faturamento(df, df2):

    cidades = cidades_maior_faturamento_(df, df2)

    plt.figure(figsize=(10,5))

    plt.barh(
        cidades.index,
        cidades["preco"]
    )

    plt.title("Top 10 Cidades por Faturamento")
    plt.xlabel("Faturamento")
    plt.ylabel("Cidade")
    plt.tight_layout()
    plt.savefig("../outputs/graficos/grafico_cidades_maior_faturamento.png")
    plt.show()

# %%
#ticket medio por estado

def ticket_medio(df,df2):
    df_itens_e_vendedores = merge_itens_do_pedido_e_vendedores(df,df2)
    df_ticket_medio = df_itens_e_vendedores.groupby("estado_do_vendedor").agg({"preco":"sum"})
    #preco = faturamento total de cada estado

    vendas_por_estado_series = df_itens_e_vendedores.groupby("estado_do_vendedor")["ID_do_pedido"].nunique()
    vendas_por_estado_series
    #numero de vendas por estado
    df_ticket_medio["vendas_por_estado"] = vendas_por_estado_series
    df_ticket_medio = df_ticket_medio.reset_index()
    df_ticket_medio["ticket_medio_por_estado"] = df_ticket_medio["preco"] / df_ticket_medio["vendas_por_estado"]
    df_ticket_medio = df_ticket_medio.sort_values(by="ticket_medio_por_estado",ascending=False)
    return df_ticket_medio

def grafico_ticket_medio(df, df2):

    ticket = ticket_medio(df, df2).head(10)

    plt.figure(figsize=(10,5))

    plt.barh(
        ticket["estado_do_vendedor"],
        ticket["ticket_medio_por_estado"]
    )

    plt.title("Ticket Médio por Estado")
    plt.xlabel("Ticket Médio")
    plt.ylabel("Estado")
    plt.tight_layout()
    plt.savefig("../outputs/graficos/grafico_ticket_medio.png")
    plt.show()

# %%

