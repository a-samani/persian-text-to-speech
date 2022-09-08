from cgitb import text
from importlib.util import spec_from_file_location
import pyttsx3
import converter

name  =  input('Enter Book name with .PDF')

speak = pyttsx3.init()
speak.setProperty('rate',175)
speak.setProperty('voice','persian-pinglish')

text = converter.convertToTxt(name)
speak.say(text)
speak.runAndWait()





