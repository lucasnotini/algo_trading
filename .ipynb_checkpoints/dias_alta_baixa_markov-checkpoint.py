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

contagem_alta = len(df[df['Sentido_Dia'] == 'alta'])
alta_alta = len( df[(df['Sentido_Dia'] == 'alta') & (df['Sentido_Dia'].shift(-1) == 'alta')])
percent_alta_alta = alta_alta / contagem_alta
alta_alta_alta = len( df[(df['Sentido_Dia'] == 'alta') & (df['Sentido_Dia'].shift(-1) == 'alta') & (df['Sentido_Dia'].shift(-2) == 'alta')  ])
percent_alta_alta_alta = alta_alta_alta / alta_alta

