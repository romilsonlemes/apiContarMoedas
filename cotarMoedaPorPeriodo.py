import requests
import json
import matplotlib.pyplot as plt

dataInicial = '20210101'
dataFinal = '20211031'
# moeda = 'USD-BRL'
moeda = 'BTC-BRL'
qtde = 200

cotacoes_btc = requests.get(f'https://economia.awesomeapi.com.br/json/daily/{moeda}/{qtde}?start_date={dataInicial}&end_date={dataFinal}')
cotacoes_btc_dic = cotacoes_btc.json()
lista_cotacoes_btc = [float(item['bid']) for item in cotacoes_btc_dic]
lista_cotacoes_btc.reverse()

print(lista_cotacoes_btc)
print(len(lista_cotacoes_btc))
# print(lista_cotacoes_btc)

# Gerar Gráfico no MatPlotLib

plt.figure(figsize=(15, 5))
plt.plot(lista_cotacoes_btc)
plt.show()






