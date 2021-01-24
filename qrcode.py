import qrcode
import image

def make_qr(filename, msg):
    img = qrcode.make(msg)
    img.save(filename)
    img.show()

make_qr("myQRCODE.png","https://github.com/Ktechen")
