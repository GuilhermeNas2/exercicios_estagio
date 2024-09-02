import json
import re
import random

#EXERCICIO 1 
def ex1():
    indice = 13
    soma = 0
    k = 0

    while(k < indice):
        k = k + 1
        soma = soma + k

    print(f"\nO resultado é {soma}\n")    

#EXERCICIO 2
def fibo():
    fibo = [0,1]
    num = None
    num2 = 0
    ident = 0
    text = "O número não faz parte da sequência"

    while(num is None or num <= 0):
        num = int(input('\ndigite um número positivo maior que zero\n '))

    while(num2 < num):   
        calc = fibo[ident-2] + fibo[ident-1]    
        fibo.append(calc)
        if(calc == num):
            text = "O número faz parte da sequência de Fibonacci"    
        num2 = calc
    print(f"\n{text} {fibo}\n")

#EXERCICIO 3 
def faturamento():
    faturamentoMax = [0]
    faturamentoMin = [0]
    faturaPerDia = []
    mediaFatura = 0

    diaMax = list()
    diaMin = list()
    dias = 0

    with open('faturamento.json', 'r') as file:
        dados = json.load(file)

    for data,val in dados["faturamento_diario"].items():
        mediaFatura += val
        dias += 1 

        faturaPerDia.append(val)

        if(faturamentoMax[0] == 0 or faturamentoMin == 0):
            faturamentoMax[0] = val
            faturamentoMin[0] = val
            diaMax.append(data)
            diaMin.append(data)

        if(val == faturamentoMax[0]):              
            diaMax.append(data)  

        if(val == faturamentoMin[0]):         
            diaMin.append(data)    

        if(val > faturamentoMax[0]):
            faturamentoMax[0] = val       
            diaMax = list()
            diaMax.append(data)
        if(val < faturamentoMin[0]):
            faturamentoMin[0] = val   
            diaMin = list()
            diaMin.append(data) 

    mediaFatura = mediaFatura/dias 
    dias = 0

    for i in range(0, len(faturaPerDia),1):
        if(mediaFatura < faturaPerDia[i]):
            dias += 1

    print(f"\nO menor faturamento foi {faturamentoMin[0]} nos dias {diaMin}")
    print(f"O maior faturamento foi {faturamentoMax[0]} nos dias {diaMax}")
    print(f"O total de dias em que o faturamento foi maior que a media diária mensal é de {dias}\n")

# EXERCICIO 4
def regEx(values):
    money = re.sub(r'R\$|\.', '', values)   
    moneyConvert = float(money.replace(",","."))
    return moneyConvert
def contribuiMoney():
    totalValue = 0
    value = {}

    contribuicao = {
        "SP" : "R$67.836,43",
        "RJ" : "R$36.678,66",
        "MG" : "R$29.229,88",
        "ES" : "R$27.165,48",
        "OUTROS": "R$19.849,53"
    }

    for estado, values in contribuicao.items():    
        coin = regEx(values)
        totalValue += coin  
        value[estado] = coin

    for estado, cont in value.items():
        cont = cont * 100    
        contribui = cont / totalValue
        value[estado] = contribui
        print(f"\nO valor arrecadado pelo estado {estado} representa {contribui:.2f}% do montante total")
    print(f"O montante total é de R${totalValue}\n")    
    
#EXERCICIO 5
def randomFrase():
    frase = input("DIGITE UMA PALAVRA OU FRASE: ")    
    alreadyNumbers = list()
    cond = False
    newFrase = ""
    for i in range(0, len(frase), 1):  
        while(cond == False):
            rNum = random.randint(0, len(frase)-1)
            if(rNum not in alreadyNumbers):
                cond = True
                alreadyNumbers.append(rNum)           
    
        cond = False
        newFrase += frase[rNum] 
        
    print(f"\n{newFrase}\n")   
    
cond = True   
while(cond == True):
    resposta = input("Ola, me chamo Ultron, como posso te ajudar hoje? Os serviços que tenho disponíveis são os seguintes:\n 1-Exercio 1 \n 2-Exercio 2 \n 3-Exercio 3 \n 4-Exercio 4 \n 5-Exercio 5 \n 6-Sair\n Digite o número do item que desejar: ")
    if(resposta == "1"):        
        ex1()        
    if(resposta == "2"):
        fibo()
    if(resposta == "3"):
        faturamento()
    if(resposta == "4"):
        contribuiMoney()
    if(resposta == "5"):
        randomFrase()
    if(resposta == "6"):      
        cond = False   
    prosseguir = input("Deseja continuar senhor?\n 1-SIM \n 2-NÃO \n Digite o número do item que desejar:")    
    if(prosseguir == "2"):
        cond = False               
print("Muito obrigado por me testar senhor, meu dono teve um certo carinho em fazer esses exercícios para você, espero que tenha gostado :)")