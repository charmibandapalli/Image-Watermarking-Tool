from PIL import Image, ImageDraw, ImageFont

def add_watermark(input_image, text):
    img = Image.open(input_image)
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    draw.text((10,10), text, fill="white", font=font)
    img.save("watermarked.png")

add_watermark("image.jpg", "My Watermark")
