from collections import deque
import random

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


# 在过滤重复元素的同时维持初始顺序不变
def order_set(items):
    seen = set()
    for item in items:
        if item not in seen:
            # 生成有序组
            yield item
            # 在保留了未加入元素后将其添加到set中用于后续判断
            seen.add(item)


def order_dict(items, key=None):
    seen = set()
    for item in items:
        # val 为经过hashable转化的值，因此只能拿来比较，而不是存储
        # key 为一个函数的指向符
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


if __name__ == '__main__':
    # 根据不同内容进行解压，星号表达式将多余的保存为一个列表
    for tag, *args in records:
        if tag == 'foo':
            do_foo(*args)
        else:
            do_bar(*args)

    # 字符串分割
    line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
    uname, *fields, homedir, sh = line.split(':')

    print("\t".join([uname, homedir, sh]))

    # deque的使用
    q = deque(maxlen=2)
    q.append(1)
    q.append(2)

    # 当q中元素已满时，插入会自动去除最先放入q中的元素
    # 因此可以实现保留最后N条记录的功能
    q.append(3)

    print(q)

    # 对字典进行一些计算操作
    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }

    # zip 函数的妙用：类似于将二维数组进行转置操作
    # 此处为将 key 与 value 一一对应的同时，进行一些关联操作
    print(max(zip(prices.keys(), prices.values())))
    # output ('IBM', 205.55) 由键来起始化顺序

    # 但是需要注意的是，zip迭代器只能被访问一次
    test = zip(prices.keys(), prices.values())

    print(min(test))
    # 此时会报错
    # print(max(test))

    # 1.10删除序列相同元素并保持顺序
    list_a = [1] * 4 + [2, 1, 3] + [5, 10]
    # 初始化列表并将顺序打乱
    random.shuffle(list_a)

    # 结果检验
    print(list_a)
    print(list(order_set(list_a)))

    # 测试字典虑重
    a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]

    # 采用 x 位的value作为判断
    print(list(order_dict(a, key=lambda d: d['x'])))