import pyttsx3
import PyPDF2
book = open("./ThinkAndGrowRich.pdf", 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()
voices = speaker.getProperty('voices')     #get the voices
speaker.setProperty('rate', 150)           #words per minute
speaker.setProperty('voice', voices[1].id) #1 for female voice, 0 for male voice
speaker.setProperty('volume', 1.0)         # Audio volume. 1.0 if max. Always keep the value between 0.0 to 1.0 
for num in range(5,pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text) 
    speaker.runAndWait() 