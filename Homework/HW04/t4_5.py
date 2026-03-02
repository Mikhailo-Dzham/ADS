def f(x):
    return x ** 3 + 4 * x ** 2 + x - 6


left = 0.0
right = 2.0

for _ in range(100):
    mid = (left + right) / 2

    if f(mid) < 0:
        left = mid
    else:
        right = mid

print(f"x: {right:.6f}")
print(f"Check f(x): {f(right):.6f}")