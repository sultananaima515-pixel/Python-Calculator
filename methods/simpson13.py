import math

def simpson_one_third(expr, a, b, n):

    expr = expr.replace("^", "**")
    expr = expr.replace("sinx", "sin(x)")
    expr = expr.replace("cosx", "cos(x)")
    expr = expr.replace("tanx", "tan(x)")
    expr = expr.replace("expx", "exp(x)")
    expr = expr.replace("logx", "log(x)")
    expr = expr.replace("sqrtx", "sqrt(x)")

    def f(x):
        return eval(expr, {"__builtins__": {}}, {
            "x": x,
            "math": math,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "exp": math.exp,
            "log": math.log,
            "sqrt": math.sqrt,
            "pi": math.pi,
            "e": math.e,
        })

    if n % 2 != 0:
        return "Error: n must be even", None

    h = (b - a) / n

    log = []
    log.append("===== Simpson's 1/3 Rule =====\n")

    log.append(f"h = (b - a) / n = ({b} - {a}) / {n} = {h}\n")

    log.append("i\t x\t\t f(x)")
    log.append("-" * 40)

    total = f(a) + f(b)

    x_vals = [a + i * h for i in range(n + 1)]
    f_vals = [f(x) for x in x_vals]

    for i in range(n + 1):
        log.append(f"{i}\t {x_vals[i]:.6f}\t {f_vals[i]:.6f}")

    for i in range(1, n):
        if i % 2 == 0:
            total += 2 * f_vals[i]
        else:
            total += 4 * f_vals[i]

    result = (h / 3) * total

    log.append("\nFormula:")
    log.append("∫ f(x) dx ≈ (h/3)[f(x0) + f(xn)")
    log.append("        + 4(f(x1) + f(x3) + ...)")
    log.append("        + 2(f(x2) + f(x4) + ...)]")

    odd_terms = [f_vals[i] for i in range(1, n, 2)]
    even_terms = [f_vals[i] for i in range(2, n, 2)]

    log.append("\nSubstitution:")
    log.append(f"= (h/3)[{f_vals[0]} + {f_vals[n]}")
    log.append(f"      + 4({'+'.join(f'{v}' for v in odd_terms) if odd_terms else '0'})")
    log.append(f"      + 2({'+'.join(f'{v}' for v in even_terms) if even_terms else '0'})]")

    log.append("\nFinal Result:")
    log.append(f"Integral ≈ {result}")

    return "\n".join(log), result