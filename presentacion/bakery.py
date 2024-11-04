from threading import Thread, Lock, Event

# Cantidad de procesos
N = 5

# Arreglo de números, inicializado a cero
number = [0] * N

# Bloqueo para garantizar acceso seguro al arreglo 'number'
lock = Lock()

# Número máximo de ejecuciones de la sección crítica para cada proceso
max_executions = 3

def bakery_algorithm(i):
    executions = 0  # Contador de ejecuciones de la sección crítica

    while executions < max_executions:
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
        executions += 1  # Incrementar el contador de ejecuciones

        # Simular la sección crítica (puedes ajustar el tiempo)
        Event().wait(1)

        # Paso P6: Salir de la sección crítica y restablecer número a 0
        with lock:
            number[i] = 0
        print(f"Proceso {i} sale de la sección crítica")

        # Simular tiempo en la sección no crítica
        Event().wait(1)

    print(f"Proceso {i} ha terminado sus ejecuciones")

# Crear los threads para simular los procesos
threads = [Thread(target=bakery_algorithm, args=(i,)) for i in range(N)]

# Iniciar los threads
for t in threads:
    t.start()

# Esperar que los threads terminen
for t in threads:
    t.join()

print("Todos los procesos han terminado.")
