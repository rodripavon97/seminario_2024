from colorama import *
from threading import *
from time import *


sem_a= Semaphore(0)
sem_b = Semaphore(0)
def procesoA () : 
    print ("proc 1: Inicio")
    sleep(4)

    print("proc 1: llegue")
    sem_b.release()
    sem_a.acquire()

    print("proc 1: continuando el encuentro")
    sleep(8)

def procesoB () : 
    print ("proc 2: Inicio")
    sleep(10)

    print("proc 2: llegue")
    sem_a.release()
    sem_b.acquire()

    print("proc 2: continuando el encuentro")
    sleep(8)

hilo1 = Thread(target=procesoA)
hilo2= Thread(target=procesoB)

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()

print ("proceso finalizado")