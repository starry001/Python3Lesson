'Python图片转字符画'
from PIL import Image

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


def get_char(r, g, b, algha=256):
    if algha == 0:
        return ""
    length = len(ascii_char)

    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1) / length
    return ascii_char[int(gray / unit)]


if __name__ == '__main__':
    im = Image.open('img.png')
    im = im.resize((im.width, im.height), Image.NEAREST)

    txt = ''
    for i in range(80):
        for j in range(80):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'

    print('txt', txt)
    with open("output.txt", 'w') as f:
        f.write(txt)
