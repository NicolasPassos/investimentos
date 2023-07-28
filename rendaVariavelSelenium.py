from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")

navegador = webdriver.Chrome(options=options)

#Lista de ativos e seus tipos que eu desejo pesquisar
ativos = [{"tipo":"acoes","ticker":"PETR4"},
          {"tipo":"acoes","ticker":"MYPK3"},
          {"tipo":"fundos-imobiliarios","ticker":"MXRF11"}]

resultadoAtivos = []

for ativo in ativos:
    navegador.get(f"https://statusinvest.com.br/{ativo['tipo']}/{ativo['ticker']}")

    #Caso apareça algum popup, clicar no botão de fechar
    try:
        navegador.find_element("xpath","/html/body/div[13]/div/div/div[1]/button/i").click()
        navegador.find_element("xpath","/html/body/div[15]/div/div/div[1]/button/i").click()
        navegador.find_element("xpath","/html/body/div[17]/div/div/div[1]/button/i").click()
    except:
        pass
    
    if ativo['tipo'] == 'acoes':
        moeda = navegador.find_element('xpath','//*[@id="main-2"]/div[2]/div/div[1]/div/div[1]/div/div[1]/span').text
        valorAtual = navegador.find_element('xpath','//*[@id="main-2"]/div[2]/div/div[1]/div/div[1]/div/div[1]/strong').text
        variacaoValorAtivo = navegador.find_element('xpath','//*[@id="main-2"]/div[2]/div/div[1]/div/div[1]/div/div[2]/span/b').text

        resultadoAtivos.append(f'A cotação do ativo {ativo["ticker"]} está com o valor de {moeda}{valorAtual} com variação do valor de {variacaoValorAtivo}.')

    if ativo['tipo'] == 'fundos-imobiliarios':
        moeda = navegador.find_element('xpath','//*[@id="main-2"]/div[2]/div[1]/div[1]/div/div[1]/span').text
        valorAtual = navegador.find_element('xpath','//*[@id="main-2"]/div[2]/div[1]/div[1]/div/div[1]/strong').text
        variacaoValorAtivo = navegador.find_element('xpath','//*[@id="main-2"]/div[2]/div[1]/div[1]/div/div[2]/span/b').text
        rendimento = navegador.find_element('xpath','//*[@id="dy-info"]/div/div[1]/strong').text
        dataPagRendimento = navegador.find_element('xpath','//*[@id="dy-info"]/div/div[2]/div[2]/div[2]/div/b').text

        resultadoAtivos.append(f'A cotação do ativo {ativo["ticker"]} está com o valor de {moeda}{valorAtual} com variação do valor de {variacaoValorAtivo}. O último rendimento deste ativo foi pago no dia {dataPagRendimento} no valor de {rendimento}.')

for resultado in resultadoAtivos:
    print(resultado)