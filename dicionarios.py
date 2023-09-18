# Criando um dicionário vazio
meu_dicionario = {}

# Adicionando pares chave-valor ao dicionário
meu_dicionario['nome'] = 'João'
meu_dicionario['idade'] = 30
meu_dicionario['cidade'] = 'São Paulo'

# Acessando valores no dicionário
nome = meu_dicionario['nome']
idade = meu_dicionario['idade']

# Verificando se uma chave está no dicionário
chave_presente = 'cidade' in meu_dicionario

# Obtendo todas as chaves e valores do dicionário
todas_as_chaves = meu_dicionario.keys()
todos_os_valores = meu_dicionario.values()

# Iterando sobre as chaves e valores do dicionário
for chave, valor in meu_dicionario.items():
    print(f'{chave}: {valor}')

# Atualizando o valor de uma chave
meu_dicionario['idade'] = 31

# Removendo uma chave do dicionário
cidade_removida = meu_dicionario.pop('cidade')

# Limpando todo o dicionário
meu_dicionario.clear()

# Imprimindo os resultados
print("Dicionário Original:", meu_dicionario)
print("Nome:", nome)
print("Idade:", idade)
print("Chave 'cidade' presente:", chave_presente)
print("Todas as chaves:", todas_as_chaves)
print("Todos os valores:", todos_os_valores)
print("Cidade removida:", cidade_removida)
