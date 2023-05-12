com = 7
connect = 6

graph = [ [0] for i in range(com+1)]
visited = [0]*(com+1)
cnt =0

def dfs(n):
    global cnt
    visited[n] = 1

    for i in graph[n]:
        if visited[i] == 0:
            dfs(i)
            cnt+=1


for i in range(connect):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


dfs(1)
print(cnt)
