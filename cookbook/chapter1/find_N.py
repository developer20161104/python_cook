import heapq
import random


# 使用heap来实现优先队列，构建的为小堆
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # 自动对关键字参数从头排序
        # 因此，当优先级相同时，按照插入时间来排序
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def __repr__(self):
        # 修改对于实例的输出
        return str(self._queue)


if __name__ == '__main__':
    # 生成指定范围的随机列表
    nums = random.sample(range(1, 42), 10)

    print(nums)
    print(heapq.nlargest(3, nums))
    print(heapq.nsmallest(3, nums))

    portfolio = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]

    # 结合lambda表达式来设置关键字比较
    print(heapq.nlargest(3, portfolio, lambda x: x['shares']))

    # 在选取元素后结合生成表达式输出指定关键字
    print([x['name'] for x in heapq.nsmallest(3, portfolio, lambda x: x['price'])])

    # 对于优先队列的使用
    q = PriorityQueue()
    q.push('foo', 1)
    q.push('bar', 5)
    q.push('spam', 4)
    q.push('grok', 1)

    print(q)
    print(q.pop())