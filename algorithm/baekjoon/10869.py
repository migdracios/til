# 사칙연산 알고리즘

'''
- 문제 : 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 
- 입력 : 두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)
- 출력 : 첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.
'''

def calculator(num1, num2):
    '''
    입력받은 값으로 덧셈, 뺄셈, 곱셈, 나눗셈, 나머지를 print문으로 출력
    '''
    print(num1+num2)
    print(num1-num2)
    print(num1*num2)
    print(num1//num2) # 자연수의 나눗셈
    print(num1%num2)
    
# 사용자 입력
A, B = map(int, input().split())
calculator(A, B)