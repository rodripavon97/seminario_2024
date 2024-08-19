"""
Enunciado TP:
Implementar una "carrera de caballos" usando threads, donde cada "caballo" es un Thread o bien un objeto de una clase que sea sub clase de Thread, y contendrá una posición dada por un número entero. El ciclo de vida de este objeto es incrementar la posición en variados instantes de tiempo, mientras no haya llegado a la meta, la cual es simplemente un entero prefijado. Una vez que un caballo llegue a la meta, se debe informar en pantalla cuál fue el ganador, luego de lo cual los demás caballos no deberán seguir corriendo. Imprimir durante todo el ciclo las posiciones de los caballos, o bien de alguna manera el camino que va recorriendo cada uno (usando símbolos Ascii). El programa podría producir un ganador disitnto cada vez que se corra. Opcionalmente, extender el funcionamiento a un array de n caballos, donde n puede ser un parámetro.
"""

#Instalar la libreria colorama
import os
from threading import *
from time import *
from random import *
from colorama import *

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
            print(Fore.MAGENTA,f"\n{self.nombre} ha ganado la carrera 🥇⭐⭐⭐⭐⭐ !")
            self.carrera.registrar_puesto(self.nombre)
        elif self.posicion >= self.distancia_meta:
            self.carrera.registrar_puesto(self.nombre)

    def imprimir_posicion(self):
        recorrido = "⮞⮞⮞⮞⮞⮞" * self.posicion + "🏇🏽"
        os.system("cls" if os.name == 'nt' else 'clear')
        print(Fore.GREEN,f"{self.nombre}: {recorrido}")

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
            print(Fore.RED,f"{i}º puesto: {nombre}")

    def iniciar(self):
        for caballo in self.caballos:
            caballo.start()


        for caballo in self.caballos:
            caballo.join()

def main():
    try:
        msg = Fore.CYAN + "Ingrese el número de caballos: " + Style.RESET_ALL
        msgMeta= Fore.CYAN + "Ingrese la distancia a la meta " + Style.RESET_ALL
        num_caballos = int(input(msg))
        distancia_meta = int(input(msgMeta))
    except ValueError:
        print(Fore.RED,"Por favor, ingrese valores numéricos válidos.")
        return

    carrera = CarreraDeCaballos(num_caballos, distancia_meta)
    carrera.iniciar()
   

if __name__ == "__main__":
    main()