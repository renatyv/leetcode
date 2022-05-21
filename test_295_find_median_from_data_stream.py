import heapq


class MedianFinder:
    class _MinHeap:
        def __init__(self):
            self._heap = []
            heapq.heapify(self._heap)
            self._len = 0

        def __len__(self):
            return self._len

        def push(self, num: int):
            heapq.heappush(self._heap, num)
            self._len += 1

        def pop(self) -> int:
            self._len -= 1
            return heapq.heappop(self._heap)

        def min(self) -> int:
            return self._heap[0]

        def __str__(self):
            return ','.join(str(x) for x in heapq.nsmallest(self._len, self._heap))

    class _MaxHeap:
        def __init__(self):
            self._min_heap = MedianFinder._MinHeap()

        def push(self, num: int):
            self._min_heap.push(-num)

        def pop(self) -> int:
            return -self._min_heap.pop()

        def max(self) -> int:
            return -self._min_heap.min()

        def __len__(self):
            return len(self._min_heap)

        def __str__(self):
            return str(self._min_heap).replace('-', '')

    def __init__(self):
        self._min_heap = MedianFinder._MinHeap()
        self._max_heap = MedianFinder._MaxHeap()

    def addNum(self, num: int) -> None:
        if not self._min_heap:
            self._min_heap.push(num)
            return
        if num > self.findMedian():
            self._min_heap.push(num)
            while len(self._min_heap) > len(self._max_heap):
                popped = self._min_heap.pop()
                self._max_heap.push(popped)
        else:
            self._max_heap.push(num)
            while len(self._max_heap) > len(self._min_heap):
                popped = self._max_heap.pop()
                self._min_heap.push(popped)

    def findMedian(self) -> float:
        if len(self._min_heap) == len(self._max_heap):
            return (self._min_heap.min() + self._max_heap.max()) / 2
        if len(self._max_heap) > len(self._min_heap):
            return self._max_heap.max()
        else:
            return self._min_heap.min()


def test_case_1():
    median_finder = MedianFinder()
    median_finder.addNum(1)
    assert median_finder.findMedian() == 1
    median_finder.addNum(2)
    assert median_finder.findMedian() == 1.5
    median_finder.addNum(3)
    assert median_finder.findMedian() == 2


def test_case_2():
    median_finder = MedianFinder()
    median_finder.addNum(0)
    median_finder.addNum(-1)
    median_finder.addNum(-2)
    assert median_finder.findMedian() == -1


def test_case_3():
    median_finder = MedianFinder()
    median_finder.addNum(0)
    median_finder.addNum(1)
    median_finder.addNum(2)
    assert median_finder.findMedian() == 1


def test_case_4():
    median_finder = MedianFinder()
    median_finder.addNum(0)
    median_finder.addNum(2)
    assert median_finder.findMedian() == 1


def test_case_5():
    median_finder = MedianFinder()
    median_finder.addNum(1)
    median_finder.addNum(2)
    assert median_finder.findMedian() == 1.5
