

# initial grpah
tree = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F', 'G'],
    'D' : ['H', 'I'],
    'E' : ['I'],
    'F' : ['U'],
    'G' : [],
    'H' : [],
    'I' : [],
    'U' : []
}
# initial start, goal
start = 'A'
goal = 'U'

open_list = []
closed_list = []

# line count
cnt =0
print(f"{cnt}. open = {open_list} \t\t closed = {closed_list}")

"""
0. depth_first_search()
1. open ← [root node] # 루트노드를 open 리스트에 넣고
2. closed ← [ ] # closed 는 비어있는 걸로 초기와
3. while open ≠ [ ] do # open 노드가 비어 있으면 종료
	X ← the first element in the open list # open 리스트에 첫 요소(인덱스0)을 x에 할당
	if X == goal then return SUCCESS # x가 goal과 같으면 탐색 종료
5.	else
				Generate the child node of the X # X의 자식노드를 생성하고
				Add the X to Closed List # X는 CLOSE 리스트에 넣는다
				# 또는 만약 X가 OPEN, CLOSED 리스트에 있으면 버림
				or discard the X if that is already in the open or closed list
				# OPEN 제일 앞에 자식노드를 넣는다.
				Add the child nodes to the head(front) of the open list
return FAIL # OPEN리스트가 빌 때까지 못찾으면 실

"""
# 1, 2 에 해당하는 부분
open_list.append(start)
cnt+=1
print(f"{cnt}. open = {open_list} \t closed = {closed_list}")

# 3번에 해당하는 코드
while (open_list != []):
    cnt+=1

    X = open_list.pop(0) # 맨 앞에를 뺌

    if X ==goal:
        print(f'{cnt}. 목표 노드 {goal} 발견!')
        break
    
    # 5번 부분 작성
    else:
        child = tree[X]
        closed_list.append(X)
        for c in child:
            if (c in open_list) or (c in closed_list):
                child.remove(c)
        
        open_list = child + open_list # 생성한 자식을 맨 앞에 붙임
    print(f"{cnt}. open = {open_list} \t closed = {closed_list}")