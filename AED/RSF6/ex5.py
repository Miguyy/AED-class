from PIL import Image, ImageDraw

def addWindowFrame(input_image_path, output_image_path, frame_color=(0, 0, 255), frame_thickness=10):
    image = Image.open(input_image_path)
    width, height = image.size

    draw = ImageDraw.Draw(image)

    mid_x = width // 2
    mid_y = height // 2

    draw.rectangle([(mid_x - frame_thickness // 2, 0), 
                    (mid_x + frame_thickness // 2, height)], 
                   fill=frame_color)

    draw.rectangle([(0, mid_y - frame_thickness // 2), 
                    (width, mid_y + frame_thickness // 2)], 
                   fill=frame_color)

    draw.rectangle([(0, 0), (width, frame_thickness)], fill=frame_color)  
    draw.rectangle([(0, 0), (frame_thickness, height)], fill=frame_color)  
    draw.rectangle([(0, height - frame_thickness), (width, height)], fill=frame_color)  
    draw.rectangle([(width - frame_thickness, 0), (width, height)], fill=frame_color)  

    image.save(output_image_path)
    print(f"Image with window frame saved as {output_image_path}")

    image.show()

input_image_path = "AED/RSF6/images/img1.jpg"
framed_output_path = "AED/RSF6/images/framed_img1.jpg"

addWindowFrame(input_image_path, framed_output_path)