import numpy as np


def matrix_multiply(m, n):
    # m: i x j
    # n: j x k
    assert len(m[0]) == len(n)
    result = [[0 for _ in range(len(m))] for _ in range(len(n[0]))]
    for i in range(len(m)):
        for k in range(len(n[0])):
            for j in range(len(n)):
                result[i][k] += m[i][j] * n[j][k]

    return result


if __name__ == '__main__':
    m_ = [[0, 1, 2], [2, 1, 0]]
    n_ = [[1, 1, 1, 1], [2, 1, 0, 1], [1, 1, 1, 1]]
    m = np.array(m_)
    n = np.array(n_)
    res = np.matmul(m, n)
    res_ = matrix_multiply(m_, n_)
    assert (res == np.array(res_)).all()


