texto = input("Digite um texto: ")
vogais = "AEIOU"

for letra in texto:
    if letra.upper() in vogais:
        print(letra, end=" ")
        
print()

for numero in range(0, 11):
    print(numero, end=" ")
    
while True:
    print("Loop infinito")
    break