import qrcode
def gen_qrcode(value):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(value)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("C:\\Users\\arsha\\PycharmProjects\\Sqrp\\static\\qr\\a.jpg")



def gen_qrcode_2(value):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(value)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("C:\\Users\\arsha\\PycharmProjects\\Sqrp\\static\\qr\\sharea.jpg")


