import pyttsx3
import PyPDF2
book = open('oop.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
friend = pyttsx3.init()
page = pdfReader.getPage(7)
text = page.extractText()
friend.say(text)
friend.runAndWait()
