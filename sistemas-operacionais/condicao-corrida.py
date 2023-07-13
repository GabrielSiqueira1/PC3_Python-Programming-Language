from threading import Thread as th

x = 0

def plus():
    global x
    for i in range(0, 100000):
        x+=1
def minus():
    global x
    for i in range(0, 100000):
        x-=1

t1 = th(target=plus)
t2 = th(target=minus)

t1.start()
t2.start()

t1.join()
t2.join()

print(f"O valor de x é {x}")
