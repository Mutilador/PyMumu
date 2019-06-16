from classes.staticLists import *
from classes.SpeechGoogle import *
import random, pygame


speech = SpeechPlay

class QualSilaba():

    def __init__(self):
        self.countSil = 0
        self.selectedSil = ""

    def selectSil(self):

        listSilSimples = SilabasSimples()
        sizeSilSimples = len(listSilSimples)
        self.selectedSil = listSilSimples[random.randint(0,sizeSilSimples-1)]

    def changeSilSelected(self):
        self.selectSil()


class QualLetra():

    def __init__(self):
        self.countLetra = 0
        self.selectedLetra = ""

    def selectLetra(self):
        listLetrasSimples = listaLetras()
        sizeLetrasSimples = len(listLetrasSimples)
        self.selectedLetra = listLetrasSimples[random.randint(0,sizeLetrasSimples-1)]

    def changeLetraSelected(self):
        self.selectLetra()

    def checkResult(self, letra):
        if letra != self.selectedLetra.lower():
            speech("Tente novamente!")
            return False

        speech("Muito bem, parabens! Vamos para próxima letra!")
        self.changeLetraSelected()

        return True