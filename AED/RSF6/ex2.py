from PIL import Image
pathImages="AED/RSF7/images/img1.jpg"
newSize=(240,240)
imagem=Image.new(size=newSize, mode= "RGB", color="white")
pixelMap=imagem.load()
for j in range(imagem.width):
    for i in range(imagem.height):
        if i<80:
            pixelMap[i,j]=(0,0,255)
        elif i<160:
            pixelMap[i,j]=(255,255,255)
        else:
            pixelMap[i,j]=(255,0,0)
imagem.show()
imagem.save(pathImages+'ex2.jpg')

'''
imagemRodada = imagem.rotate(90)
'''