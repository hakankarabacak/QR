import imp


from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open("TARGET QR PATH")

result = decode(img)

print(result)
