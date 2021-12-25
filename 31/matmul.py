from itertools import product


class Matrix(object):
    def __init__(self, values):
        self.values = values

    def __repr__(self):
        return f'<Matrix values="{self.values}">'

    def __matmul__(self, other):

        result = []
        res_row_idxs = range(len(self.values))
        res_col_idxs = range(len(other.values[0]))

        result = [[] for row in self.values]
        for res_i, res_j in product(res_row_idxs, res_col_idxs):
            row = self.values[res_i]
            col = [other_row[res_j] for other_row in other.values]
            res_v = sum((v_r * v_c for v_r, v_c in zip(row, col)))
            result[res_i].append(res_v)

        return Matrix(result)

    def __rmatmul__(self, other):
        print(f"Rultiplying: {self}, {other}")
        other_dup = Matrix(other.values)
        result = self @ other_dup
        return result

    def __imatmul__(self, other):
        result = self @ other
        self.values = result.values
        return self


if __name__ == "__main__":
    matrix_a = Matrix([[1, 2], [3, 4]])
    matrix_b = Matrix([[11, 12], [13, 14]])

    print(matrix_a)
    print(matrix_b)
    print(matrix_a @ matrix_b)
    matrix_a @= matrix_b
    print(f"In place: {matrix_a}")
