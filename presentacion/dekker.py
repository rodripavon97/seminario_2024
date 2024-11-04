from threading import *

# Variables globales
wantp = False
wantq = False
turn = 1
process= 10
i=0

# Función para el proceso p
def process_p():
    global wantp, wantq, turn, process,i
    while i< process:
        # Sección no crítica
        print("p: Sección no crítica")
        
        wantp = True
        while wantq:  # Espera si q quiere entrar
            if turn == 2:
                wantp = False  # Cede el turno a q
                while turn == 2:
                    pass
                wantp = True  # Vuelve a querer entrar
        # Sección crítica
        print("p: Sección crítica")
        
        turn = 2  # Cede el turno a q
        wantp = False  # Sale de la sección crítica
        i+=1

# Función para el proceso q
def process_q():
    global wantp, wantq, turn, i, process
    while i< process:
        # Sección no crítica
        print("q: Sección no crítica")
        
        wantq = True
        while wantp:  # Espera si p quiere entrar
            if turn == 1:
                wantq = False  # Cede el turno a p
                while turn == 1:
                    pass
                wantq = True  # Vuelve a querer entrar
        # Sección crítica
        print("q: Sección crítica")
        
        turn = 1  # Cede el turno a p
        wantq = False  # Sale de la sección crítica
        i+=1

# Creación de hilos para simular los procesos
thread_p = Thread(target=process_p)
thread_q = Thread(target=process_q)

# Inicio de los hilos
thread_p.start()
thread_q.start()

# Para evitar que el programa termine inmediatamente
thread_p.join()
thread_q.join()
