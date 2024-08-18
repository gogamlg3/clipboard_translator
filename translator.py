import easyocr
from PIL import ImageGrab
from time import sleep
import numpy
import win32clipboard
from googletrans import Translator

translator = Translator()
reader = easyocr.Reader(['en'])

while True:
    image = ImageGrab.grabclipboard()
    
    if image != None:
        try:
            image = numpy.array(image)
            ocr = reader.readtext(image, detail=0)
            text = ' '.join(ocr)
            print(f"[original]: {text}")
            translation = translator.translate(text, src='en', dest='ru')
            print(f"[translate]: {translation.text}")
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.CloseClipboard()

        except Exception as e:
            print(e)

    sleep(1)
