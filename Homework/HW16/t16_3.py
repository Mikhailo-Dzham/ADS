import sys
sys.setrecursionlimit(2000000)


class Tree:
    def __init__(self, key, color=0, parent=None):
        self.key = key
        self.color = color
        self.parent = parent
        self.children: list['Tree'] = []

    def get_colors_recursive(self, answers):

        my_colors = set()

        # додаємо свій власний колір
        my_colors.add(self.color)

        # рекурсивно йдемо до всіх дітей
        for child in self.children:
            # берем всі кольори дитини та її піддерева
            child_colors = child.get_colors_recursive(answers)
            my_colors.update(child_colors)

        answers[self.key] = len(my_colors)

        return my_colors


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        n = int(f.readline().strip())

        # Створюємо словник усіх вершин наперед
        # щоб при зчитуванні швидко знаходити батька за його номером.
        nodes = [Tree(key=i) for i in range(n + 1)]
        root = None

        for i in range(1, n + 1):
            line = f.readline().strip()
            if not line:
                continue
            p, c = map(int, line.split())

            nodes[i].color = c

            # Будуємо зв'язки дерева
            if p == 0:
                root = nodes[i]
            else:
                nodes[i].parent = nodes[p]
                nodes[p].children.append(nodes[i])

        #масив, де кожна вершина запише свою кінцеву відповідь
        answers = [0] * (n + 1)

        if root:
            root.get_colors_recursive(answers)

        print(*(answers[1:]))