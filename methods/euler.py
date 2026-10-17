import math

def euler_method(expr, x0, y0, h, xn):

    expr = expr.replace("^", "**")
    expr = expr.replace("sinx", "sin(x)")
    expr = expr.replace("cosx", "cos(x)")
    expr = expr.replace("tanx", "tan(x)")
    expr = expr.replace("expx", "exp(x)")
    expr = expr.replace("logx", "log(x)")
    expr = expr.replace("sqrtx", "sqrt(x)")

    def f(x, y):
        return eval(expr, {"__builtins__": {}}, {
            "x": x,
            "y": y,
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

    log = []
    steps = []

    x = x0
    y = y0
    step = 0

    log.append("===== Euler Method =====\n")
    log.append("Step\t x\t\t y")

    while x <= xn + 1e-10:

        steps.append((step, x, y))

        log.append(f"{step}\t {x:.4f}\t {y:.6f}")

        if x >= xn:
            break

        y = y + h * f(x, y)
        x = x + h
        step += 1

    log.append("\nFinal Result:")
    log.append(f"y({xn}) ≈ {y}")

    return "\n".join(log), steps, y