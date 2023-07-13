import threading

x = 0
turn = '-1'
interested = [False, False]

def plus():
    global x
    global turn
    global interested

    for i in range(0,10):

        turn = threading.current_thread().getName()
        interested[int(threading.current_thread().getName())] = True

        while turn == threading.current_thread().getName() and interested[1]:
            string = 'ocupado'

        x += 1

        interested[ int(threading.current_thread().getName()) ] = False

def minus():
    global x
    global turn
    global interested

    for i in range(0,10):

        turn = threading.current_thread().getName()
        interested[int(threading.current_thread().getName())] = True

        while turn == threading.current_thread().getName() and interested[0]:
            string = 'ocupado'

        x -= 1

        interested[ int(threading.current_thread().getName()) ] = False

t1 = threading.Thread(target=plus, name='0')
t2 = threading.Thread(target=minus, name='1')

t1.start()
t2.start()

t1.join()
t2.join()

print(f"O valor de x é {x}")
