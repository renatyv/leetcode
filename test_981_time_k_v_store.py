class TimeMap:

    def __init__(self):
        # dict key -> sorted list of pairs (timestamp, value)
        self.timestamped_map: dict[str, list[tuple[int, str]]] = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        """Stores the key key with the value value at the given time timestamp."""
        if key not in self.timestamped_map:
            self.timestamped_map[key] = [(timestamp, value)]
        else:
            self.timestamped_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        """ Returns a value such that set was called previously, with timestamp_prev <= timestamp.
        If there are multiple such values, it returns the value associated with the largest timestamp_prev.
        If there are no values, it returns "".
        Idea: simple binary search"""
        if key not in self.timestamped_map:
            return ''
        values = self.timestamped_map[key]
        if timestamp >= values[-1][0]:
            return values[-1][1]
        if timestamp < values[0][0]:
            return ''
        left = 0
        right = len(values) - 1
        while left + 1 < right:
            pivot = left + (right - left) // 2
            pivot_timestamp, val = values[pivot]
            if timestamp == pivot_timestamp:
                return val
            if timestamp < pivot_timestamp:
                right = pivot
            else:
                left = pivot
        return values[left][1]


def test_edge_cases():
    timeMap = TimeMap()
    assert timeMap.get('foo', 1) == ''
    timeMap.set('foo', 'bar', 1)
    timeMap.set('foo', 'bar4', 4)
    timeMap.set('foo', 'bar7', 7)
    assert timeMap.get('foo', 0) == ''
    assert timeMap.get('foo', 2) == 'bar'
    assert timeMap.get('foo', 4) == 'bar4'
    assert timeMap.get('foo', 5) == 'bar4'
    assert timeMap.get('foo', 7) == 'bar7'
    assert timeMap.get('foo', 12) == 'bar7'


def test_examples():
    # ["TimeMap", "set", "get", "get", "set", "get", "get"]
    # [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
    # [null, null, "bar", "bar", null, "bar2", "bar2"]
    timeMap = TimeMap()
    timeMap.set('foo', 'bar', 1)
    assert timeMap.get('foo', 1) == 'bar'
    assert timeMap.get('foo', 3) == 'bar'
    timeMap.set('foo', 'bar2', 4)
    assert timeMap.get('foo', 4) == 'bar2'
    assert timeMap.get('foo', 5) == 'bar2'
