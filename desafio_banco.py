menu = """
    Bem vindo ao banco DIO!
 Digite o número para efetuar sua operação

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

opcao_valida = False
while not opcao_valida:

    opcao = input(menu)
    if opcao == "1":
        deposito = float(input("Informe quanto deseja depositar na conta: "))
        if deposito < 0:
            print("Não pode fazer depositos negativos,tente novamente")
        else:
            saldo += deposito
            extrato += f"Deposito: R$ {deposito:.2f}\n"
    elif opcao == "2":
        saque = float(input("Informe o quanto deseja sacar de sua conta: "))
        if numero_saques >= LIMITE_SAQUES:
            print("O limite máximo de saques diários já foi utilizado, tente outro dia")
        elif saque > limite:
            print("Seu limite de saque é de 500 reais, tente novamente")
        elif saque > saldo:
            print("Você não tem saldo suficiente")
        elif saque <= 0:
            print("Saque deve ser maior que 0")
        elif saque <= saldo:
            saldo -= saque
            numero_saques +=1
            extrato += f"Saque: R$ {saque:.2f}\n"
        else:
            print("Saque invalido, tente novamente")
    elif opcao == "3":
        print("============================ EXTRATO ============================")
        if not extrato:
            print("Ainda não houve movimentações na conta.")
        else:
            print(extrato)
            print(f"Saldo atual: R$ {saldo:.2f}")    
        print("=================================================================") 
    elif opcao == "0":
        print("Obrigado por usar nosso Banco, até mais!")
        opcao_valida = True
    else:
        print("Operação não existente, tente novamente")                   