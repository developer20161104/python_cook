if __name__ == '__main__':
    # 1.11 命名切片
    record = '....................100 .......513.25 ..........'

    # 定义命名切片来提取固定位置字段，尽量避免硬编码下标
    # slice(start, stop, step)
    SHARES = slice(20, 23)

    PRICE = slice(31, 37)

    print(int(record[SHARES]) * float(record[PRICE]))

    # 创建命名切片来进行测试
    a = slice(1, 60, 2)

    s = 'helloworld'

    # 使用 indices 将当前切片映射到指定长度当中
    # 即修改结束位置
    print(a.indices(len(s)))

    # 并且需要注意的是，indices 并非在原切片上修改，因此需要进行接受
    # 此处为将切片解压给 range 函数来进行后续处理
    for i in range(*a.indices(len(s))):
        print(s[i], end='\t')
    print()

    # 1.12 统计序列中出现次数最多的元素
    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
        'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
        'my', 'eyes', "you're", 'under'
    ]

    from collections import Counter

    # 实质为构建一个字典
    word_count = Counter(words)
    print(word_count)
    # 统计出现最多的前n个元素
    print(word_count.most_common(3))

    # 作集合的计算时，注意Counter对象与字典本身的区别
    # 字典是不能进行简单数学计算的
    """
    # error
    other = {'eyes': 1, 'looking': 1, 'are': 1, 'in': 1, 'not': 1, 'you': 1, 'my': 1, 'why': 1}
    test = {'eyes': 8, 'the': 5, 'look': 4, 'into': 3, 'my': 3, 'around': 2, 'not': 1, "don't": 1, "you're": 1, 'under': 1}
    print(other + test)"""

    # correct
    other = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
    print(Counter(other) + word_count)
