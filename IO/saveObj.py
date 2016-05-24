import pickle

'''
保存数据到本地，序列化
'''
# d = dict(age=1, name='Bob', sex=1)
# f = open('save.txt', 'wb')
# pickle.dump(d, f)

# 读取本地数据，反序列化
f = open('save.txt', 'rb')
d = pickle.load(f)
print(d)
