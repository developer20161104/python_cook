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
