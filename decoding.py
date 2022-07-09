import imp


from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open("TARGET QR")

result = decode(img)

print(result)