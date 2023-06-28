# QR code save in python vs code folder in text name.
import qrcode
qr=qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)
data="https://www.instagram.com/piyushchirote/"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
img.save('text.png')