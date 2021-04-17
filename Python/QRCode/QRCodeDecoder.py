import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

na = input("Enter the Image Name :")
d = decode(Image.open(na+".jpg"))
print("Decoding the QRCODE...\n")
print("---------------------------------------------")
print(d,"\n")
print("---------------------------------------------")
print(d[0].data.decode("ascii"))
