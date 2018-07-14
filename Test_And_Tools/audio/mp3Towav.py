import pydub
sound = pydub.AudioSegment.from_mp3("./test.mp3")
sound.export("./test.wav", format="wav")