# declaração das variáveis
inicio = 100
fim = 501

# verifica quais números são divisíveis por cinco, e exibe aqueles que são
for numero in range(inicio, fim):
    if numero % 5 == 0 and numero % 2 == 0 and numero % 7 == 0:
        print(numero)