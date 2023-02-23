n,m= map(int,input().split())

n_5=n
n_2=n

n_m_5=n-m
n_m_2=n-m

m_5=m
m_2=m

def five(x):
    cnt=0
    while x>=5:
        x = x//5
        cnt +=x
    return cnt
def two(x):
    cnt2=0
    while x>=2:
        x = x//2
        cnt2+=x
    return cnt2
print(min(two(n_2)-two(n-m_2)-two(m_2), five(n_5)-five(n-m_5)-five(m_5)))