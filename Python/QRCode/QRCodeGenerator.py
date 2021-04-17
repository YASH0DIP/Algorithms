#import sys
#import os
import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

name = input("Enter the Data :")
qr = pyqrcode.create(name)
qr.png(name+".jpg", scale=8)

print("QR Code Created Succesfully.\n")

#path = "C:/#Programming/Programs/Python/QRCode/"
#mode = 0o666
#flags = os.O_RDWR
#fd = os.open(path, flags, mode)
