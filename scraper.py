from bs4 import BeautifulSoup
import requests

url = 'https://www.pichau.com.br/hardware/placa-de-video'

headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
placas = soup.find_all('div', class_='MuiCardContent-root jss53')
ultima_pagina = soup.find('button', 'MuiButtonBase-root MuiPaginationItem-root MuiPaginationItem-page MuiPaginationItem-textPrimary MuiPaginationItem-sizeLarge')


for i in range(1, 47):
    url_pagina = f'https://www.pichau.com.br/hardware/placa-de-video?page={i}'
    site = requests.get(url_pagina, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    placas = soup.find_all('div', class_='MuiCardContent-root jss53')
    
    with open('precos_placas.csv', 'a', newline='',encoding='UTF-8' ) as f:
        for placa in placas:
            
            marca = placa.find('h2', class_='MuiTypography-root jss61 jss62 MuiTypography-h6').get_text()
            try:
                preco = placa.find('div', class_='jss64').get_text().strip()
                num_preco = preco[2:]
            except:
                num_preco = '0'
            try:
                preco_cartao = placa.find('div', class_='jss72').get_text().strip()
                num_preco_cartao = preco_cartao[3:]
            except:
                num_preco_cartao = '0'
                
            linha = marca + ';' + num_preco + ';' + num_preco_cartao + '\n'
            print(linha)
            f.write(linha)

    print(url_pagina)