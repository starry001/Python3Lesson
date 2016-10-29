'根据图片改变url地址、转换字符串、字符识别'
import string

text = """g fmnc wms bgblr rpylqjyrc gr zw fylb.rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

o = ''
for each in text:
    # ython中提供函数ord()将字母转换成ASCII码，提供函数chr()将相对应的ASCII码转化为字母
    if ord(each) >= ord('a') and ord(each) <= ord('z'):
        o += chr((ord(each) + 2 - ord('a')) % 26 + ord('a'))
    else:
        o += each
print(o)
"""output : i hope you didnt translate it by hand.thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url."""


# 2.x:string.maketrans     3.x:str.maketrans
def std_solution(text):
    table = str.maketrans(string.ascii_lowercase,
                          string.ascii_lowercase[2:] + string.ascii_lowercase[:2])
    print(str.translate(text, table))


std_solution(text)
