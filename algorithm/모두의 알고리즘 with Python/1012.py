# 최대공약수 알고리즘
# 유클리드 알고리즘

'''
- gcd(a, b) = gcd(b, b % a) ... = gcd(n, 0) = n
a와 b의 최대공약수는 b와 b를 a로 나눈 나머지와 같다.
같은 식을 재귀로 반복하다보면 나머지가 0이 되는 순간, 앞의 값이 최대공약수가 됨
'''

def find_gcd(num1, num2):
    
    if num2 == 0:
        return num1
    gcd_num1 = num2
    gcd_num2 = num2 % num1
    find_gcd(gcd_num1, gcd_num2)
    
test1, test2 = 60, 24

def gcd(a, b):
    print(a % b)
    print(b % a)
    
gcd(20, 12)