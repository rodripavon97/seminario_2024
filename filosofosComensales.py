from snakes.nets import *
import time

# Crear una red de Petri
net = PetriNet('Dining Philosophers')

# Lugares para los filósofos pensando y comiendo
for i in range(1, 6):
    net.add_place(Place(f'P{i}', [1]))  # Pensando
    net.add_place(Place(f'C{i}', []))   # Comiendo

# Lugares para los tenedores
for i in range(1, 6):
    net.add_place(Place(f'T{i}', [1]))  # Cada tenedor tiene un token al inicio

# Transiciones para pensar -> comer y comer -> pensar
for i in range(1, 6):
    net.add_transition(Transition(f'T{i}_think_to_eat'))
    net.add_transition(Transition(f'T{i}_eat_to_think'))

# Conectar los filósofos a las transiciones y los tenedores
for i in range(1, 6):
    next_i = (i % 5) + 1  # Tenedores compartidos con el siguiente filósofo
    
    net.add_input(f'P{i}', f'T{i}_think_to_eat', Value(1))  # Valor 1 representa un token
    net.add_input(f'T{i}', f'T{i}_think_to_eat', Value(1))  # Valor 1 representa un token
    net.add_input(f'T{next_i}', f'T{i}_think_to_eat', Value(1))  # Tenedor siguiente
    net.add_output(f'C{i}', f'T{i}_think_to_eat', Value(1))

    net.add_input(f'C{i}', f'T{i}_eat_to_think', Value(1))
    net.add_output(f'T{i}', f'T{i}_eat_to_think', Value(1))
    net.add_output(f'T{next_i}', f'T{i}_eat_to_think', Value(1))
    net.add_output(f'P{i}', f'T{i}_eat_to_think', Value(1))

# Función para disparar todas las transiciones de manera continua
def simulate_dining_philosophers():
    while True:
        for i in range(1, 6):
            try:
                print(f"Disparando T{i}_think_to_eat")
                net.transition(f'T{i}_think_to_eat').fire({})
                print(f"Tokens en P{i} (Pensando): {net.place(f'P{i}').tokens}")
                print(f"Tokens en C{i} (Comiendo): {net.place(f'C{i}').tokens}")
            except Exception as e:
                print(f"No se pudo disparar T{i}_think_to_eat: {e}")

            time.sleep(1)  # Simulación con pausa de 1 segundo

            try:
                print(f"Disparando T{i}_eat_to_think")
                net.transition(f'T{i}_eat_to_think').fire({})
                print(f"Tokens en P{i} (Pensando): {net.place(f'P{i}').tokens}")
                print(f"Tokens en C{i} (Comiendo): {net.place(f'C{i}').tokens}")
            except Exception as e:
                print(f"No se pudo disparar T{i}_eat_to_think: {e}")

            time.sleep(1)  # Simulación con pausa de 1 segundo

# Ejecutar la simulación
simulate_dining_philosophers()
