print("Digite os termos de uma equação quadrática (ax² + bx + c = 0)")
a = float(input("a: "));
b = float(input("b: "));
c = float(input("c: "));

if b < 0 and c > 0:
    print("{}x² - {}x + {} = 0".format(a, -b, c))

if b > 0 and c < 0:
    print("{}x² + {}x - {} = 0".format(a, b, -c))

if (b < 0 and c < 0):
    print("{}x² - {}x - {} = 0".format(a, -b, -c))

if (b > 0 and c > 0):
    print("{}x² + {}x + {} = 0".format(a, b, c))

import math
delta = b ** 2 - 4 * a * c

if delta < 0:
    print("Esta equação não possui raízes reais.")
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    if delta == 0:
        print("A única raiz desta equação é {}".format(x1))
    else:
        if x1 > x2:
            print("As raízes desta equação são {} e {}".format(x1, x2))
        else:
            print("As raízes desta equação são {} e {}".format(x2, x1))









