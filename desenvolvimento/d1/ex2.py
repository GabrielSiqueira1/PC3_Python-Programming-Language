# relação dos nomes
nomes = ['Maria', 'Julieta', 'Fernando', 'Cristiano', 'Julieta', 'Maria', 'Fernando', 'Cláudio']
# estrutura que irá armazenar o número de letras de cada nome
qtd_letras = {}
# calcula o tamanho de cada nome (em número de letras) e armazena o valor na estrutura
qtd_letras = {nome: len(nome) for nome in nomes}

print(qtd_letras)

qtd_letras.clear()

for nome in nomes:
    qtd_letras[nome] = len(nome)

print(qtd_letras)