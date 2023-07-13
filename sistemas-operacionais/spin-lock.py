import threading

x = 0
turn = '0'

def plus():
    global x
    global turn

    for i in range(0, 10):
        while threading.current_thread().getName() != turn:
            string = 'ocupado'

        x += 1

        turn = '1'

def minus():
    global x
    global turn

    for i in range(0, 10):
        while threading.current_thread().getName() != turn:
            string = 'ocupado'

        x -= 1

        turn = '0'

t1 = threading.Thread(target=plus, name='0')
t2 = threading.Thread(target=minus, name='1')

t1.start()
t2.start()

t1.join()
t2.join()

print(f"O valor de x é {x}");
