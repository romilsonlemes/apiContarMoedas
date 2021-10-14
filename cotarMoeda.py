import requests
import json

cotacoes = requests.get('https://economia.awesomeapi.com.br/json/all')
cotacoes_dic = cotacoes.json()
#print(cotacoes_dic['USD']['code'])
print('Dolar Americano')
print(cotacoes_dic['USD']) # Dolar Americano
print('Dolar Canadense')
print(cotacoes_dic['CAD']) # Dolar Canadense

#print(cotacoes_dic)









