from PIL import Image
from random import randint

pathImages="AED/RSF7/images/img1.jpg"

def imageArt():
    newSize=(400,400)
    imagem=Image.new(size=newSize, mode= "RGB", color="white")
    pixelMap=imagem.load()
    for i in range(imagem.width):
        for j in range(imagem.height):
            (r, g, b) = imagem.getpixel((i,j))
            r = randint(0,255) ; g = randint(0,255) ; b = randint(0,255)
            imagem.putpixel((i,j), (r, g, b))
    imagem2=imagem
    imagem2.show()
    imagem2.save(pathImages+'ex1.jpg')
imageArt()