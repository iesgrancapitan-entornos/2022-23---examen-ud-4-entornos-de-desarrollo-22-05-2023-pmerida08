"""
Clase Perro.

Autor: Pablo Merida
"""
class Perro:
    """
    Clase que representa a un perro

    """
    def __init__(self):
        """
        Constructor de la clase Perro

        :param ladra: Hace que ladre el perro
        """
        self.ladra = None

    def ladrar(self):
        """
        Hace el ladrido
        :return:
        """
        self.ladra = 'Guau'
        print(self.ladra);

p = Perro();
p.ladrar();
