import threading
import time

wantp = False
wantq = False
last = 1


def critical_section_p():
    global wantp, last
    while True:
        
        time.sleep(1)

        
        wantp = True
        last = 1
        while wantq and last == 1:
            pass  # Espera mientras q quiera entrar y es el turno de q

       
        print("Proceso p está en la sección crítica")
        time.sleep(1)

        
        wantp = False
        print("Proceso p ha salido de la sección crítica")

def critical_section_q():
    global wantq, last
    while True:
        # Sección no crítica
        time.sleep(1)

        
        wantq = True
        last = 2
        while wantp and last == 2:
            pass  # Espera mientras p quiera entrar y es el turno de p

        
        print("Proceso q está en la sección crítica")
        time.sleep(1)

        
        wantq = False
        print("Proceso q ha salido de la sección crítica")

thread_p = threading.Thread(target=critical_section_p)
thread_q = threading.Thread(target=critical_section_q)

thread_p.start()
thread_q.start()

thread_p.join()
thread_q.join()