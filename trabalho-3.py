from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

url = "https://www.bing.com/sportsdetails?q=Brasileir%C3%A3o%20%20S%C3%A9rie%20A&sport=Soccer&scenario=League&TimezoneId=Central%20Brazilian%20Standard%20Time&league=Soccer_BrazilBrasileiroSerieA&seasonyear=2023&intent=Standings&segment=sports&isl2=true&"
html = urlopen(url)
bs = BeautifulSoup(html, 'html.parser')

tabela = bs.find('table')
dados = pd.read_html(str(tabela))[0]

# Excluir colunas indesejadas
colunas_indesejadas = [1, 7, 8]
dados = dados.drop(columns=colunas_indesejadas)

# Excluir a segunda linha
dados = dados.drop(0)

# Inverter a ordem das linhas
dados = dados.iloc[::-1]

# Organizar as colunas 2, 3, 4, 5, 6 e 9 em ordem crescente
colunas_a_organizar = [2, 3, 4, 5, 6, 9]
dados[colunas_a_organizar] = dados[colunas_a_organizar].apply(pd.to_numeric, errors='coerce')
dados = dados.sort_values(by=colunas_a_organizar)

# Criar tabela1 com os pontos
tabela1 = dados[[0, 2]].copy()
tabela1.columns = ['Time', 'Pontos']

# Criar tabela2 com as vitórias
tabela2 = dados[[0, 3]].copy()
tabela2.columns = ['Time', 'Jogos Disputados']

# Criar tabela2 com as vitórias
tabela3 = dados[[0, 4]].copy()
tabela3.columns = ['Time', 'Vitórias']

# Criar tabela2 com as vitórias
tabela4 = dados[[0, 5]].copy()
tabela4.columns = ['Time', 'Derrotas']

# Criar tabela2 com as vitórias
tabela5 = dados[[0, 6]].copy()
tabela5.columns = ['Time', 'Empates']

# Criar tabela2 com as vitórias
tabela6 = dados[[0, 9]].copy()
tabela6.columns = ['Time', 'Saldo de Gols']


# Solicitar ao usuário que escolha a tabela
escolha = input("Digite: ")

# Validar a escolha do usuário
if escolha == '1':
    tabela = tabela1
    titulo = 'Pontuação dos times no Brasileirão 2023'
    ylabel = 'Pontos'
elif escolha == '2':
    tabela = tabela2
    titulo = 'Quantidade de Jogos Disputados dos times no Brasileirão 2023'
    ylabel = 'Jogos Disputados'
elif escolha == '3':
    tabela = tabela3
    titulo = 'Quantidade de Vitórias dos times no Brasileirão 2023'
    ylabel = 'Vitórias'
elif escolha == '4':
    tabela = tabela4
    titulo = 'Quantidade de Derrotas dos times no Brasileirão 2023'
    ylabel = 'Derrotas'
elif escolha == '5':
    tabela = tabela5
    titulo = 'Quantidade de Empates dos times no Brasileirão 2023'
    ylabel = 'Empates'
elif escolha == '6':
    tabela = tabela6
    titulo = 'Quantidade de Saldo de Gols dos times no Brasileirão 2023'
    ylabel = 'Saldo de Gols'
else:
    print("Escolha inválida. Por favor, digite números válidos.")
    exit()
    
for i in range(0, max(tabela[ylabel])+1, 5):
    plt.axhline(y=i, color='blue' , linewidth=0.1)
    
# Plotar o gráfico de barras
largura_coluna = 0.8
plt.bar(tabela['Time'], tabela[ylabel], width=largura_coluna, label=ylabel)
plt.xlabel('Time')
plt.ylabel(ylabel)
plt.title(titulo)
plt.xticks(rotation=90)
plt.legend()
plt.tight_layout()
plt.show()

# Exibir a tabela escolhida
print("Tabela Escolhida:")
print(tabela)

# Exibir os dados
print(dados)