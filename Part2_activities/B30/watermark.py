from PIL import Image, PngImagePlugin

img = Image.open("original_B30.png")

metadata = PngImagePlugin.PngInfo()
metadata.add_text("Watermark", "AI_GENERATED_WATERMARK")

img.save("watermarked.png", pnginfo=metadata)

print("Watermark added to watermarked.png")