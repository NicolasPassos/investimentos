from selenium import webdriver

navegador = webdriver.Chrome()

#Abrindo site
siteBanco = navegador.get('https://www.bcb.gov.br/controleinflacao/historicotaxasjuros')

#Se o botão de cookies aparecer, clicar em aceitar
try:
    navegador.find_element('xpath','/html/body/app-root/bcb-cookies/div/div/div/div/button[2]').click()
except:
    pass

#Pegando a ultima taxa de juros
taxaJuros = navegador.find_element('xpath','//*[@id="historicotaxasjuros"]/tbody/tr[1]/td[5]').text
taxaSelic = float(taxaJuros.replace(',','.')) - 0.10
taxaSelic = str(taxaSelic).replace('.',',')
print(f'A última taxa de juros registrada foi {taxaJuros} e taxa Selic {taxaSelic}')