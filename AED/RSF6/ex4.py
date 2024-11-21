from PIL import Image

def imageGrayScale(input_image_path):
    image = Image.open(input_image_path)
    width, height = image.size
    grayscale_image = Image.new("L", (width, height))
    for x in range(width):
        for y in range(height):
            red, green, blue = image.getpixel((x, y))
            gray = int(0.299 * red + 0.587 * green + 0.114 * blue)
            grayscale_image.putpixel((x, y), gray)
    grayscale_image.show()
imageGrayScale("AED/RSF6/images/img1.jpg")