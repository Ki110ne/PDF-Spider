import io
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import sys
import string
import os
import hashlib
def get_pdf():
	return [i for i in os.listdir(".") if i.endswith("pdf")]
def convert_pdf_2_text(path):
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    device = TextConverter(rsrcmgr, retstr,  laparams=LAParams())
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    with open(path, 'rb') as fp:
        for page in PDFPage.get_pages(fp, set()):
            interpreter.process_page(page)
        text = retstr.getvalue()
    device.close()
    retstr.close()
    return text
def find_password():
	pdf_path = get_pdf()
	for i in pdf_path:
		print("Searching word in " + i)
		pdf_text = convert_pdf_2_text(i).split(" ")
		for word in pdf_text:
			sha1_password = hashlib.sha1((word+"Salz!").encode()).hexdigest()
			if sha1_password == '3fab54a50e770d830c0416df817567662a9dc85c':
				print("Find the password :" + word)
				exit()
if __name__ == "__main__":
	find_password()