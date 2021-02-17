import pyqrcode
import png 
from pyqrcode import QRCode

s = "https://github.com/ovictorjo"

url = pyqrcode.create(s)

url.png('myqr.png',scale=6)


