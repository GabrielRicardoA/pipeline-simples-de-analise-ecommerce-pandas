# %%

import pandas as pd

#importar dataset

def extract_dataset(caminho_df):
    df = pd.read_csv(f"../data/raw/{caminho_df}")
    return df

#%%
#clientes
df_clientes = extract_dataset("olist_customers_dataset.csv")


# %%
#localizacao

df_localizacao = extract_dataset("olist_geolocation_dataset.csv")

# %%
#itens do pedido

df_itens_do_pedido = extract_dataset("olist_order_items_dataset.csv")

# %%
#lista de pagamentos

df_lista_de_pagamentos =extract_dataset("olist_order_payments_dataset.csv")

# %%
#avaliacao do pedido

df_avaliacao_do_pedido = extract_dataset("olist_order_reviews_dataset.csv")

#%%
#Pedidos

df_pedidos = extract_dataset("olist_orders_dataset.csv")

# %%
#lista de produtos

df_produtos = extract_dataset("olist_products_dataset.csv")

#%%
#vendedores

df_vendedores = extract_dataset("olist_sellers_dataset.csv")

#%%
#Categoria do produto

df_categoria_do_produto = extract_dataset("product_category_name_translation.csv")
# %%
