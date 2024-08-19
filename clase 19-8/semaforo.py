import threading
import time

# Crear un semáforo binario inicializado en 1
semaphore = threading.Semaphore(1)

# Definir la función para el proceso p
def process_p():
    while True:
        # Sección no crítica
        print("Proceso p: En la sección no crítica")
        time.sleep(1)  # Simula tiempo en la sección no crítica
        
        # Entrar en la sección crítica
        semaphore.acquire()
        print("Proceso p: En la sección crítica")
        time.sleep(1)  # Simula tiempo en la sección crítica
        
        # Salir de la sección crítica
        semaphore.release()
        print("Proceso p: Salió de la sección crítica")
        time.sleep(1)  # Simula tiempo entre ciclos

# Definir la función para el proceso q
def process_q():
    while True:
        # Sección no crítica
        print("Proceso q: En la sección no crítica")
        time.sleep(1)  # Simula tiempo en la sección no crítica
        
        # Entrar en la sección crítica
        semaphore.acquire()
        print("Proceso q: En la sección crítica")
        time.sleep(1)  # Simula tiempo en la sección crítica
        
        # Salir de la sección crítica
        semaphore.release()
        print("Proceso q: Salió de la sección crítica")
        time.sleep(1)  # Simula tiempo entre ciclos

# Crear hilos para cada proceso
thread_p = threading.Thread(target=process_p)
thread_q = threading.Thread(target=process_q)

# Iniciar los hilos
thread_p.start()
thread_q.start()

# Unir los hilos para que el programa principal espere a que terminen
thread_p.join()
thread_q.join()
