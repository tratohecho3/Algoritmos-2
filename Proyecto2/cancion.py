from pathlib import Path
from PyQt5.QtCore import QFile


class Cancion:
    def __init__(self, titulo, artista, filepath):
        self.titulo = titulo
        self.artista = artista
        self.filepath = filepath
    def es_igual(self,other):
        if self.artista.lower() == other.artista.lower():
            if self.titulo.lower() == other.titulo.lower():
                return True
            else:
                return False
        else:
            return False

    def es_menor_artista(self,other):
        if self.artista.lower() == other.artista.lower():
            if self.titulo.lower() < other.titulo.lower():
                return True
            else:
                return False
        elif self.artista.lower() < other.artista.lower():
            return True
        else:
            return False

    def es_menor_titulo(self,other):
        if self.titulo.lower() == other.titulo.lower():
            if self.artista.lower() < other.artista.lower():
                return True
            else:
                return False
        elif self.titulo.lower() < other.titulo.lower():
            return True
        else:
            return False

    def __str__(self):
        cadena = "Titulo: " + self.titulo + ", Artista: " + self.artista
        return cadena

