from PIL import Image

img = Image.open("edited.png")

print("Detected watermark:", img.info.get("Watermark"))