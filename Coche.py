"""
Clase Coche base para el Examen de la UD4
Refactorización
Extrae una superclase Vehículo con los campos
    num_serie
    fabricante
    color
:autor: Pablo Merida
"""

"""

"""
class Vehiculo:
    """
    Representa a la superclase Vehiculo

    :param color: Representa el color
    :param num_serie: Representa el numero de serie
    :param fabricante: Representa el fabricante del vehiculo
    """
    color = 'rojo';
    fabricante = 'seat';
    num_serie = 1;


class Coche(Vehiculo):
    """
    Es la clase que hereda de Coche

    :param cilindrada: Es la cilindrada del coche en cuestion

    """
    cilindrada = 1000;

    def __init__(self):
        """
        Constructor heredado de la clase Coche
        """
        pass;

    @property
    def num_serie(self):
        """
        Getter de num_serie

        :return:
        """
        return self.__num_serie

    @num_serie.setter
    def num_serie(self, value):
        """
        Setter de value

        :param value:
        :return:
        """
        self.__num_serie = value

    @property
    def color(self):
        """
        Getter de color

        :return:
        """

        return self.__color

    @color.setter
    def color(self, value: int):
        """
        Setter de color
        :param value:
        :return:
        """

        self.__color = value

    @property
    def cilindrada(self):
        """
        Getter de cilindrada
        :return:
        """

        return self.__cilindrada

    @cilindrada.setter
    def cilindrada(self, value):
        """
        Setter de cilindrada
        :param value:
        :return:
        """
        self.__cilindrada = value

    @property
    def fabricante(self):
        """
        getter de Fabricante
        :return:
        """

        return self.__fabricante

    @fabricante.setter
    def fabricante(self, value):
        """
        Setter de fabricante

        :param value:
        :return:
        """
        self.__fabricante = value
