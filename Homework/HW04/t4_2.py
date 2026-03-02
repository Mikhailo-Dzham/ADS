import math

### Input c
c = float(input())

### const
ITERATIONS = 100 # Higher value for higher accuracy. 100 is enough

left = 0.0 # Low limit
right = 100000.0  # High limit

# Binary search
for _ in range(ITERATIONS):
    mid = (left + right) / 2
    val = mid * mid + math.sqrt(mid)

    if val < c:
        left = mid
    else:
        right = mid

# Output
print(f"{right:.6f}")