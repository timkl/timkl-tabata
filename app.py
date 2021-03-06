from helpers import createSpeak, createTick
from pydub import AudioSegment


def promptUser():
    '''
    Take the users input and return a Tabata instance.
    '''
    exercises = []
    numExercises = int(raw_input('How many exercises? '))
    durExercise = int(raw_input('Exercise duration? '))
    durRest = int(raw_input('Rest duration? '))
    numCycles = int(raw_input('How many cycles? '))
    for e in range(0, int(numExercises)):
        question = 'Enter the name of exercise ' + str(e+1) + ': '
        exercise = raw_input(question)
        exercises.append(exercise)
    return Tabata(numExercises, durExercise, durRest, exercises, numCycles)


class Tabata(object):
    '''
    Use the Tabata instance properties to create the mp3.
    '''
    def __init__(self, numExercises, durExercise,
                 durRest, exercises, numCycles):
        self.numExercises = numExercises
        self.durExercise = durExercise
        self.durRest = durRest
        self.exercises = exercises
        self.numCycles = numCycles

    def createTabataMp3(self):
        exerciseSnippets = []
        exerciseTickPath = createTick('tickExercise', self.durExercise)
        exerciseTick = AudioSegment.from_mp3(exerciseTickPath)
        restSpeakPath = createSpeak("Rest")
        restSpeak = AudioSegment.from_mp3(restSpeakPath)
        restTickPath = createTick('tickRest', self.durRest)
        restTick = AudioSegment.from_mp3(restTickPath)
        fanfare = AudioSegment.from_mp3("audio/fanfare.mp3")
        for e in self.exercises:
            exerciseSpeakPath = createSpeak(e, self.exercises.index(e))
            exerciseSpeak = AudioSegment.from_mp3(exerciseSpeakPath)
            exercise = exerciseSpeak + exerciseTick + restSpeak + restTick
            exerciseSnippets.append(exercise)

        tabata = (sum(exerciseSnippets) * self.numCycles) + fanfare

        tabata.export("tabata.mp3", format="mp3")


init = promptUser()
init.createTabataMp3()
