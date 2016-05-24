from PIL import Image
import  sys

im = Image.open('test.jpg')
print(im.format, im.size, im.mode)
im.thumbnail((375,667))
im.save('new.jpg', 'JPEG')

print(sys.path)
sys.path.append('/Users/michael/my_py_scripts')
print(sys.path)
