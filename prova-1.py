cont = 0
contA = 0
contV = 0
contR = 0
porcentagemR = ''
porcentagemV = ''
porcentagemA = ''
idade_menor_A = 1000
idade_maior_A = 0
idade_menor_V = 1000
idade_maior_V = 0
idade_menor_R = 1000
idade_maior_R = 0
idade_menor_respA = ''
idade_maior_respA = ''
idade_menor_respV = ''
idade_maior_respV = ''
idade_menor_respR = ''
idade_maior_respR = ''
contM = 0
contF = 0
contMA = 0
contFA = 0
contMV = 0
contFV = 0
contMR = 0
contFR = 0
while True:
    cor = (input("Cor Preferida \nIndique A para Azul \nIndique V para Verde \nIndique R para Rosa \n(EM CAIXA ALTA)\n\n "))
    idade = int(input("Informe sua Idade:\n\n"))
    sexo = (input("Informe seu Sexo: \nM para Masculino \nF para Feminino \n(EM CAIXA ALTA)\n\n"))
    cont += 1
    if(cor == 'A'):
        contA += 1
        if contA > 0:
            porcentagemA = (contA * 100) / cont
        if (idade > idade_maior_A):
            idade_maior_A = idade
            idade_maior_respA = cor
        if (idade < idade_menor_A):
            idade_menor_A = idade
            idade_menor_respA = cor
        if sexo == 'M':
            contMA += 1
        if sexo == 'F':
            contFA +=1
    if(cor == 'V'):
        contV += 1
        if contV > 0:
            porcentagemV = (contV * 100) / cont
        if (idade > idade_maior_V):
            idade_maior_V = idade
            idade_maior_respV = cor
        if (idade < idade_menor_V):
            idade_menor_V = idade
            idade_menor_respV = cor
        if sexo == 'M':
            contMV += 1
        if sexo == 'F':
            contFV +=1
    if(cor == 'R'):
        contR += 1
        if contR > 0:
            porcentagemR = (contR * 100) / cont
        if (idade > idade_maior_R):
            idade_maior_R = idade
            cor = 'R'
            idade_maior_respR = cor
        if (idade < idade_menor_R):
            idade_menor_R = idade
            idade_menor_respR = cor
        if sexo == 'M':
            contMR += 1
        if sexo == 'F':
            contFR +=1
    if(input("Deseja Continuar? (S, N)" )) != "S":
        break

print("TOTAL DE PESSOAS" , cont)
print("Percentual de Pessoas que prefere Azul" , porcentagemA)  
print("Percentual de Pessoas que prefere Verde" , porcentagemV)  
print("Percentual de Pessoas que prefere Rosa" , porcentagemR)
print(f"Idade da Pessoa Mais Velha tem {idade_maior_A} anos de idade e prefere a cor {idade_maior_respA}")
print(f"Idade da Pessoa Mais Velha tem {idade_menor_A} anos de idade e prefere a cor {idade_maior_respA}")
print(f"Idade da Pessoa Mais Velha tem {idade_maior_V} anos de idade e prefere a cor {idade_maior_respV}")
print(f"Idade da Pessoa Mais Velha tem {idade_menor_V} anos de idade e prefere a cor {idade_maior_respV}")
print(f"Idade da Pessoa Mais Velha tem {idade_maior_R} anos de idade e prefere a cor {idade_maior_respR}")
print(f"Idade da Pessoa Mais Velha tem {idade_menor_R} anos de idade e prefere a cor {idade_maior_respR}")
print("A quantidade de pessoas do Sexo Masculino que prefere a cor Azul é: " , contMA)
print("A quantidade de pessoas do Sexo Feminino que prefere a cor Azul é: " , contFA)
print("A quantidade de pessoas do Sexo Masculino que prefere a cor Verde é: " , contMV)
print("A quantidade de pessoas do Sexo Feminino que prefere a cor Verde é: " , contFV)
print("A quantidade de pessoas do Sexo Masculino que prefere a cor Rosa é: " , contMR)
print("A quantidade de pessoas do Sexo Feminino que prefere a cor Rosa é: " , contFR)