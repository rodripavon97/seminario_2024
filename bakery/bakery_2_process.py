from threading import *
np , nq = 0 , 0
rango= 10000000
text_p_not_critical= "----p no esta en sesion critica---"
text_q_not_critical= "----q no esta en sesion critica"
text_p_critical="----p esta en sesion critica -----"
text_q_critical="----q esta en sesion critica -----"

def mensaje(text) :
    print(text)

def cicle_range(range_):
    for i in range (range_):
            pass

def while_not(conditional1, condictional2, text):
    while not (conditional1 or condictional2):
        pass  
    mensaje(text)


def range_bakery(range_i, text,code):
    for i in range(range_i):
        mensaje(text)
        code()
    
def proc_p(): 
    global np, nq
    def code_p() : 
        cicle_range(rango)
        np=nq+1
        while_not(nq == 0, np<=nq, text_p_critical)
        np=0
    range_bakery(10, text_p_not_critical, code_p)
       

def proc_q(): 
    global np, nq
    def code_q() :
        cicle_range(rango)
        nq=np+1
        while_not(np==0,nq<=np, text_q_critical)
        mensaje ("q en sesion critica")
        nq=0
    range_bakery(10, text_q_not_critical, code_q)

p_hilo = Thread(target=proc_p)
q_hilo = Thread(target= proc_q)

p_hilo.start()
q_hilo.start()