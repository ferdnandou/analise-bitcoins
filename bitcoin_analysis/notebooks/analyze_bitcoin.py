import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
file_path = 'data/bitcoin_data.csv'
df = pd.read_csv(file_path)

# Diagnóstico Inicial
print("Primeiras linhas do DataFrame:")
print(df.head())

print("\nInformações sobre os dados:")
print(df.info())

print("\nDescrição estatística dos dados:")
print(df.describe())

# Converter a coluna de datas
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Gráfico de preço de fechamento
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Close'], label='Preço de Fechamento', color='blue')
plt.xlabel('Data')
plt.ylabel('Preço de Fechamento em USD')
plt.title('Variação do Preço de Fechamento do Bitcoin')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('reports/bitcoin_closing_price.png')
plt.show()

# Gráfico de volume de negociação
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Volume'], label='Volume de Negociação', color='orange')
plt.xlabel('Data')
plt.ylabel('Volume de Negociação')
plt.title('Volume de Negociação do Bitcoin ao Longo do Tempo')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('reports/bitcoin_volume.png')
plt.show()
