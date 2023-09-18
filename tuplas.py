# Criando uma tupla
minha_tupla = (1, 2, 3, 4, 5)

# Acessando elementos da tupla
primeiro_elemento = minha_tupla[0]
segundo_elemento = minha_tupla[1]

# Encontrando o comprimento da tupla
tamanho_da_tupla = len(minha_tupla)

# Verificando se um elemento está na tupla
elemento_presente = 2 in minha_tupla

# Concatenando tuplas
outra_tupla = (6, 7, 8)
tupla_concatenada = minha_tupla + outra_tupla

# Contando a ocorrência de um elemento na tupla
contagem_do_elemento = minha_tupla.count(3)

# Encontrando o índice de um elemento na tupla
indice_do_elemento = minha_tupla.index(4)

# Imprimindo os resultados
print("Tupla Original:", minha_tupla)
print("Primeiro Elemento:", primeiro_elemento)
print("Tamanho da Tupla:", tamanho_da_tupla)
print("Elemento 2 presente na Tupla:", elemento_presente)
print("Tupla Concatenada:", tupla_concatenada)
print("Contagem do Elemento 3:", contagem_do_elemento)
print("Índice do Elemento 4:", indice_do_elemento)
