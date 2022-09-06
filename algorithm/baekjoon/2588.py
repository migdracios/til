# 세자릿수 곱셈 알고리즘

'''
- 문제 : 세 자릿수의 곱셈을 실행하는 과정을 프로그램으로 구현하시오
- 입력 : 첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다
- 출력 : 첫째 줄부터 넷째 줄까지 차례대로 (3), (4), (5), (6)에 들어갈 값을 출력한다.
'''

def multiply_decimal(num1, num2):
    '''
    1. 두 번째 숫자의 첫 번째 자리 곱셈 출력
    2. 두 번째 숫자의 두 번째 자리 곱셈 출력
    3. 두 번째 숫자의 세 번째 자리 곱셈 출력
    4. 1/2/3을 덧셈한 값 출력
    '''
    num_str = str(num2)
    num_first = int(num_str[2])
    num_second = int(num_str[1])
    num_third = int(num_str[0])
    
    num_first = num1*num_first
    num_second = num1*num_second
    num_third = num1*num_third
    print(num_first)
    print(num_second)
    print(num_third)
    print(num_first+num_second*10+num_third*100)

A = int(input())
B = int(input())
multiply_decimal(A, B)
    