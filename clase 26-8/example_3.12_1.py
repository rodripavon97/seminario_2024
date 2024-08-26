from threading import *
from time import *
global_value= 1
def p():
    global global_value
    local1 = 0

    while True: 
        print("p1: Sesion no critica")

        while True: 
            local1, global_value = global_value, local1
            print("p2 intercambio realizado")

            if local1 == 1:
                sleep(10)
                break
        
        print ("p4 sesion critica de p")

        local1, global_value = global_value, local1
        print ("intercambio realizdo")


def q():
    global global_value
    local2 = 0

    while True: 
        print("q1: Sesion no critica")

        while True: 
            local2, global_value = global_value, local2
            print("q2 intercambio realizado")

            if local2 == 1:
                sleep(10)
                break
        
        print ("q4 sesion critica de p")

        local2, global_value = global_value, local2
        print ("intercambio realizdo")

p1= Thread(target=p)
q1= Thread(target=q)

p1.start()
q1.start()

p1.join()
q1.join()
