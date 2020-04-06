import numpy as np


def decorate_matrix(n):
    matrix = np.zeros((n, n))
    matrix[0] = 1
    matrix[-1] = 1
    matrix[:, 0] = 1
    matrix[:, -1] = 1
    return matrix
    pass


def main():
    print(str(decorate_matrix(4)))


if __name__ == '__main__':
    main()
