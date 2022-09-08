import arabic_reshaper
from bidi.algorithm import get_display
import pdfplumber
def convertToTxt (name):
    with pdfplumber.open(name) as pdf:
        my_page = pdf.pages[0]
        thepages=my_page.extract_text()
        reshaped_text = arabic_reshaper.reshape(thepages)
        return (get_display(reshaped_text))
    