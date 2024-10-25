from threading import *

wantp = 0
wantq = 0

def procesop():
    global wantp
    global wantq
    i = 0
    while i < 10:
        if wantq == -1:
            wantp = -1
        else:
            wantp = 1
        
        if wantq == int(wantp):
            pass
        else:
            print("Proceso P ENTRA a la sección critica")
            wantp = 0
            print("Proceso P SALE de sección critica")
            i += 1

def procesoq():
    global wantp
    global wantq
    i = 0
    while i < 10:
        if wantp == -1:
            wantq = 1
        else:
            wantq = -1
        
        if wantp == -int(wantq):
            pass
        else:
            print("Proceso Q ENTRA a la sección critica")
            wantq = 0
            print("Proceso Q SALE de sección critica")
            i += 1

threadP = Thread(target=procesop)
threadQ = Thread(target=procesoq)

threadP.start()
threadQ.start()

threadP.join()
threadQ.join()