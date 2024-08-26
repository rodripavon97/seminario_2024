from colorama import *
from threading import *
from time import *


sem_a= Semaphore(0)
sem_b = Semaphore(0)
tiempoSeleccionado = 10

def mensaje(text, color= Fore.RESET) :
    print (text, color)

def tiempoEspera(tiempo):
    sleep(tiempo)

def procesoA () : 
    mensaje("Inicializando el proceso 1", Fore.RED)
    tiempoEspera(tiempoSeleccionado)

    mensaje("Yendo no, llegando el proceso 1", Fore.GREEN)
    sem_b.release()
    sem_a.acquire()

    mensaje("Continuando el proceso 1 despues del enceuntroo", Fore.YELLOW)
    tiempoEspera(tiempoSeleccionado)

def procesoB () : 
    mensaje("Inicializando el proceso 2", Fore.RED)
    tiempoEspera(tiempoSeleccionado)
    mensaje("Yendo no, llegando el proceso 2", Fore.CYAN)
    sem_a.release()
    sem_b.acquire()

    mensaje("Continuando el proceso 2 despues del enceuntroo", Fore.GREEN)
    tiempoEspera(tiempoSeleccionado)

hilo1 = Thread(target=procesoA)
hilo2= Thread(target=procesoB)

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()

mensaje("Proceso finalizado por favor reinicie el codigo", Fore.CYAN)