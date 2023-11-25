from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

url = "https://www.bing.com/sportsdetails?q=Brasileir%C3%A3o%20%20S%C3%A9rie%20A&sport=Soccer&scenario=League&TimezoneId=Central%20Brazilian%20Standard%20Time&league=Soccer_BrazilBrasileiroSerieA&seasonyear=2023&intent=Standings&segment=sports&isl2=true&"
html = urlopen(url)
bs = BeautifulSoup(html, 'html.parser')

tabela = bs.find('table')
dados = pd.read_html(str(tabela))[0]

# Excluir a primeira coluna
dados = dados.drop(1, axis=1)

# Excluir a segunda linha
dados = dados.drop(0)

# Inverter a ordem das linhas
dados = dados.iloc[::-1]

# Plotar o gráfico de barras
largura_coluna = 0.8 # Ajuste a largura das barras conforme preferir

plt.bar(dados[0], dados[2], width=largura_coluna, label='Pontos')
plt.xlabel('Time')
plt.ylabel('Pontos')
plt.title('Pontuação dos times no Brasileirão 2023')
plt.xticks(rotation=60)
plt.legend()
plt.tight_layout()  # Ajustar o layout para uma melhor exibição
plt.show()

print(dados)
