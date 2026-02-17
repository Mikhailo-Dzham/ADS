def f(x):
    return x ** 3 + x + 1

### Limits
left = 0.0
right = 10.0
target = 5.0

# 100 is enough
for _ in range(100):
    mid = (left + right) / 2

    if f(mid) <= target:
        left = mid
    else:
        right = mid

# Output
print(f"x: {right:.6f}")