
def generate(numRows: int) -> list[list[int]]:
    """generate n rows of pascal's triangle"""
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1], [1,1]]
    rows = [[1], [1,1]]
    for nrow in range(2, numRows):
        prev_row = rows[-1]
        row = [1]
        for col in range(len(prev_row)-1):
            row.append(prev_row[col]+prev_row[col+1])
        row.append(1)
        rows.append(row)
    return rows


def test_generate():
    assert generate(1) == [[1]]
    assert generate(2) == [[1], [1, 1]]
    assert generate(3) == [[1], [1, 1], [1, 2, 1]]
    assert generate(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    assert generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6,4, 1]]
