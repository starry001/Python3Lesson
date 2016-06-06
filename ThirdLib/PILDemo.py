from PIL import Image, ImageFilter, ImageDraw, ImageFont
import random

# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('test.jpg')
# 获得图像尺寸:
w, h = im.size
print('Original image size: %s x %s' % (w, h))
# 缩放到50%:
im.thumbnail((w / 2, h / 2))
print('Resize image to: %s x %s' % (w / 2, h / 2))
# 把缩放后的图像用jpeg格式保存:
im.save('thumbnail.jpg', 'jpeg')

# 模糊滤镜
im = Image.open('test.jpg')
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'JPEG')


def rndChar():
    return chr(random.randint(65, 90))


def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


width = 60 * 4
hight = 60
image = Image.new('RGB', (width, hight), (255, 255, 255))
# 创建字体对象
font = ImageFont.truetype('c:/Windows/Fonts/Arial.ttf', 36)
# 创建draw对象
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(hight):
        draw.point((x, y), fill=rndColor())

for x in range(4):
    draw.text((10 + 60 * x, 10), rndChar(), fill=rndColor2(), font=font, )
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
