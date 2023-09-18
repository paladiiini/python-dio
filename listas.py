# Criando uma lista vazia
minha_lista = []

# Adicionando elementos à lista
minha_lista.append(1)
minha_lista.append(2)
minha_lista.append(3)

# Acessando elementos da lista
primeiro_elemento = minha_lista[0]
segundo_elemento = minha_lista[1]

# Atualizando elementos da lista
minha_lista[1] = 4

# Removendo elementos da lista
elemento_removido = minha_lista.pop(2)

# Encontrando o comprimento da lista
tamanho_da_lista = len(minha_lista)

# Verificando se um elemento está na lista
elemento_presente = 2 in minha_lista

# Concatenando listas
outra_lista = [5, 6, 7]
minha_lista.extend(outra_lista)

# Ordenando a lista
minha_lista.sort()

# Invertendo a ordem da lista
minha_lista.reverse()

# Criando uma cópia da lista
copia_lista = minha_lista.copy()

# Limpando a lista
minha_lista.clear()

# Imprimindo os resultados
print("Lista Original:", copia_lista)
print("Lista Vazia:", minha_lista)
