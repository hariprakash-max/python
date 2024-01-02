# import ORcode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode
# string which represents the QRcode
site="https://www.mygreatlearning.com/"
# generate QR code
url_qr=pyqrcode.create(site)
# create and save the svg file naming"myqr.svg"
# url_qr.svg("great.svg",scale=8)
# create and save the png file naming"myqr.png"
url_qr.png("great.png",scale=6)
