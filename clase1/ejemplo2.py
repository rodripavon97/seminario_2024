from threading import *
from time import *

def tarea1():
    print("hola")
    for i in range(100):
        print(f'i={i},',"vecinirijllo", end='')
        sleep(.10)
        


def tarea2():
    print("adioss")
    for i in range(100):
        print(f'i={i},' ,"adios", end='')
        sleep(.10)

def main () :
    arrayHilos = []
    for i in range(100):
        a = Thread(target=tarea1)
        arrayHilos.append(a)
    for i in range(10):
        print(arrayHilos[i] )

p1 = Thread(target=tarea1)
p2 = Thread(target=tarea2)

p1.start()
p2.start()
p1.join()

p2.join()