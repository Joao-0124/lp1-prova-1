from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Seu código para obter dados e criar tabelas ...

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

# Criar tabela2 com os jogos
tabela2 = dados[[0, 3]].copy()
tabela2.columns = ['Time', 'Jogos Disputados']

# Criar tabela3 com as vitórias
tabela3 = dados[[0, 4]].copy()
tabela3.columns = ['Time', 'Vitorias']

# Criar tabela4 com as derrotas
tabela4 = dados[[0, 5]].copy()
tabela4.columns = ['Time', 'Derrotas']

# Criar tabela5 com os empates
tabela5 = dados[[0, 6]].copy()
tabela5.columns = ['Time', 'Empates']

# Criar tabela6 com o saldo de gols
tabela6 = dados[[0, 9]].copy()
tabela6.columns = ['Time', 'Saldo de Gols']

# Função para criar e exibir um frame com a tabela selecionada
def exibir_tabela(tabela, titulo, ylabel):
    # Função para fechar o frame anterior
    def fechar_frame_anterior():
        for widget in root.winfo_children():
            if isinstance(widget, tk.Frame):
                widget.destroy()

    # Fechar o frame anterior
    fechar_frame_anterior()

    # Calcular a posição do meio da janela
    meio_x = root.winfo_screenwidth() // 2
    meio_y = root.winfo_screenheight() // 2

    # Criar um novo frame para a nova tabela
    frame = tk.Frame(root)
    frame.place(x=meio_x, y=meio_y, anchor='center')  # Alteração aqui

    # Criar uma nova figura com tamanho aumentado
    plt.figure(figsize=(10, 6))  # Ajuste o tamanho conforme necessário
    
    # Adicionar linhas horizontais para cada intervalo desejado no eixo y
    max_value = max(abs(tabela[ylabel]))
    min_value = tabela[ylabel].min()
    
    # Definir intervalo para linhas horizontais
    if min_value < 0:
        for i in range(min_value, max_value + 1, 5):
            plt.axhline(y=i, color='blue', linewidth=0.1)
    else:
        for i in range(0, max_value + 1, 5):
            plt.axhline(y=i, color='blue', linewidth=0.1)
    
    plt.bar(tabela['Time'], tabela[ylabel], width=0.8, label=ylabel)
    plt.xlabel('Time')
    plt.ylabel(ylabel)
    plt.title(titulo)
    plt.xticks(rotation=90)
    plt.tight_layout()

    canvas = FigureCanvasTkAgg(plt.gcf(), master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Funções para exibir diferentes tabelas com botões
def exibir_tabela1():
    exibir_tabela(tabela1, 'Pontuação dos times no Brasileirão 2023', 'Pontos')

def exibir_tabela2():
    exibir_tabela(tabela2, 'Quantidade de Jogos Disputados dos times no Brasileirão 2023', 'Jogos Disputados')

def exibir_tabela3():
    exibir_tabela(tabela3, 'Quantidade de Vitórias dos times no Brasileirão 2023', 'Vitorias')

def exibir_tabela4():
    exibir_tabela(tabela4, 'Quantidade de Derrotas dos times no Brasileirão 2023', 'Derrotas')

def exibir_tabela5():
    exibir_tabela(tabela5, 'Quantidade de Empates dos times no Brasileirão 2023', 'Empates')

def exibir_tabela6():
    exibir_tabela(tabela6, 'Quantidade de Saldo de Gols dos times no Brasileirão 2023', 'Saldo de Gols')
    
# Criar a janela principal
root = tk.Tk()
root.title("Brasileirão 2023")

root.state('zoomed')


# Criar botões para exibir diferentes tabelas
botao_tabela1 = ttk.Button(root, text="Pontos", command=exibir_tabela1 , width=20, padding=(20, 30))
botao_tabela1.pack(anchor=tk.W, pady=5)

botao_tabela2 = ttk.Button(root, text="Jogos Disputados", command=exibir_tabela2 , width=20, padding=(20, 30))
botao_tabela2.pack(anchor=tk.W, pady=5)

botao_tabela3 = ttk.Button(root, text="Vitorias", command=exibir_tabela3 , width=20, padding=(20, 30))
botao_tabela3.pack(anchor=tk.W, pady=5)

botao_tabela4 = ttk.Button(root, text="Derrotas", command=exibir_tabela4 , width=20, padding=(20 , 30))
botao_tabela4.pack(anchor=tk.W, pady=5)

botao_tabela5 = ttk.Button(root, text="Empates", command=exibir_tabela5 , width=20, padding=(20, 30))
botao_tabela5.pack(anchor=tk.W, pady=5)

botao_tabela6 = ttk.Button(root, text="Saldo de Gols", command=exibir_tabela6 , width=20, padding=(20 , 30))
botao_tabela6.pack(anchor=tk.W, pady=5)


# Loop principal da interface gráfica
root.mainloop()