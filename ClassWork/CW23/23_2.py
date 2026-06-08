import sys

def dfs(graph, strt):

    for i, edge in enumerate(graph[strt]):
        if int(edge) and not i in component:
            component.append(i)
            dfs(graph, i)

if __name__=="__main__":
    data = sys.stdin.read().split("\n")
    size, start = map(int, data[0].split())
    start -=1
    m = [list(map(int, i.split())) for i in data[1::]]

    component = [start]
    dfs(m, start)
    print(len(component))
