# corrigir instalação https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i
# instalar outra língua: https://github.com/tesseract-ocr/tessdata
# pegar linguas: print(pytesseract.get_languages())

#caminho = r"C:\Users\Python\AppData\Local\Programs\Tesseract-OCR"

#texto = pytesseract.image_to_string(imagem, lang="por") #
#print(texto)

#C:\Program Files\Tesseract-OCR


import cv2
import pytesseract

# ler a imagem e trazer para python
imagem = cv2.imread("11111.png")

# extrair informação da imagem, usando tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR' + r'\tesseract.exe'
texto = pytesseract.image_to_string(imagem)

print(texto)