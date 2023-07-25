import requests
from datetime import datetime
import json

anoAtual = datetime.now().year

consumo = requests.get(f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4189/dados?formato=json&dataInicial=01/01/{anoAtual}&dataFinal=31/12/{anoAtual}')

response = consumo.content
response = json.loads(response)
ultimoItem = len(response) - 1

print(f"A ultima taxa registrada foi na data {response[ultimoItem]['data']} e a taxa é de {response[ultimoItem]['valor']}")