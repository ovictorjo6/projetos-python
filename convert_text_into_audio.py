from gtts import gTTS 
from playsound import playsound

audio = 'speech.mp3'

language = 'en'

sp = gTTS(text = 'A computer is like air conditioning – it becomes useless when you open Windows',lang=language,slow=False)

sp.save(audio)
playsound(audio)
