#   Leer archivo de texto
#   pip install pyttsx3
import pyttsx3

book = open(r"/home/ed/otrapracticamas/Ejercicio-Video-83/book.txt")
book_text = book.readlines()
engine = pyttsx3.init()
for lines in book_text:
    engine.say(lines)
    engine.runAndWait()
