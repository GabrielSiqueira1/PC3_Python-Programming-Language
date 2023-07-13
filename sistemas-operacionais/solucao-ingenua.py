from threading import Thread as th

x = 0
ocupado = False

def plus():
    global x
    global ocupado

    while ocupado:
        a = 0
    
    for i in range(0, 100000):
        ocupado = True
        x+=1
        ocupado = False

def minus():
    global x
    global ocupado

    while ocupado:
        a = 0
    
    for i in range(0, 100000):
        ocupado = True
        x-=1
        ocupado = False

t1 = th(target=plus)
t2 = th(target=minus)

t1.start()
t2.start()

t1.join()
t2.join()

print(f"O valor de x é {x}")
# Por mais que o valor dê 0, é possível que uma das threads perca seu acesso a CPU variando o resultado final.
