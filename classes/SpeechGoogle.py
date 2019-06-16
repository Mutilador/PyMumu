
from google_speech import Speech

def SpeechPlay(tecla):
    lang = "pt-br"
    speech = Speech(tecla, lang)
    speech.play()
