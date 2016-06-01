from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

'''
namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。
'''
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(isinstance(p, tuple))
print(isinstance(p, Point))

'''
使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。
'''
deq = deque(['x', 'y', 'y'])
deq.append('z')
print(deq)
deq.appendleft('a')
print(deq)

'''
使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
'''
dict = defaultdict(lambda: 'N/A')
dict['a'] = 'key'
print(dict['b'])

'''
使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
如果要保持Key的顺序，可以用OrderedDict
OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
'''
dd = (('a', 1), ('b', 2), ('c', 3))
print(dd)  # dict的Key是无序的
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)


# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：

class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        # 调用父类的构造函数，下面要用到父类的__setitem__
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        # containsKey=1时表示key已存在，则执行修改操作
        # containsKey=0时表示key不存在，则执行添加操作
        containsKey = 1 if key in self else 0
        # 当已达最大容量，当新加key不存在时，会运行这段，先删除最先添加的
        # 当key存在时，不会运行这段，会运行第2个if进行修改
        if len(self) - containsKey >= self._capacity:
            # popitem移除键值对并返回，last=true时按LIFO顺序返回
            # last=false时按FIFO顺序返回
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        # 调用父类的__setitem__方法写入键值对
        OrderedDict.__setitem__(self, key, value)


lo = LastUpdatedOrderedDict(3)
lo['1'] = 1
lo['2'] = '2'
lo[3] = True
print(lo)
lo[4] = 'a'
print(lo)

'''
Counter是一个简单的计数器，例如，统计字符出现的个数：
Counter实际上也是dict的一个子类
'''
c = Counter()
for i in 'programming':
    c[i] = c[i] + 1
print(c)
