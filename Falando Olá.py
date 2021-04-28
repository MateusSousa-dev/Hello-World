'''
    Necessário instalar pacote gTTS e playsound.
        Pode ser instalado por:
            pip install gTTS
            pip install playsound
   Need install packages gTTS and playsound.
        Can install with:
            pip install gTTS
            pip install playsound
'''

from gtts import gTTS
from playsound import playsound
from time import sleep

def audio_en(text):
    speach = gTTS(text, lang='en')
    speach.save('hello.mp3')
    playsound('hello.mp3')

def audio_pt_br(texto):
    fala = gTTS(texto, lang='pt-br')
    fala.save('Ola.mp3')
    playsound('Ola.mp3')

audio_en('Hello World!')
audio_pt_br('Olá Mundo!')
