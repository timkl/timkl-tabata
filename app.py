import os
import shutil
from gtts import gTTS
from pydub import AudioSegment

shutil.rmtree('temp')
os.mkdir('temp')

text1 = raw_input("Enter name of exercise1: ")
text2 = raw_input("Enter name of exercise2: ")
text3 = raw_input("Enter name of exercise3: ")

tts1 = gTTS(text=text1, lang='en-us')
tts2 = gTTS(text=text2, lang='en-us')
tts3 = gTTS(text=text3, lang='en-us')
ttsPause = gTTS(text="Pause!", lang='en-us')

tts1.save("temp/exercise1.mp3")
tts2.save("temp/exercise2.mp3")
tts3.save("temp/exercise3.mp3")
ttsPause.save("temp/pause.mp3")

exercise1 = AudioSegment.from_mp3("temp/exercise1.mp3")
exercise2 = AudioSegment.from_mp3("temp/exercise2.mp3")
exercise3 = AudioSegment.from_mp3("temp/exercise3.mp3")
pause = AudioSegment.from_mp3("temp/pause.mp3")


def countdown(seconds):
    ticking = AudioSegment.from_mp3("audio/ticking.mp3")
    milliseconds = seconds * 1000
    countdown = ticking[:milliseconds]
    return countdown

exerciseCountdown = countdown(20)
pauseCountdown = countdown(10)

exerciseCountdown.export("temp/exerciseCountdown.mp3", format="mp3")
pauseCountdown.export("temp/pauseCountdown.mp3", format="mp3")

fanfare = AudioSegment.from_mp3("audio/fanfare.mp3")

tabata = exercise1 + \
            exerciseCountdown + \
            pause + \
            pauseCountdown + \
            exercise2 + \
            exerciseCountdown + \
            pause + \
            pauseCountdown + \
            exercise3 + \
            exerciseCountdown

tabata = tabata + tabata + fanfare

tabata.export("tabata.mp3", format="mp3")

shutil.rmtree('temp')
