##########Болок збору данних#########

def get_couple() -> list:
    return [int(el) for el in input().split()]

def get_grass_zones(gz_count) ->list:
    return [get_couple() for _ in range(gz_count)] #Приймає m пар коодинат що позначають зони трави

###########Блок бінарногого пошуку#######

def bin_search(high, low=1):
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if check(mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans

###########Блок перевірки умови (Використаємо Жадний алгоритм)########

def check(d) -> bool:

    current_zone = 0
    last_cow = grass_zones[current_zone][0]

    for cow in range(n-1):
        step = last_cow + d

        while current_zone < m and step > grass_zones[current_zone][1]:
            current_zone +=1

        if current_zone >= m:
            return False

        last_cow = max(step, grass_zones[current_zone][0])
    return True

##################################################################

# Отримуємо Інпут
n, m = get_couple()
grass_zones = get_grass_zones(m)

grass_zones.sort() #Сортуємо зони по порядку

#Шукаєм необхідні для продовження параметри
first_gz = grass_zones[0][0] #Початок зелених зон
last_gz = grass_zones[-1][1]#Кінець зелених зон
max_d = (last_gz - first_gz) // (n-1)

####
# print(n, m)
# print(grass_zones)
# print(first_gz, last_gz)
#### Треба для тесту вводу

print(bin_search (max_d))