import threading
from time import sleep

lock_1 = threading.Lock()
lock_2 = threading.Lock()

def time():
    while True:
        lock_1.acquire()
        print(f"Cheguei {threading.current_thread().getName()}")
        lock_2.acquire()
        print("Time")

def space():
    while True:
        lock_2.acquire()
        print(f"Cheguei {threading.current_thread().getName()}")
        sleep(2)
        lock_1.acquire()
        print("Space")

t1 = threading.Thread(target=time, name='0')
t2 = threading.Thread(target=space, name='1')

t1.start()
t2.start()

t1.join()
t2.join()

print("Terminou!")
