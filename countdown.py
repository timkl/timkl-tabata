from pydub import AudioSegment


def countdown(seconds):
    ticking = AudioSegment.from_mp3("audio/ticking.mp3")
    milliseconds = seconds * 1000
    countdown = ticking[:milliseconds]
    return countdown
