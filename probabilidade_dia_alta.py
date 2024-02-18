import pandas as pd
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

start_date = '2003-10-01'
# symbol = '^GDAXI'
symbol = '^BVSP'

#baixa dados yf
df = yf.download(symbol, start = start_date)
#remove colunas que nao vou usar
df = df.drop(columns = ['Adj Close', 'Volume'])
#define dias de alta e baixa em coluna usando np.where(condição, valor verdadeiro, valor falso)
df['Sentido_Dia'] = np.where(df['Close'] > df['Open'], 'alta','baixa')

#conta duas altas consecutivas com np.where criando nova coluna 'duas_altas'
df['Dia_Seguinte'] = df['Sentido_Dia'].shift(-1)

# Inicialize um DataFrame vazio para armazenar os resultados
probabilidades = pd.DataFrame(columns=['N_Dias_Alta', 'Probabilidade_Alta_Seguinte'])
# Loop para calcular as probabilidades para cada número de dias de alta consecutivos
for n in range(1, 11):  # Supondo até 10 dias consecutivos de alta
    altas_seguidas = (df['Sentido_Dia'] == 'alta').rolling(n).sum()
    probabilidade = (altas_seguidas.shift(-n) == n).mean()
    probabilidades = probabilidades.append({'N_Dias_Alta': n, 'Probabilidade_Alta_Seguinte': probabilidade}, ignore_index=True)

probabilidades



