import pandas as pd

# Caminho do arquivo CSV limpo
caminho_csv = 'conjunto_de_dados_trabalho_pratico_contextualizacao_atividade_pico_web.csv'

# ==============================================================================
# MICROATIVIDADE 1: Ler um arquivo CSV usando a biblioteca Pandas
# ==============================================================================
df_original = pd.read_csv(
    caminho_csv,
    sep=';',
    engine='python',
    encoding='utf-8'
)

print('=== MICROATIVIDADE 1: Conjunto de Dados Original ===')
print(df_original)

# ==============================================================================
# MICROATIVIDADE 2: Criar um subconjunto de dados (3 colunas)
# ==============================================================================
df_subconjunto = df_original[['ID', 'Date', 'Calories']]

print('\n=== MICROATIVIDADE 2: Subconjunto de Dados (3 Colunas) ===')
print(df_subconjunto)

# ==============================================================================
# MICROATIVIDADE 3: Configurar max_rows para 9999 e exibir com to_string()
# ==============================================================================
pd.options.display.max_rows = 9999

print('\n=== MICROATIVIDADE 3: Exibição Completa com to_string() ===')
print(df_original.to_string())

# ==============================================================================
# MICROATIVIDADE 4: Exibir as primeiras e últimas 10 linhas
# ==============================================================================
print('\n=== MICROATIVIDADE 4: Primeiras 10 Linhas ===')
print(df_original.head(10))

print('\n=== MICROATIVIDADE 4: Últimas 10 Linhas ===')
print(df_original.tail(10))

# ==============================================================================
# MICROATIVIDADE 5: Exibir informações gerais sobre colunas, linhas e dados
# ==============================================================================
print('\n=== MICROATIVIDADE 5: Informações Gerais do Conjunto de Dados ===')
df_original.info()
