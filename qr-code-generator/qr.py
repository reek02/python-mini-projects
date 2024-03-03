import qrcode as qr
img = qr.make("https://www.facebook.com/reekparnasenphotography")
img.save("new_qrcode.png")
