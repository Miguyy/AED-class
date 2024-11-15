from PIL import Image, ImageOps

def imageMoldura(input_image_path):
    image = Image.open(input_image_path)
    moldura_color = (255, 0, 255) 
    moldura_size = 20 
    image_com_moldura = ImageOps.expand(image, border=moldura_size, fill=moldura_color)
    image_com_moldura.show()
    return image_com_moldura

imageMoldura("AED/RSF7/images/img1.jpg")

