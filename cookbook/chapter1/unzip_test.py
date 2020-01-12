from collections import deque

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


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