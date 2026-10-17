def gaussian_naive(matrix):

    n = len(matrix)

    mat = [row[:] for row in matrix]

    log = []

    log.append("GAUSSIAN ELIMINATION")
    log.append("=" * 40)

    for k in range(n - 1):

        log.append(f"\nIteration {k+1}")

        for i in range(k + 1, n):

            if mat[k][k] == 0:
                return "Zero Pivot Error", None

            factor = mat[i][k] / mat[k][k]

            log.append(
                f"R{i+1} = R{i+1} - ({factor:.4f})R{k+1}"
            )

            for j in range(k, n + 1):
                mat[i][j] -= factor * mat[k][j]

        log.append("\nMatrix:")

        for row in mat:
            log.append(
                " ".join(f"{x:8.4f}" for x in row)
            )

    x = [0.0] * n

    x[n - 1] = mat[n - 1][n] / mat[n - 1][n - 1]

    for i in range(n - 2, -1, -1):

        s = 0

        for j in range(i + 1, n):
            s += mat[i][j] * x[j]

        x[i] = (mat[i][n] - s) / mat[i][i]

    return "\n".join(log), x