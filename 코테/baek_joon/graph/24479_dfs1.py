
n,m,r = 5,5,1

visited = [ [] for i in range(n+1)]

start = 1
edge = [[1,4], [1,2], [2,3], [2,4], [3,4]]
for i in range(n+1):
    
    if visited[i]==1:
        continue
    
    