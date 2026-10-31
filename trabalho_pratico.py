import pandas as pd
import numpy as np

caminho_csv = 'conjunto_de_dados_trabalho_pratico_contextualizacao_atividade_pico_web.csv'

# Passos 1 a 4: Leitura do CSV
df_original = pd.read_csv(
    caminho_csv,
    sep=';',
    engine='python',
    encoding='utf-8'
)

# Passo 5: Verificação inicial
print('=== PASSO 5a: Informações Gerais ===')
df_original.info()
print('\n=== PASSO 5b: Primeiras e últimas 5 linhas ===')
print(df_original.head(5))
print(df_original.tail(5))

# Passo 6: Cópia do DataFrame
df_copia = df_original.copy()

# Passo 7: Tratamento de nulos em 'Calories'
df_copia['Calories'] = df_copia['Calories'].fillna(0)

# Passo 8: Substituição em 'Date' e tentativa de to_datetime
df_copia['Date'] = df_copia['Date'].fillna('1900/01/01')
try:
    df_copia['Date'] = pd.to_datetime(df_copia['Date'])
except ValueError as e:
    print(f'\nErro esperado (Passo 9): {e}')

# Passo 9: Substituição de '1900/01/01' por NaN
df_copia['Date'] = df_copia['Date'].replace('1900/01/01', np.nan)
try:
    df_copia['Date'] = pd.to_datetime(df_copia['Date'])
except ValueError as e:
    print(f'Erro esperado (Passo 10): {e}')

# Passo 10 e 11: Correção de '20201226' e conversão total
df_copia['Date'] = df_copia['Date'].replace('20201226', pd.to_datetime('20201226', format='%Y%m%d'))
df_copia['Date'] = pd.to_datetime(df_copia['Date'])

# Passo 12: Remoção de nulos (linha 22)
df_copia = df_copia.dropna(subset=['Date'])

# Passo 13: Verificação final
print('\n=== PASSO 13: DataFrame Final Tratado (31 Registros) ===')
print(df_copia.to_string())
df_copia.info()
