import threading
import time
import random
import sys
import argparse

# Configuración
META = 50  # La posición que representa la meta

# Variable global para indicar si ya hay un ganador
ganador = None
ganador_lock = threading.Lock()

class Caballo(threading.Thread):
    def __init__(self, nombre, meta):
        super().__init__()
        self.nombre = nombre
        self.posicion = 0
        self.meta = meta

    def run(self):
        global ganador
        while self.posicion < self.meta:
            if ganador is not None:
                break
            time.sleep(random.uniform(0.1, 0.5))  # Simula el tiempo de avance
            self.posicion += 1

            # Imprimir el estado de la carrera
            self.imprimir_estado()

            if self.posicion >= self.meta:
                with ganador_lock:
                    if ganador is None:
                        ganador = self.nombre
                        print(f"\n¡{self.nombre} ha ganado la carrera!")

    def imprimir_estado(self):
        sys.stdout.write(f"\r{self.nombre}: {'-' * self.posicion} ({self.posicion})")
        sys.stdout.flush()

# Procesar argumentos de línea de comandos
parser = argparse.ArgumentParser(description="Simulación de una carrera de caballos.")
parser.add_argument('num_caballos', type=int, help='Número de caballos en la carrera')
args = parser.parse_args()

num_caballos = args.num_caballos

if num_caballos <= 0:
    print("El número de caballos debe ser un entero positivo.")
    sys.exit(1)

# Crear e iniciar los caballos
caballos = [Caballo(f"Caballo {i + 1}", META) for i in range(num_caballos)]

for caballo in caballos:
    caballo.start()

for caballo in caballos:
    caballo.join()
