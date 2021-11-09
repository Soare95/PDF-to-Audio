from gtts import gTTS...
import PyPDF2

PAGE_NUMBER = 35

file = open("TR_SEA2_Geology.pdf", "rb")
file_reader = PyPDF2.PdfFileReader(file)
page = file_reader.getPage(PAGE_NUMBER)
pdf_text = page.extractText()

text_converter = gTTS(text=pdf_text)
text_converter.save("output.mp3")
