import os
import time

menu = '''
----- Menu do Banco ----

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Digite a operação desejada
--> '''

LIMITE_SAQUE = 500
SAQUES_DIARIOS = 3
saldo = 0
extrato = ''
numero_saques = 0

while True:
    opcao = input(menu)
    
    if opcao == 'd':
        os.system('cls')
        valor = float(input('Informe o valor do depósito: R$'))
        
        if valor > 0:
            saldo += valor
            extrato += f'Depositado R${valor:.2f}\n'
        else:
            print('---ERROR---')
            print('Por favor, informe um valor válido')
    
    elif opcao == 's':
        os.system('cls')
        valor = float(input('Informe o valor do saque: R$'))
        
        if saldo < valor:
            print('----ERROR----')
            print("Saldo insuficiente!")
        
        elif numero_saques >= 3:
            print('----ERROR----')
            print("Atingiu o limite de saques do dia!")
        
        elif valor > LIMITE_SAQUE:
            print('----ERROR----')
            print("O limite de saques diário é de R$500,00 !")
        
        elif valor > 0:
            saldo -= valor
            numero_saques += 1
            extrato +=f'{numero_saques}º Saque do dia, sacado R${valor:.2f}\n'
        
        else:
            print('Não foi digitado um valor válido!')
    
    elif opcao =='e':
        os.system('cls')
        print('Aqui está o seu extrato: ')
        print(extrato)
    
    elif opcao =='q':
        os.system('cls')
        print('Saindo do programa em 3..2..1..')
        time.sleep(3)
        break

    else:
        os.system('cls')
        print('Você não digitou nenhuma opção válida!')