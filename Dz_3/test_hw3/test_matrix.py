from Dz_3.matrix_v2 import Matrix
import pytest



@pytest.mark.parametrize("matrix1, matrix2, exepted_matrix",
[
    (
        [[1, 1, 1], [1, 1, 1]],
        [[1, 1, 1], [1, 1, 1]],
        [[2, 2, 2], [2, 2, 2]]
    ),
    (
        [[], []],
        [[], []],
        [[], []]
    ),
    (
        [[12], [12]],
        [[1], [1]],
        [[13], [13]]
    )
])
def test_matrix_for_add(matrix1, matrix2, exepted_matrix):
    assert (Matrix(matrix1) + Matrix(matrix2)).matrix_data() == Matrix(exepted_matrix).matrix_data()


@pytest.mark.parametrize("matrix1, matrix2, exepted_matrix",
[
    (
        [[1, 1, 1], [1, 1, 1]],
        [[1, 1, 1], [1, 1, 1]],
        [[0, 0, 0], [0, 0, 0]]
    ),
    (
        [[], []],
        [[], []],
        [[], []]
    ),
    (
        [[12], [12]],
        [[1], [1]],
        [[11], [11]]
    )
])
def test_matrix_for_sub(matrix1, matrix2, exepted_matrix):
    assert (Matrix(matrix1) - Matrix(matrix2)).matrix_data() == Matrix(exepted_matrix).matrix_data()


@pytest.mark.parametrize("matrix, value, exepted_matrix",
[
    (
        [[1, 1, 1], [1, 1, 1]],
        2,
        [[2, 2, 2], [2, 2, 2]]
    ),
    (
        [[1], [1]],
        5,
        [[5], [5]]
    ),
    (
        [[12], [12]],
        3,
        [[36], [36]]
    )
])
def test_matrix_for_mul(matrix1, value, exepted_matrix):
    assert (Matrix(matrix1) * value).matrix_data() == Matrix(exepted_matrix).matrix_data()
