from t2_10 import f
from t2_11 import g, g_optimized


def h(n):
    # f(n) -- O(n)
    # g(n) -- O(n**2)
    # Сумарна швидкість визначається найповільнішою частною
    return f(n) + g(n)  # Загальна складність O(n^2)

# І так це можна оптимізувати до О(1)

def h_optimized(n):
    return g_optimized(n) + (n**2 + n)//2