import qrcode
import zpl

data = '00_PRODUCT_TYPE_VERSION'

l = zpl.Label(30, 50)
height = 0
char = 8

while (char * len(data)) / 2 >= l.width:
    char -= 1

l.origin(0, l.height - char)
l.write_text(data, char_height=char, char_width=char, line_width=l.width, justification='C')
l.endorigin()

qr = qrcode.QRCode(box_size=10, border=1)
qr.add_data(data)
qr.make(fit=False)
img = qr.make_image()
l.origin((l.width-img.width)/2, height)
image_height = l.write_graphic(img, img.width, height=0)
l.endorigin()

print(l.dumpZPL())
l.preview()
