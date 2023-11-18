from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = "https://www.bing.com/sportsdetails?q=Brasileir%C3%A3o%20%20S%C3%A9rie%20A&sport=Soccer&scenario=League&TimezoneId=Central%20Brazilian%20Standard%20Time&league=Soccer_BrazilBrasileiroSerieA&seasonyear=2023&intent=Standings&segment=sports&isl2=true&"
html = urlopen(url)
bs = BeautifulSoup(html, 'html.parser')

tabela = bs.find('table')

dados = pd.read_html(str(tabela))[0]

plt.bar(dados['Team'], dados['Pts'])
plt.xlabel('Time')
plt.ylabel('Pontos')
plt.title('Pontuação dos times no Brasileirão 2023')
plt.xticks(rotation=45)  # Rotacionar os rótulos do eixo x para melhorar a legibilidade
plt.show()

print(dados)
