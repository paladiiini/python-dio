saldo = 2000.0
saque = float(input("Digite o valor do saque: "))

if saldo>=saque:
    saldo-=saque
    print("Saque realizado com sucesso!")
else:
    print("Saldo insuficiente!")
    

opcao = int(input("Digite 1 para saque ou 2 para extrato: "))

if opcao==1:
    valor = float(input("Digite o valor do saque: "))
    if saldo>=saque:
        saldo-=saque
        print("Saque realizado com sucesso!")
elif opcao==2:
    print("Extrato: ", saldo)
else:
        print("Saldo insuficiente!")