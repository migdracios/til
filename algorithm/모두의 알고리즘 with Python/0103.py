# 1부터 n까지의 합 알고리즘
## 합 저장 알고리즘

def sum_n(n):
    s = 0
    for i in range(1, n+1):
        s = s + 1
    return s

print(sum_n(1))