import pyttsx3

def text_to_speak(text):
	engine = pyttsx3.init()
	engine.setProperty('rate',150)
	engine.setProperty('volume',0.9)
	engine.say(text)
	engine.runAndWait()

text = 'Hello, how are you, Plamen Stoilkov'
text_to_speak(text)
