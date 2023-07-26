# declaração das variáveis
inicio = 0
fim = 100

# verifica quais números são divisíveis por cinco, e exibe aqueles que são
for numero in range(inicio, fim):
    if numero % 5 == 0:
        print(numero)