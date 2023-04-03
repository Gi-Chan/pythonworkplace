

# 초기 상태
puzzle = [1, 2, 3,
          0, 4, 6,
          7, 5, 8]

# 목표 상태
goal = [1, 2, 3, 
        4, 5, 6, 
        7, 8, 0]


class State:
    def __init__(self, board, goal, moves=0):
        self.board = board
        self.moves = moves
        self.goal = goal

    # i1과 i2를 교환하여서 새로운 상태를 반환한다. 
    def get_new_board(self, i1, i2, moves):
        new_board = self.board[:]
        new_board[i1], new_board[i2] = new_board[i2], new_board[i1]
        return State(new_board, self.goal, moves)
    
    # 자식 노드를 확장하여서 리스트에 저장하여서 반환한다. 
    def expand(self, moves):
        result = []
        i = self.board.index(0) # 숫자 0(빈칸)의 위치를 찾는다. 
        if not i in [0, 1, 2] : # UP 연산자
            result.append(self.get_new_board(i, i-3, moves))
        if not i in [0, 3, 6] : # LEFT 연산자
            result.append(self.get_new_board(i, i-1, moves))
        if not i in [2, 5, 8]: # RIGHT 연산자
            result.append(self.get_new_board(i, i+1, moves))
        if not i in [6, 7, 8]: # DOWN 연산자
            result.append(self.get_new_board(i, i+3, moves))
        
        return result

    # 객체를 출력할 때 사용한다. 
    def __str__(self):
        return str(self.board[:3]) +"\n"+\
        str(self.board[3:6]) +"\n"+\
        str(self.board[6:]) +"\n"+\
        "------------------"
    def __eq__(self, other):
        return self.board == other.board
    

# open 리스트
open_queue = [ ]
open_queue.append(State(puzzle, goal))
closed_queue = [ ]
moves = 0
while len(open_queue) != 0: 
    x = open_queue.pop(0) # 큐의 맨 앞에서 노드를 가져온다.
    closed_queue.append(x) # 가져온 노드는 닫힌 리스트에 추가한다. 
    if x.board == goal:
        print(print("탐색 서공"))
        break

    moves = x.moves + 1
    for state in x.expand(moves):
        if (state not in closed_queue) and (state not in open_queue): # 현재 상태가 visit하지 않았으면 open_quqeue에 추가
            open_queue.append(state) # BFS 는 큐의 형태로 탐색하니까 그냥 append 해도 된다.
    
    print(x)
print(moves)