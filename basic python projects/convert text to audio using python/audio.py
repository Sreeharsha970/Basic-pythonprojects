#using module of gtts and playsound we have to convert text to audio
from gtts import gTTS
from playsound import playsound
audio="speech.mp3"
language='en'
sp=gTTS(text="myself sreeharsha studying srm university", lang=language,slow=False)
sp.save(audio)
playsound(audio)
print("=======audio is playing====")