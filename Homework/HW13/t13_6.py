def solve_731():
    expr = input().strip()
    stack = []

    def priority(op):
        if op in ('+', '-'): return 1
        if op in ('*', '/'): return 2
        return 3  # Для літер повертаємо найвищий пріоритет

    def needs_left_brackets(parent_op, left_op):
        return priority(left_op) < priority(parent_op)

    def needs_right_brackets(parent_op, right_op):
        if priority(right_op) < priority(parent_op):
            return True
        # якщо пріоритети рівні, правій частині потрібні дужки
        # тільки якщо батьківський оператор є некоммутативним
        if priority(right_op) == priority(parent_op):
            return parent_op in ('-', '/')
        return False

    for char in reversed(expr):
        if char in "+-*/":

            left_expr, left_op = stack.pop()
            right_expr, right_op = stack.pop()

            l_str = f"({left_expr})" if needs_left_brackets(char, left_op) else left_expr
            r_str = f"({right_expr})" if needs_right_brackets(char, right_op) else right_expr

            stack.append((l_str + char + r_str, char))
        else:
            stack.append((char, 'VAR'))

    print(stack[0][0])


if __name__ == '__main__':
    solve_731()