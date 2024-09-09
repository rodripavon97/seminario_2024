from threading import *
from colorama import *

# Inicialización de los semáforos
mutex = Semaphore(1)
count = 0
barrera = Semaphore(0)  # Inicializado a 0, se liberará cuando todos lleguen a la marca

def proceso(id, n_proc):
    global count, barrera, mutex

    # Código antes de la marca
    print(Fore.GREEN,f"Proceso {id} llegó a la marca")

    # Sección crítica para modificar el contador
    mutex.acquire()  # P(mutex)
    count += 1
    if count == n_proc:
        # Si todos los procesos han llegado, liberar a todos
        for _ in range(n_proc):
            barrera.release()  # V(barrera)
        count = 0  # Reiniciar el contador después de liberar a todos
    else:
        mutex.release()  # V(mutex) fuera del else para evitar deadlocks antes de bloquearse
        barrera.acquire()  # P(barrera)
    
    mutex.release()  # V(mutex)

    # Código después de la marca
    print(Fore.LIGHTRED_EX,f"Proceso {id} continúa")

# Leer el número de procesos
n_proc = int(input("Ingrese el número de procesos: "))

# Crear e iniciar los hilos
hilos = []
for i in range(n_proc):
    hilo = Thread(target=proceso, args=(i + 1, n_proc))
    hilos.append(hilo)
    hilo.start()

# Esperar a que todos los hilos terminen
for hilo in hilos:
    hilo.join()
