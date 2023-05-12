
# 100일 동안
# 50일은 비, 50일은 해가 뜸
# 101부터 108일까지 관측값은 있는데 날씨값은 모름 -> 이건 비터비(디코딩)문제

## 함수의 파라미터에는 언더바를 붙이는 게 국제 표준임

##  Viterbi(decode)
def decode(states, init_prob, trans_prob, emit_prob, sequence):
    pass

# 초기 모델
states = ('rainy', 'sunny')
init_prob = {
    'rainy' : 0.5,
    'sunny' : 0.5
    }
trans_prob = {
    'rainy': { 'rainy' : 0.7, 'sunny' : 0.3 },
    'sunny': { 'rainy' : 0.4, 'sunny' : 0.6 }
    }   
emit_prob = {
    'sunny': { 'walk' : 0.6, 'shop' : 0.3, 'clean' : 0.1 },
    'rainy': { 'walk' : 0.1, 'shop' : 0.4, 'clean' : 0.5 }
    }   
sequence = ['walk', 'shop', 'clean', 'clean', 'walk', 'walk', 'walk', 'clean']



## forward
def forward(states_, init_prob_, trans_prob_, emit_prob_, sequence_):

    # 시퀀스의 길이
    length = len(sequence_)

    # 길이가 0이면 종료
    if length==0:
        return 0
    
    # 딕셔너리를 저장하는 리스트
    alpha = [{}]

    # 초기 상태 설정
    for state in states_:
        # 처음 상태는       초기 확률의 상태 확률 * 해당 상태에서 관측값이 [0]이다.
        alpha[0][state] = init_prob_[state] * emit_prob_[state][sequence_[0]]
    
    # 2번째 이상부터 
    for index in range(1, length):
        # 새로운 상태를 저장할 딕셔너리를 추가
        alpha.append({})
        # 상태에서 다음 상태로 갈 확률을 구하기 위해 반복문을 설정한다
        for state_to in states_:
            prob=0 # state_to 로 전이할 확률
            # state_from 상태에서 state_to 으로 갈 확률을 구한다
            for state_from in states_:
                prob +=alpha[index-1][state_from] * trans_prob_[state_from][state_to]
            alpha[index][state_to] = prob * emit_prob_[state_to][sequence_[index]]
    return alpha



##  Evaluation
def evaluate(states_, init_prob_, trans_prob_, emit_prob_, sequence_):
    states_ = set(states_) # 상태에 중복된 값이 있으면 안되므로 set 적용

    length = len(sequence_)
    if length ==0:
        return 0
    
    prob = 0
    alpha = forward(states_, init_prob_, trans_prob_, emit_prob_, sequence_)
    for state in alpha[length-1]:
        prob += alpha[length-1][state]

    return prob*100



alpha = evaluate(states, init_prob, trans_prob, emit_prob, sequence)
print(alpha)





