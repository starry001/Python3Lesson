import unittest
from  MyDict import MyDict


class TestDict(unittest.TestCase):
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = MyDict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = MyDict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'MyDict' object has no attribute 'empty'
    '''

    def test_init(self):
        d = MyDict(a=1, b='a')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'a')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = MyDict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = MyDict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = MyDict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = MyDict()
        with self.assertRaises(AttributeError):
            value = d.empty

    # def setUp(self):
    #     print('setUp...')
    #
    # def tearDown(self):
    #     print('tearDown...')
