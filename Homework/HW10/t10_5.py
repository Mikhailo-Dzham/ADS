import sys


def solve():
    input_data = sys.stdin.read().split()

    idx = 0
    n_params = len(input_data)

    while idx < n_params:
        capacity = int(input_data[idx])
        num_tracks = int(input_data[idx + 1])

        tracks = []
        for i in range(num_tracks):
            tracks.append(int(input_data[idx + 2 + i]))

        idx += 2 + num_tracks

        # Якщо відсорутвати за спаавднням то можна буде швидше знайти велику суму а також відсікти погані бранчі
        tracks.sort(reverse=True)

        suffix_sums = [0] * num_tracks
        current_suffix = 0
        for i in range(num_tracks - 1, -1, -1):
            current_suffix += tracks[i]
            suffix_sums[i] = current_suffix

        best_sum = -1

        def dfs(i, current_sum):
            nonlocal best_sum

            if current_sum > best_sum:
                best_sum = current_sum

            # Якщо ми вже знайшли ідеальну суму, далі шукати немає сенсу взагалі ;) Ну майже повний перебір
            if best_sum == capacity:
                return

            if i == num_tracks:
                return

            # Branch and bound
            if current_sum + suffix_sums[i] <= best_sum:
                return

            # Branch 1
            if current_sum + tracks[i] <= capacity:
                dfs(i + 1, current_sum + tracks[i])
                # Якщо після гілки ми досягли ідеалу — миттєво виходимо з рекурсії
                if best_sum == capacity:
                    return

            # Branch 2: Пропускаємо трек
            dfs(i + 1, current_sum)

        dfs(0, 0)

        print(f"sum:{best_sum}")


if __name__ == "__main__":
    sys.setrecursionlimit(2500) #Якщо збільшити ліміт рекурсій то працює швидше, але 1000 (дефолт) буде досить
    solve()