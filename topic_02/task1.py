def discriminant(a, b, c):
    return b ** 2 - 4 * a * c


def roots(a, b, c):
    D = discriminant(a, b, c)

    if D > 0:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        print("x1 =", x1)
        print("x2 =", x2)

    elif D == 0:
        x = -b / (2 * a)
        print("x =", x)

    else:
        print("Дійсних коренів немає")


a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
c = float(input("Введіть c: "))

roots(a, b, c)