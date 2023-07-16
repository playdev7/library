import numpy as np

def OR(x1, x2):
    x = np.array([0.5, 0.5])
    w = np.array([x1, x2])
    b = -0.2

    y = np.sum(w * x) + b

    if y <= 0:
        return 0
    else:
        return 1

print(OR(1, 1))
print(OR(1, 0))
print(OR(0, 1))
print(OR(0, 0))

