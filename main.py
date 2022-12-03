import qrcode
import zpl
import socket


def main(height, width, data, preview=False):
    l = zpl.Label(height, width)
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
    l.origin((l.width - img.width) / 2, height)
    l.write_graphic(img, img.width, height=0)
    l.endorigin()

    if preview:
        l.preview()
    return l.dumpZPL()


if __name__ == '__main__':
    data = '00_PRODUCT_TYPE_VERSION'
    dump = main(30, 50, data)
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "IP"
    port = 9100
    try:
        mysocket.connect((host, port))  # connecting to host
        mysocket.send(dump)  # using bytes
        mysocket.close()  # closing connection
    except:
        print("Error with the connection")
