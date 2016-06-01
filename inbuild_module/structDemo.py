import struct

# 在Python中，比方说要把一个32位无符号整数变成字节，也就是4个长度的bytes，你得配合位运算符这么写：
n = 10240099  # 0x9c4063
b1 = (n & 0xff000000) >> 24
print(b1)
b2 = (n & 0xff0000) >> 16
print(b2)
b3 = (n & 0xff00) >> 8
print(b3)
b4 = n & 0xff
print(b4)
bs = bytes([b1, b2, b3, b4])
print(bs)

'''
0
156
64
99
b'\x00\x9c@c'
'''

'''
Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换。
struct的pack函数把任意数据类型变成bytes：
'''
b = struct.pack('>I', 10240099)
print(b)  # b'\x00\x9c@c'

'''
pack的第一个参数是处理指令，'>I'的意思是：
>表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
后面的参数个数要和处理指令一致。
unpack把bytes变成相应的数据类型：
'''

s = struct.unpack('>I', b'\x00\x9c@c')
print(s)
'''
根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。
所以，尽管Python不适合编写底层操作字节流的代码，但在对性能要求不高的地方，利用struct就方便多了。
'''
print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))

'''
BMP格式采用小端方式存储数据，文件头的结构按顺序如下：
两个字节：'BM'表示Windows位图，'BA'表示OS/2位图；
一个4字节整数：表示位图大小；
一个4字节整数：保留位，始终为0；
一个4字节整数：实际图像的偏移量；
一个4字节整数：Header的字节数；
一个4字节整数：图像宽度；
一个4字节整数：图像高度；
一个2字节整数：始终为1；
一个2字节整数：颜色数。
所以，组合起来用unpack读取
'''

with open('../a2.bmp', 'rb') as f:
    c = f.read()
    # print(c)
    r = struct.unpack('<ccIIIIIIHH', c[:30])
    print(r)  # (b'B', b'M', 964662, 0, 54, 40, 512, 628, 1, 24)


# 请编写一个bmpinfo.py，可以检查任意文件是否是位图文件，如果是，打印出图片大小和颜色数。
def isBmpfile(file):
    try:
        with open(file, 'rb') as f:
            try:
                r = struct.unpack('<ccIIIIIIHH', f.read(30))
                if isinstance(r, tuple):
                    if r[0] == b'B' and r[1] == b'M':
                        print('is Windows bmp')
                        print('bmp size is ', r[2])
                        print('bmp color number is ', r[9])

                    elif r[0] == b'B' and r[1] == b'A':
                        print('is OS/2 bmp')
                        print('bmp size is ', r[2])
                        print('bmp color number is ', r[9])
                    else:
                        print('unknow type bmp')
            except TypeError as e:
                print('is not a bmp')
    except FileNotFoundError as e:
        print('file not found', e)


filePath = '../a2.bmp'
isBmpfile(filePath)
