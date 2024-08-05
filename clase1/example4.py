from threading import *

def tarea1(x):
        print("print", x)
        
def main () :
    arrayHilos = []
    for i in range(100):
        a = Thread(target=tarea1, args=10)
        arrayHilos.append(a)
        
for i in range(10):
    arrayHilos = Thread(target=tarea1(i))
    arrayHilos.start()

main()