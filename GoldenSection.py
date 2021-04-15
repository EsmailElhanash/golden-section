from sympy import *

print('Enter a function of x: ')
f = input()
x = Symbol('x')
f = lambdify(x, f)
print('enter interval start')
intervalStart = float("%.4f" % float(input()))
print('enter interval end')
intervalEnd = float("%.4f" % float(input()))
GR = 0.618
xl = float("%.4f" % intervalStart)
xu = float("%.4f" % intervalEnd)
x1 = float("%.4f" % (xl + GR * (xu - xl)))
x2 = float("%.4f" % (xu - GR * (xu - xl)))
length = float("%.4f" % abs(xu - xl))
eb = float("%.4f" % (x2 - xl))
print('Xl    \t\tX2    \t\tX1    \t\tXu    \t\tf(x2) \t\tf(x1) \t\tL    \t\tError Bound')
for i in range(8):
    print(str("%.4f" % xl) + '\t\t' + str("%.4f" % x2) + '\t\t' + str("%.4f" % x1) + '\t\t' + str("%.4f" % xu) + '\t\t' + str("%.4f" % f(x2)) + '\t\t' + str("%.4f" % f(x1)) + '\t\t' + str("%.4f" % length) + '\t\t' + str("%.4f" % eb))
    if f(x1) > f(x2):
        xl = x2
        x2 = x1
        x1 = float("%.4f" % (xl + GR * (xu - xl)))
        length = float("%.4f" % abs(xu - xl))
        eb = float("%.4f" % (x2 - xl))
    else:
        xu = x1
        x1 = x2
        x2 = float("%.4f" % (xu - GR * (xu - xl)))
        length = float("%.4f" % abs(xu - xl))
        eb = float("%.4f" % (x2 - xl))


if f(x1) >= f(x2):
    print('Fmax= ' + str(f(x1)))
else:
    print('Fmax= ' + str("%.4f" % f(x2)))

    #2 * sin(x) - 0.1 * x**2