from helpers import createSpeak, createTick
from pydub import AudioSegment


def promptUser():
    exercises = []
    numExercises = int(raw_input('How many exercises? '))
    durExercise = int(raw_input('Exercise duration? '))
    durRest = int(raw_input('Rest duration? '))
    for e in range(0, int(numExercises)):
        question = 'Enter the name of exercise ' + str(e+1) + ': '
        exercise = raw_input(question)
        exercises.append(exercise)
    return Tabata(numExercises, durExercise, durRest, exercises)


class Tabata(object):

    def __init__(self, numExercises, durExercise, durRest, exercises):
        self.numExercises = numExercises
        self.durExercise = durExercise
        self.durRest = durRest
        self.exercises = exercises

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

        tabata = sum(exerciseSnippets) + fanfare
        tabata.export("temp/tabata.mp3", format="mp3")


init = promptUser()
init.createTabataMp3()
