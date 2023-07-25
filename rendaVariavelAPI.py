import requests
import json

ativos = ["PETR4",
          "MYPK3",
          "MXRF11"]

for ativo in ativos:
    #Consumindo a API de acordo com os ativos da lista
    consumo = requests.get(f'https://brapi.dev/api/quote/{ativo}')
    #Convertendo retorno como json
    response = json.loads(consumo.content)['results'][0]

    #Definindo variáveis
    moeda = response['currency']
    nomeAtivo = response['shortName']
    ticker = response['symbol']
    valorAtivo = response['regularMarketPrice']
    varicaoAtivo = response['regularMarketChangePercent']

    print(f'O ativo {ticker} - {nomeAtivo} está com o valor de {valorAtivo} ({moeda}), com variação de {varicaoAtivo}%.')