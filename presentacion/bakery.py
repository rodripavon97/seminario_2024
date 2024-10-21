from threading import *

# Cantidad de procesos
N = 5

# Arreglo de números, inicializado a cero
number = [0] * N

# Bloqueo para garantizar acceso seguro al arreglo 'number'
lock = Lock()

def bakery_algorithm(i):
    while True:
        # Sección no crítica
        print(f"Proceso {i} en sección no crítica")

        # Paso P2: Elegir un número de turno
        with lock:
            number[i] = 1 + max(number)
        print(f"Proceso {i} tiene número {number[i]}")

        # Paso P3 y P4: Espera activa hasta que le toque entrar a la sección crítica
        for j in range(N):
            if i != j:
                while number[j] != 0 and (number[j], j) < (number[i], i):
                    pass

        # Sección crítica
        print(f"Proceso {i} en sección crítica")

        # Simular la sección crítica (puedes ajustar el tiempo)
        Event().wait(1)

        # Paso P6: Salir de la sección crítica y restablecer número a 0
        number[i] = 0
        print(f"Proceso {i} sale de la sección crítica")

        # Simular tiempo en la sección no crítica
        Event().wait(1)

# Crear los threads para simular los procesos
threads = [Thread(target=bakery_algorithm, args=(i,)) for i in range(N)]

# Iniciar los threads
for t in threads:
    t.start()

# Esperar que los threads terminen (esto nunca sucederá porque el loop es infinito)
for t in threads:
    t.join()
