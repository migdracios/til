# 더하기 사이클

'''
문제
---
0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다. 
먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다. 
그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다. 다음 예를 보자.

26부터 시작한다. 2+6 = 8이다. 
새로운 수는 68이다. 6+8 = 14이다. 새로운 수는 84이다. 8+4 = 12이다. 새로운 수는 42이다. 4+2 = 6이다. 새로운 수는 26이다.
위의 예는 4번만에 원래 수로 돌아올 수 있다. 따라서 26의 사이클의 길이는 4이다.

N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.
---
입력 : 26
출력 : 4
'''
def plus_cycle(default_number, input_number, cycle):
    '''
    1. 함수의 인자 input_number를 문자열로 바꾼다
    2. input_number의 첫 번째와 두 번째 값을 더한다
    3. input_number의 두 번째 값과 더한 값을 문자열화한 두 번째 값을 합쳐 새로운 수로 만든다
    4. 사이클에 1을 더해 카운트한다
    5. 새로운 수가 default_number와 같다면 사이클을 반환하면서 함수 종료
    6. 아니라면, 함수에 인자를 담아 재귀호출한다 
    '''
    str_input_num = str(input_number)
    if len(str_input_num) == 1:
        str_input_num = str(0) + str_input_num
    plus_input_num = str(int(str_input_num[0]) + int(str_input_num[1]))
    plus_input_num = plus_input_num if len(plus_input_num) == 1 else plus_input_num[-1]
    new_num = int(str_input_num[1] + plus_input_num)
    cycle += 1
    if new_num == default_number:
        print(cycle)
        return cycle
    return plus_cycle(default_number, new_num, cycle)
    
    
input_number = int(input())
plus_cycle(input_number, input_number, 0)