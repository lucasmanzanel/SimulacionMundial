class Seleccion:
    def __init__(self, pais, confederacion, puntos, titulos):
        self.pais = pais
        self.confederacion = confederacion
        self.puntos = puntos
        self.titulos = titulos

    def __str__(self):
        n = len(self.confederacion)
        renglon = "{:<30} {:<18} {:<9} {}".format(self.pais, self.confederacion[2:n], self.puntos, self.titulos)
        return renglon


class Paises_Confederacion:
    def __init__(self, pais, puntos, titulos):
        self.pais = pais
        self.puntos = puntos
        self.titulos = titulos

    def __str__(self):
        renglon = "{:<30} {:<9} {}".format(self.pais, self.puntos, self.titulos)
        return renglon
