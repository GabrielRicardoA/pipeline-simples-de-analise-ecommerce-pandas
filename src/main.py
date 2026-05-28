# %%
import pandas as pd
import matplotlib.pyplot as plt
from load import (
    criar_pastas,
    salvar_csv,
    salvar_tabela
)

from transform import (
    df_clientes, df_pedidos, df_vendedores,
    df_produtos, df_itens_do_pedido,
    df_lista_de_pagamentos
)

from analysis_pandas import (
    faturamento, numero_pedidos, valor_ticket_medio,categorias_mais_fatura,
    quantidade_de_produtos_vendidos,produtos_mais_geram_receita,
    grafico_categorias_mais_vendida,vendedores_faturamento_maior,
    grafico_categorias_mais_fatura,ticket_medio,cidades_maior_faturamento_,
    grafico_produtos_mais_vendidos,
    grafico_produtos_mais_geram_receita,
    grafico_vendedores_mais_vendem,
    grafico_vendedores_faturamento_maior,
    grafico_estados_mais_clientes,
    grafico_estados_com_mais_vendedores,
    grafico_cidades_maior_faturamento,
    grafico_ticket_medio
)
#%%
criar_pastas()
#%%
#salvar os csvs

salvar_csv(df_clientes,"../data/processed/clientes_processed.csv")
salvar_csv(df_itens_do_pedido,"../data/processed/itens_do_pedido_processed.csv")
salvar_csv(df_lista_de_pagamentos,"../data/processed/df_lista_de_pagamentos_processed.csv")
salvar_csv(df_pedidos,"../data/processed/df_pedidos_processed.csv")
salvar_csv(df_produtos,"../data/processed/df_produtos_processed.csv")
salvar_csv(df_vendedores,"../data/processed/df_vendedores_processed.csv")
#%%
#salvar tabelas
salvar_tabela(
    categorias_mais_fatura(
        df_itens_do_pedido,
        df_produtos
    ),

    "../outputs/tabelas/categorias_mais_faturam.csv"
)

salvar_tabela(
    produtos_mais_geram_receita(
        df_itens_do_pedido,
        df_produtos
    ),

    "../outputs/tabelas/produtos_mais_geram_receita.csv"
)

salvar_tabela(
    vendedores_faturamento_maior(
        df_itens_do_pedido
    ),

    "../outputs/tabelas/vendedores_maior_faturamento.csv"
)

salvar_tabela(
    ticket_medio(
        df_itens_do_pedido,
        df_vendedores
    ),

    "../outputs/tabelas/ticket_medio_por_estado.csv"
)

salvar_tabela(
    cidades_maior_faturamento_(
        df_itens_do_pedido,
        df_vendedores
    ),

    "../outputs/tabelas/cidades_maior_faturamento.csv"
)
# %%
print("===== KPIs GERAIS =====")
print(f"Faturamento total: R$ {faturamento(df_lista_de_pagamentos):,.2f}")
print(f"Número total de pedidos: {numero_pedidos(df_lista_de_pagamentos)}")
print(f"Ticket médio: R$ {valor_ticket_medio(df_lista_de_pagamentos):,.2f}")
print(f"Produtos vendidos: {quantidade_de_produtos_vendidos(df_itens_do_pedido)}")

# %%
grafico_categorias_mais_vendida(df_itens_do_pedido, df_produtos)

# %%
grafico_categorias_mais_fatura(df_itens_do_pedido, df_produtos)

# %%
grafico_produtos_mais_vendidos(df_itens_do_pedido, df_produtos)

# %%
grafico_produtos_mais_geram_receita(df_itens_do_pedido, df_produtos)

# %%
grafico_vendedores_mais_vendem(df_itens_do_pedido)

# %%
grafico_vendedores_faturamento_maior(df_itens_do_pedido)

# %%
grafico_estados_mais_clientes(df_clientes)

# %%
grafico_estados_com_mais_vendedores(df_vendedores)

# %%
grafico_cidades_maior_faturamento(df_itens_do_pedido, df_vendedores)

# %%
grafico_ticket_medio(df_itens_do_pedido, df_vendedores)