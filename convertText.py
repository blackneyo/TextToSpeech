'''
2022.04.18 이동한
'''
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Please say something")
    audio = r.listen(source)
    print("Time over, thanks")


# r은 sr.Recognizer() 인식기 인스턴스
try:
    print("You said: "+r.recognize_google(audio, language = 'en-US'));
except:
    pass

# gTTS load
from gtts import gTTS
input_text = "I like NLP and now this is machine voice"
convert = gTTS(text = input_text, lang='en', slow=False)
# save
convert.save('audio.mp3')
