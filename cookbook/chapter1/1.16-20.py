if __name__ == '__main__':
    # 1.16 过滤序列元素
    # 注意区分列表推导与生成器表达式

    # 列表推导
    # 会直接占用较大内存
    mylist = [1, 4, -5, 10, -7, 2, 3, -1]
    print([n for n in mylist if n > 0])

    # 生成器表达式
    # 生成的是一个迭代器，内部为 yield ，内存消耗较小
    pos = (n for n in mylist if n > 0)

    # 输出时需要 list 来生成最终结果
    print(list(pos))

    # 1.17 字典推导: 常用与求取某个字典的子集
    # 类似于列表的推导

    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }

    # 除了括号外与列表推导基本没啥区别，应该也比较占内存
    print({key: value for key, value in prices.items() if value < 100})

    # 1.18 命名元组的使用
    from collections import namedtuple

    Stock = namedtuple('Stock', ['name', 'shares', 'prices'])

    # 测试命名元组列表
    test = [Stock('first', 10.3, 12), Stock('sec', 10.6, 30), Stock('third', 12, 41)]


    def compute_costs(records):
        total = 0.0

        for rec in records:
            s = Stock(*rec)
            # 在拥有命名元组后，可以直接用名字取代下标
            # 相比用下标表示更加清晰，并且如果在内部元素不变的情况下，字典可以考虑转化为命名元组减少开销
            total += s.shares * s.prices

        return total


    # 使用命名元组列表求得的结果
    print(compute_costs(test))

    # 1.19 生成器的使用
    dig = range(1, 10)
    # 相对于使用列表推导，使用生成器表达式来进行迭代解决更加节约空间
    print(sum(x*x for x in dig))

    portfolio = [
        {'name':'GOOG', 'shares': 50},
        {'name':'YHOO', 'shares': 75},
        {'name':'AOL', 'shares': 20},
        {'name':'SCOX', 'shares': 65}
    ]

    # 像lambda表达式来使用，但是缺点是不能全部输出

    # print(min(portfolio, key=lambda x: x['shares']))
    print(min(x['shares'] for x in portfolio))
