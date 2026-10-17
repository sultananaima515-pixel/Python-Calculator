def calculate_errors(true_value, approx_value):

    absolute_error = abs(
        true_value - approx_value
    )

    relative_error = (
            absolute_error /
            abs(true_value)
    )

    percentage_error = (
            relative_error * 100
    )

    log = []

    log.append(
        f"True Value = {true_value}"
    )

    log.append(
        f"Approximate Value = {approx_value}"
    )

    log.append("")

    log.append(
        f"Absolute Error = {absolute_error}"
    )

    log.append(
        f"Relative Error = {relative_error}"
    )

    log.append(
        f"Percentage Error = {percentage_error}%"
    )

    return (
        "\n".join(log),
        absolute_error,
        relative_error,
        percentage_error
    )