import os
import time

def menu():
    menu = '''
    ----- Menu do Banco ----

    [nu] Cadastrar Novo Usuário
    [nc] Cadastrar Nova Conta do Banco
    [l] Exibir Contas
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    Digite a operação desejada
    --> '''
    return input(menu)

def depositar(valor, saldo):
    if valor > 0:
        saldo += valor
        extrato = guardar_extrato(extrato= f'Depositado R${valor:.2f}')

        return saldo, extrato
    else:
        return 'Valor abaixo de 0!!'

def sacar(*, valor, saldo, limite, numero_saques):
    if saldo < valor:
        print( '----ERROR----')
        print('Saldo Insuficiente!')
    
    elif numero_saques >= 3:
        print( '----ERROR----')
        print('Atingiu o limite de saques do dia!')
    
    elif valor > limite:
        print('----ERROR----')
        print('O limite de saques diário é de R$500,00 !')
    
    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        extrato = guardar_extrato(extrato= f'{numero_saques}º Saque do dia, sacado R${valor:.2f}')
        return saldo, extrato

def guardar_extrato(extrato):
    lista_extrato.append(extrato)
    return lista_extrato

def novo_usuario(usuarios):
    cpf = input('Digite o CPF por favor: ')
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print('\nJá existe algum usuário com esse CPF!')
        return
    
    nome = input('Digite o seu nome completo: ')
    data_nascimento = input('Digite a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Digite o endereço (rua, nro - bairro - cidade/sgila estado): ')

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print('Usuário criado com sucesso!!')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def cadastrar_conta_bancaria(agencia, numero_conta, usuarios):
    cpf = input("Por favor, informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Conta criada')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    
    print('---ERROR---')
    print('Usuário não encontrado!')

def listar_contas(contas):
    for conta in contas:
        print('='*50)
        print(f'Agência:    {conta['agencia']}')
        print(f'Conta:  {conta['numero_conta']}')
        print(f'Titular:    {conta['usuario']['nome']}')

def main():
    
    LIMITE_SAQUE = 500
    AGENCIA = '0001'

    saldo = 0
    lista_extrato = []
    numero_saques_por_dia = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        
        if opcao == 'nu':
            novo_usuario(usuarios)
            
        elif opcao =='nc':
            numero_conta = len(contas) + 1
            conta = cadastrar_conta_bancaria(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 'l':
            listar_contas(contas)

        elif opcao == 'd':
            os.system('cls')
            try:
                valor = float(input('Informe o valor do depósito: R$'))
                saldo, lista_extrato = depositar(valor, saldo)
                print('== Depósito Realizado com Sucesso! ==')
            except:
                print('---ERROR---')
                print('Por favor, informe um valor válido')
        
        elif opcao == 's':
            os.system('cls')
            
            try:
                valor = float(input('Informe o valor do saque: R$'))
                resultado = sacar(valor=valor, saldo=saldo, limite=LIMITE_SAQUE, numero_saques=numero_saques_por_dia)
                if resultado is not None:
                    saldo, lista_extrato = resultado
                    numero_saques_por_dia += 1
            except:
                print('Não foi digitado um valor válido!')
        
        elif opcao =='e':
            os.system('cls')
            print('---TRANSACOES EFETUADAS---')
            for transacao in lista_extrato:
                print(transacao)
            input()
            os.system('cls')
        
        elif opcao =='q':
            os.system('cls')
            print('Saindo do programa em 2..1..')
            time.sleep(2)
            break

        else:
            os.system('cls')
            print('Você não digitou nenhuma opção válida!')

main()