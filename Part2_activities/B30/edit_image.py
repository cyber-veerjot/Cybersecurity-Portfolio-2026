from PIL import Image, PngImagePlugin

img = Image.open("watermarked.png")

# light edit: resize slightly
img = img.resize((img.width - 1, img.height - 1))

metadata = PngImagePlugin.PngInfo()
metadata.add_text("Watermark", "AI_GENERATED_WATERMARK")

img.save("edited.png", pnginfo=metadata)

print("Edited image saved with watermark preserved")