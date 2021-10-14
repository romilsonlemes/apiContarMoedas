import requests
import json

cotacoes = requests.get('https://economia.awesomeapi.com.br/json/all')
cotacoes_dic = cotacoes.json()
#print(cotacoes_dic['USD']['code'])
#print('Dolar Americano')
#print(cotacoes_dic['USD'][bid]) # Dolar Americano, Campo BID
print('\nValor da cotação para:\n')
print(f'Dolar Americano: {cotacoes_dic["USD"]["bid"]}')
print(f'Euro...........: {cotacoes_dic["EUR"]["bid"]}')
print(f'BitCoin........: {cotacoes_dic["BTC"]["bid"]}')
#print(cotacoes_dic)









