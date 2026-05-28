# %%
import pandas as pd
from extract import (df_clientes,df_pedidos,df_vendedores,
                     df_produtos,df_avaliacao_do_pedido,
                     df_localizacao,df_itens_do_pedido,
                     df_categoria_do_produto,df_lista_de_pagamentos)

#%%
df_clientes.columns = [
    "ID_do_cliente",
    "ID_unico_do_cliente",
    "prefixo_do_cep",
    "cidade_do_cliente",
    "estado_do_cliente"
]
df_clientes.head()
# %%
df_pedidos.columns = [
    "ID_do_pedido",
    "ID_do_cliente",
    "status_do_pedido",
    "data_da_compra",
    "data_de_aprovacao",
    "data_de_envio_transportadora",
    "data_de_entrega_cliente",
    "data_estimada_de_entrega"
]
df_pedidos.head()

# %%
df_vendedores.columns = [
    "ID_do_vendedor",
    "prefixo_do_cep_vendedor",
    "cidade_do_vendedor",
    "estado_do_vendedor"
]
df_vendedores.head()
# %%
df_produtos.columns = [
    "ID_do_produto",
    "categoria_do_produto",
    "tamanho_nome_do_produto",
    "tamanho_descricao_do_produto",
    "quantidade_de_fotos",
    "peso_em_gramas",
    "comprimento_cm",
    "altura_cm",
    "largura_cm"
]
df_produtos.head()
# %%
df_avaliacao_do_pedido.columns = [
    "ID_da_review",
    "ID_do_pedido",
    "nota_da_review",
    "titulo_do_comentario",
    "mensagem_do_comentario",
    "data_de_criacao_review",
    "data_de_resposta_review"
]
df_avaliacao_do_pedido
# %%
df_localizacao.columns = [
    "prefixo_do_cep",
    "latitude",
    "longitude",
    "cidade",
    "estado"
]
df_localizacao.head()
# %%
df_itens_do_pedido.columns = [
    "ID_do_pedido",
    "ID_do_item_do_pedido",
    "ID_do_produto",
    "ID_do_vendedor",
    "data_limite_de_envio",
    "preco",
    "valor_do_frete"
]
df_itens_do_pedido.head()
# %%
df_categoria_do_produto.columns = [
    "categoria_do_produto",
    "categoria_do_produto_ingles"
]
df_categoria_do_produto.head()
# %%


df_lista_de_pagamentos.columns = [
    "ID_do_pedido",
    "sequencia_do_pagamento",
    "tipo_de_pagamento",
    "quantidade_de_parcelas",
    "valor_do_pagamento"
]
df_lista_de_pagamentos.head()
# %%