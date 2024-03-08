menu_opcoes = " Menu de opções "
menu = f'''

{menu_opcoes.center(26, "=")}\n
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

saldo = 0
limite = 500
extrato = ""
deposito = 0
saque = 0
valor_saques = 0
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    # DEPÓSITO
    if opcao == "d":
        print(" Depósito ".center(25, "="))
        deposito = float(input("Deposite o valor desejado: "))
        
        if deposito > 0:
            print("Depositado com sucesso!")
            saldo += deposito
            extrato +=f"\nDeposito: R${deposito:.2f}"
            
        else:
            print("Valor inválido")
            deposito = 0
    
    # SAQUE
    elif opcao == "s":
        print(" Saque ".center(25, "=")) 
        if numero_saques < LIMITE_SAQUES:
            saque = float(input("informe o valor do saque: "))
            if saque > saldo:
                print("Saldo insuficiente")
            elif saldo > 500:    
                print("Limite de saque: R$500")
            else:
                print("Saque feito com sucesso!")
                valor_saques += saque
                saldo = saldo - saque
                extrato +=f"\nSaque: R${saque:.2f}"
                numero_saques+= 1
        else:
            print("Limite de saque diário atingido")
    
    # EXTRATO 
    elif opcao == "e":
        print(" Extrato ".center(25, "="))
        print(extrato)
        print(f"\nSaldo atual da conta: R${saldo:,.2f}")
        
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")