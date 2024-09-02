from threading import *
from random import *

text_not_critical = "no esta en sesion critica"
text_critical= "esta en sesion critica"
def message(msg):
    print(msg)

def range_cicle(range_, i, turno):
    for _ in range (range_):
        pass
    message(f"{i} : {text_not_critical} ")
    turno[i]=1+max(turno)

def range_multiproc(n_proc, turno, i):
    for j in range(n_proc):
        if j == 1:
            continue
        while turno[j] != 0 and (turno[i] > turn[j] or (turn[i] == turn[j] and i >j )):
         pass
        message(f"{i} : {text_critical} ")
        turno[i] = 0

def ejecution(threads) :
    for hilos in threads:
        hilos.start()

def bakery_n_process(i):
    global n_proc, turn
    range_cicle(randint(1, 300000), i, turn)
    range_multiproc(n_proc,turn,i)
  
global n_proc, turn
n_proc= int(input ("ingrese un numero de hilos a usar : "))
turn = [0] * n_proc

hilos = [Thread(target=bakery_n_process, args=(i,)) for i in range(n_proc)]
ejecution(hilos)