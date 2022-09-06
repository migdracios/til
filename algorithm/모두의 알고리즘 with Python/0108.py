# 팩토리얼 알고리즘

def fact(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f
    
test_num = 3
print(fact(test_num)) 