from threading import *
from time import *

def tarea1():
    print("hola")
    for i in range(100):
        print("vecinirijllo")
        sleep(10)
        


def tarea2():
    print("adioss")
    for i in range(100):
        print("adios")
        sleep(10)


p1 = Thread(target=tarea1)
p2 = Thread(target=tarea2)

p1.start()
p1.join()
p2.start()
p2.join()