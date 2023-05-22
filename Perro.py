"""
Clase Perro.

Autor: Jaime Rabasco Ronda.
"""
class Perro:

    def __init__(self):
        self.ladra = None

    def ladrar(self):
        self.ladra = 'Guau'
        print(self.ladra);

p = Perro();
p.ladrar();
