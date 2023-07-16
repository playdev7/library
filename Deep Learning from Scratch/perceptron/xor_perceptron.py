import numpy as np

# NAND, OR, AND 퍼셉트론을 조합하여 XOR 다중 퍼셉트론을 만들어낸다.

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    y = np.sum(w * x) + b
    if y <= 0:
        return 0
    else:
        return 1

def OR(x1, x2):
    x = np.array([0.5, 0.5])
    w = np.array([x1, x2])
    b = -0.2
    y = np.sum(w * x) + b
    if y <= 0:
        return 0
    else:
        return 1

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)

    return y

print(XOR(1, 1))
print(XOR(0, 1))
print(XOR(0, 1))
print(XOR(0, 0))1