import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    # 가중치*x 의 합이 편항 b 를 넘어서야 뉴런이 활성화된다.
    b = -0.7
    tmp = np.sum(w*x) + b
    # 즉 가중치의 합에서 편향을 감산하였을 때 0 이상이 된다면 활성화 된 것이다.
    if tmp <= 0:
        return 0
    else:
        return 1

print(AND(0, 0))
print(AND(1, 0))
print(AND(0, 1))
print(AND(1, 1))
