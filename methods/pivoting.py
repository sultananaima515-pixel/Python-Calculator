def gaussian_partial_pivot(matrix):
    n = len(matrix)
    log = []

    for i in range(n):

        # Partial Pivoting
        max_row = i
        for k in range(i + 1, n):
            if abs(matrix[k][i]) > abs(matrix[max_row][i]):
                max_row = k

        if max_row != i:
            matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
            log.append(f"R{i+1} <--> R{max_row+1}")

        # Elimination
        for j in range(i + 1, n):
            factor = matrix[j][i] / matrix[i][i]

            for k in range(i, n + 1):
                matrix[j][k] -= factor * matrix[i][k]

            log.append(
                f"R{j+1} = R{j+1} - ({factor:.4f})R{i+1}"
            )

    # Back Substitution
    x = [0] * n

    for i in range(n - 1, -1, -1):
        x[i] = matrix[i][n]

        for j in range(i + 1, n):
            x[i] -= matrix[i][j] * x[j]

        x[i] /= matrix[i][i]

    return "\n".join(log), x