import os
os.system('cls')

def mostrar_menu():
    print('BANCO - COFRINHO')
    print('1 - Ver saldo')
    print('2 - Depositar')
    print('3 - Sacar')
    print('4 - Ver Extrato')
    print('0 - Sair')

def ver_saldo(saldo):
    print(f'\nSaldo atual: {saldo}')

def depositar(saldo, extrato):
    valor = float(input("\nDigite o valor para depósito: R$ "))

    if valor <= 0:
        print("Operação recusada: o valor do depósito deve ser maior que zero.")
        return saldo

    saldo += valor
    extrato.append(f"Depósito: +R$ {valor}")
    print(f"Depósito de R$ {valor} realizado com sucesso!")
    return saldo

def sacar(saldo, extrato):
    valor = float(input("\nDigite o valor para o saque: R$ "))

    if valor <= 0:
        print("Operação inválida: o valor do saque deve ser maior que zero.")
        return saldo

    if valor > saldo:
        print("Operação inválida: Saldo insuficiente.")
        return saldo

    saldo -= valor
    extrato.append(f"Saque:    -R$ {valor}")
    print(f"Saque de R$ {valor} realizado com sucesso!")
    return saldo

def ver_extrato(extrato, saldo):
    print("\n= Extrato de Movimentações =")
    if len(extrato) == 0:
        print("Nenhuma anomalia registrada no momento.")
    else:
        for movimentacao in extrato:
            print(movimentacao)
    print("--------------------------------")
    print(f"Saldo atual: R$ {saldo}")

saldo = 500.00
extrato = []
opcao = ""

while opcao != "0":
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            ver_saldo(saldo)
        case "2":
            saldo = depositar(saldo, extrato)
        case "3":
            saldo = sacar(saldo, extrato)
        case "4":
            ver_extrato(extrato, saldo)
        case "0":
            print("\nFoi bom enquanto durou, muito obrigado pela presença marcante no nosso estabelecimento. Até logo!")
            break
        case _:
            print("\nOpção inválida! Tente novamente...")

    input("\nPressione Enter para continuar...")