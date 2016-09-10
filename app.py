from gtts import gTTS
from pydub import AudioSegment
from countdown import countdown

exerciseCount = int(raw_input('How many exercises? '))
exerciseDuration = int(raw_input('Exercise duration? '))
restDuration = int(raw_input('Rest duration? '))

tabata = []
segmentPaths = []
segments = []


class Exercise(object):

    def __init__(self, name, filePath):
        self.name = name
        self.filePath = filePath

    # create method here that creates an exerciseCycle

for e in range(0, int(exerciseCount)):
    # Give the exercise a title
    question = 'Enter the name of exercise ' + str(e+1) + ': '
    exerciseName = raw_input(question)
    # Add exercise + exercise parameters
    filePath = 'temp/exercise' + str(e+1) + '.mp3'
    exercise = Exercise(exerciseName, filePath)
    tabata.append(exercise)


# Create the soundbits that we need

rest = gTTS(text="Rest!", lang='en-us')
rest.save("temp/rest.mp3")
rest = AudioSegment.from_mp3('temp/rest.mp3')

exerciseCountdown = countdown(exerciseDuration)
restCountdown = countdown(restDuration)

exerciseCountdown.export("temp/exerciseCountdown.mp3", format="mp3")
restCountdown.export("temp/restCountdown.mp3", format="mp3")
exerciseCountdown = AudioSegment.from_mp3('temp/exerciseCountdown.mp3')
restCountdown = AudioSegment.from_mp3('temp/restCountdown.mp3')

fanfare = AudioSegment.from_mp3("audio/fanfare.mp3")

counter = 1

for t in tabata:
    tts = gTTS(text=t.name, lang='en-us')
    tts.save(t.filePath)
    exercise = AudioSegment.from_mp3(t.filePath)
    segment = exercise + exerciseCountdown + rest + restCountdown
    segmentPath = 'temp/segment' + str(counter) + '.mp3'
    segment.export(segmentPath)
    segmentPaths.append(segmentPath)
    counter = counter + 1


for s in segmentPaths:
    segment = AudioSegment.from_mp3(s)
    segments.append(segment)


output = sum(segments) + fanfare
output.export("temp/output.mp3", format="mp3")
