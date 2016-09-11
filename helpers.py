from gtts import gTTS
from pydub import AudioSegment


def countdown(seconds):
    ticking = AudioSegment.from_mp3("audio/ticking.mp3")
    milliseconds = seconds * 1000
    countdown = ticking[:milliseconds]
    return countdown


def createSpeak(line, index="no-index"):
    speak = gTTS(text=line, lang='en-us')
    if index != "no-index":
        speakPath = 'temp/exercise' + str(index+1) + '.mp3'
    else:
        speakPath = 'temp/' + line + '.mp3'
    speak.save(speakPath)
    return speakPath


def createTick(title, seconds):
    tick = countdown(seconds)
    tickPath = 'temp/' + title + '.mp3'
    tick.export(tickPath, format="mp3")
    return tickPath
