# 최대공약수 알고리즘
# 유클리드 알고리즘

'''
- gcd(a, b) = gcd(b, b % a) ... = gcd(n, 0) = n
a와 b의 최대공약수는 b와 b를 a로 나눈 나머지와 같다.
같은 식을 재귀로 반복하다보면 나머지가 0이 되는 순간, 앞의 값이 최대공약수가 됨
'''

def find_gcd(num1, num2):
    min_num = min(num1, num2)
    max_num = max(num1, num2)
    if min_num == 0:
        return max_num
    # 함수를 실행하고 끝나는게 아니라 함수를 인자를 넣어 반환해야 한다!
    return find_gcd(min_num, max_num % min_num)
    
test1, test2 = 60, 24
result = find_gcd(test1, test2)
print(result)
