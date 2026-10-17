def lu_decomposition(matrix):

    n = len(matrix)

    # Separate coefficient matrix and RHS vector
    A = [row[:-1] for row in matrix]
    b = [row[-1] for row in matrix]

    L = [[0.0 for _ in range(n)] for _ in range(n)]
    U = [[0.0 for _ in range(n)] for _ in range(n)]

    log = []

    log.append("LU DECOMPOSITION")
    log.append("=" * 50)

    for i in range(n):

        # Upper Matrix
        for k in range(i, n):

            total = 0.0

            for j in range(i):
                total += L[i][j] * U[j][k]

            U[i][k] = A[i][k] - total

        # Lower Matrix
        for k in range(i, n):

            if i == k:
                L[i][i] = 1.0

            else:

                total = 0.0

                for j in range(i):
                    total += L[k][j] * U[j][i]

                if U[i][i] == 0:
                    return (
                        "Zero Pivot Error! LU Decomposition Failed.",
                        None,
                        None,
                        None
                    )

                L[k][i] = (A[k][i] - total) / U[i][i]

        # Iteration Log
        log.append(f"\nIteration {i + 1}")
        log.append("-" * 40)

        log.append("\nL Matrix")

        for row in L:
            log.append(
                " ".join(
                    f"{value:10.4f}"
                    for value in row
                )
            )

        log.append("\nU Matrix")

        for row in U:
            log.append(
                " ".join(
                    f"{value:10.4f}"
                    for value in row
                )
            )

    # Forward Substitution
    y = [0.0] * n

    log.append("\n")
    log.append("=" * 20)
    log.append("FORWARD SUBSTITUTION")
    log.append("=" * 20)

    for i in range(n):

        total = 0.0

        for j in range(i):
            total += L[i][j] * y[j]

        y[i] = b[i] - total

        log.append(
            f"y{i + 1} = {y[i]:.6f}"
        )

    # Back Substitution
    x = [0.0] * n

    log.append("\n")
    log.append("=" * 20)
    log.append("BACK SUBSTITUTION")
    log.append("=" * 20)

    for i in range(n - 1, -1, -1):

        total = 0.0

        for j in range(i + 1, n):
            total += U[i][j] * x[j]

        if U[i][i] == 0:
            return (
                "Zero Pivot Error! Back Substitution Failed.",
                None,
                None,
                None
            )

        x[i] = (y[i] - total) / U[i][i]

        log.append(
            f"x{i + 1} = {x[i]:.6f}"
        )

    return "\n".join(log), L, U, x