import re
import operator

priority = {"+": 1, "-": 1, "*": 2, "/": 2, "u-": 3, "u+": 3, "^": 4}
operations = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "^": operator.pow
}


def to_rpn(expression):
    expression = re.sub(r"\s+", "", expression)
    tokens = re.findall(r"\d+(?:\.\d+)?|[()+\-*/^]", expression)

    if "".join(tokens) != expression:
        raise ValueError("Недопустимий символ")

    output = []
    stack = []
    previous = "start"

    for token in tokens:
        if token[0].isdigit():
            if previous in ("number", ")"):
                raise ValueError("Неправильний вираз")
            output.append(token)
            previous = "number"

        elif token == "(":
            if previous in ("number", ")"):
                raise ValueError("Неправильний вираз")
            stack.append(token)
            previous = "("

        elif token == ")":
            if previous not in ("number", ")"):
                raise ValueError("Неправильний вираз")
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            if not stack:
                raise ValueError("Неправильні дужки")
            stack.pop()
            previous = ")"

        else:
            if token in "+-" and previous in ("start", "operator", "("):
                stack.append("u" + token)
                previous = "operator"
                continue

            if previous not in ("number", ")"):
                raise ValueError("Неправильний вираз")

            while stack and stack[-1] != "(":
                top = stack[-1]
                if priority[top] > priority[token] or (
                    priority[top] == priority[token] and token != "^"
                ):
                    output.append(stack.pop())
                else:
                    break

            stack.append(token)
            previous = "operator"

    if previous not in ("number", ")"):
        raise ValueError("Незавершений вираз")

    while stack:
        if stack[-1] == "(":
            raise ValueError("Неправильні дужки")
        output.append(stack.pop())

    return output


def calculate_rpn(tokens):
    stack = []

    for token in tokens:
        if token not in priority:
            stack.append(float(token))
        elif token in ("u-", "u+"):
            if not stack:
                raise ValueError("Неправильний вираз")
            value = stack.pop()
            stack.append(-value if token == "u-" else value)
        else:
            if len(stack) < 2:
                raise ValueError("Недостатньо операндів")
            b = stack.pop()
            a = stack.pop()
            stack.append(operations[token](a, b))

    if len(stack) != 1:
        raise ValueError("Неправильний вираз")

    return stack[0]


while True:
    expression = input("\nВведіть вираз (або exit): ")

    if expression.lower().strip() == "exit":
        break

    try:
        rpn = to_rpn(expression)
        result = calculate_rpn(rpn)

        print("Зворотний польський запис:", " ".join(rpn))
        print("Результат:", result)

    except (ValueError, ZeroDivisionError, OverflowError) as error:
        print("Помилка:", error)
