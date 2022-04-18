
def matrixReshape(mat: list[list[int]], reshaped_nrows: int, reshaped_ncols: int) -> list[list[int]]:
    mat_nrows, mat_ncols = len(mat), len(mat[0])
    if mat_nrows*mat_ncols != reshaped_nrows*reshaped_ncols:
        return mat
    if mat_nrows == reshaped_nrows and mat_ncols == reshaped_ncols:
        return mat
    reshaped_matrix = []
    for row_n in range(reshaped_nrows):
        row = []
        for i in range(reshaped_ncols):
            row.append(0)
        reshaped_matrix.append(row)
    for reshaped_row in range(reshaped_nrows):
        for reshaped_col in range(reshaped_ncols):
            mat_r, mat_c = get_mat_row_col_from_reshaped(reshaped_row, reshaped_col,
                                                         reshaped_ncols,
                                                         mat_nrows, mat_ncols)
            reshaped_matrix[reshaped_row][reshaped_col] = mat[mat_r][mat_c]
    return reshaped_matrix


def get_mat_row_col_from_reshaped(reshaped_row, reshaped_col, reshaped_ncols, mat_nrows, mat_ncols):
    """converts: reshaped index -> flattened index-> mat index"""
    flattened_index = reshaped_row * reshaped_ncols + reshaped_col
    mat_r = flattened_index // mat_ncols
    mat_c = flattened_index % mat_ncols
    return mat_r, mat_c


def test_index_concerter():
    assert get_mat_row_col_from_reshaped(0, 0, 3, 2, 2) == (0, 0)
    assert get_mat_row_col_from_reshaped(0, 2, 4, 2, 2) == (1, 0)
    assert get_mat_row_col_from_reshaped(1, 0, 2, 1, 4) == (0, 2)
    assert get_mat_row_col_from_reshaped(2, 2, 3, 3, 3) == (2, 2)
    assert get_mat_row_col_from_reshaped(1, 2, 3, 3, 2) == (2, 1)


def test_matrixReshape_example_1():
    assert matrixReshape([[1,2],[3,4]], 1, 4) == [[1,2,3,4]]


def test_matrixReshape_example_2():
    assert matrixReshape([[1,2],[3,4]], 2, 4) == [[1,2],[3,4]]


def test_matrixReshape_edgecases():
    assert matrixReshape([[1]], 1, 1) == [[1]]
    assert matrixReshape([[1]], 2, 1) == [[1]]
    assert matrixReshape([[1]], 1, 2) == [[1]]
    assert matrixReshape([[1,2],[3,4]], 2, 2) == [[1,2],[3,4]]
    assert matrixReshape([[1, 2], [3, 4]], 1, 2) == [[1, 2], [3, 4]]
    assert matrixReshape([[1, 2], [3, 4]], 2, 3) == [[1, 2], [3, 4]]


def test_matrixReshape_1():
    assert matrixReshape([[1,2],[3,4]], 4, 1) == [[1],[2],[3],[4]]
    assert matrixReshape([[1], [2], [3], [4]], 2, 2) == [[1, 2], [3, 4]]
    assert matrixReshape([[1], [2], [3], [4], [5]], 1, 5) == [[1,2,3,4,5]]
    assert matrixReshape([[1, 2, 3, 4, 5]], 5, 1) == [[1], [2], [3], [4], [5]]
    assert matrixReshape([[1,2], [3,4], [5,6]], 2, 3) == [[1,2,3],[4,5,6]]
    assert matrixReshape([[1, 2, 3], [4, 5, 6]], 3, 2) == [[1, 2], [3, 4], [5, 6]]


