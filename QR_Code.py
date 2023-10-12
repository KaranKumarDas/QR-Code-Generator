import pyqrcode
import png
from pyqrcode import QRCode

QRstring= input('Input Your Link to generate QR CODE :--> ')
url=pyqrcode.create(QRstring)
url.png('QR.png', scale = 8)