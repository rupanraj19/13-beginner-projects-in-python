# convert a text or link into a qr code
# install and import the libraries needed (qrcode Image)
# create function  that collects a text and converts it into to a qrcode
# save the qr code as an image

import qrcode

def generate_qrcode(text):
   
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )

    qr.add_data(text) # add data to qr code 
    qr.make(fit = True) # make qr code
    img = qr.make_image(fill_color = "black", back_color = "white")
    img.save("qrcode.png")

url = input("Enter URL to generate qr code: ")
generate_qrcode(url)
