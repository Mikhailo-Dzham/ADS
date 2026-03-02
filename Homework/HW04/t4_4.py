import math


def f(x):
    # sin(x) - x/3 = 0
    return math.sin(x) - x / 3


left = 1.6
right = 3.0

for _ in range(100):
    mid = (left + right) / 2

    # function is descending:
    # f(1.6) > 0, а f(3) < 0.
    if f(mid) > 0:
        left = mid
    else:
        right = mid

print(f"x =  {right:.6f}")
print(f"Check sin(x): {math.sin(right):.6f}")
print(f"Check x/3:    {right / 3:.6f}")