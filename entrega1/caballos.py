from threading import *
from time import *
from random import *

class Caballo(Thread):
    def __init__(self, nombre, distancia_meta, carrera):
        super().__init__()
        self.nombre = nombre
        self.posicion = 0
        self.distancia_meta = distancia_meta
        self.carrera = carrera

    def correr(self):
        while not self.carrera.ganador_evento.is_set() and self.posicion < self.distancia_meta:
            self.posicion += randint(1, 3)
            self.imprimir_posicion()
            sleep(uniform(0.1, 0.5))
        
        if self.posicion >= self.distancia_meta and not self.carrera.ganador_evento.is_set():
            self.carrera.ganador_evento.set()
            print(f"\n{self.nombre} ha ganado la carrera!")
            self.carrera.registrar_puesto(self.nombre)
        elif self.posicion >= self.distancia_meta:
            self.carrera.registrar_puesto(self.nombre)

    def imprimir_posicion(self):
        recorrido = "-" * self.posicion + ">"
        print(f"{self.nombre}: {recorrido}")

    def run(self):
        self.correr()

class CarreraDeCaballos:
    def __init__(self, num_caballos, distancia_meta):
        self.ganador_evento = Event()
        self.caballos = [Caballo(f"Caballo {i+1}", distancia_meta, self) for i in range(num_caballos)]
        self.distancia_meta = distancia_meta
        self.puestos = []

    def registrar_puesto(self, nombre):
        self.puestos.append(nombre)
        if len(self.puestos) == len(self.caballos):
            self.mostrar_puestos()

    def mostrar_puestos(self):
        print("\nResultados finales:")
        for i, nombre in enumerate(self.puestos, 1):
            print(f"{i}º puesto: {nombre}")

    def iniciar(self):
        for caballo in self.caballos:
            caballo.start()

        for caballo in self.caballos:
            caballo.join()

def main():
    try:
        num_caballos = int(input("Ingrese el número de caballos: "))
        distancia_meta = int(input("Ingrese la distancia a la meta: "))
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")
        return

    carrera = CarreraDeCaballos(num_caballos, distancia_meta)
    carrera.iniciar()

if __name__ == "__main__":
    main()