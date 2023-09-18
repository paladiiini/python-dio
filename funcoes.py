def apresentacao():
    print("Bem vindo ao meu programa!")
    
nome = "Vitor"

def apresentacao_nome(nome):
    print(f"Olá, meu nome é {nome}")
    
def apresentacao_nome_parametro(nome = "Anonimo"):
    print(f"Olá, meu nome é {nome}")
    
apresentacao()
apresentacao_nome(nome)
apresentacao_nome_parametro()

def soma_total(numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

total = soma_total([1, 2, 3, 4, 5])
print(total)