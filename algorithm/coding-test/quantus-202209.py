# 퀀터스테크놀로지스-과제

'''
1. 숫자 1 혹은 0을 임의로 return하는 get_1_or_0 함수를 구현
2. 1.에서 작성한 get_1_or_0을 이용하여 숫자 n을 인자로 받아 0~n 사이의 임의의 정수를 반환하는 get_random 함수를 구현
- get_1_or_0에서는 난수 생성 함수를 사용해도 괜찮으나, get_random 함수에서는 절대 난수 생성 함수를 직접 사용해서는 안됨
'''

import random

def get_1_or_0():
    return random.randint(0,1)

def get_random(n):
    '''
    get_1_or_0 함수를 호출한 값을 활용하여 get_random의 값이 0~n까지의 임의의 정수를 반환해야함
    get_random 함수에서는 난수 생성을 할 수 없음
    ---
    case1. 난수 생성한 값에 입력값을 더하거나 곱해서 리턴한다 -> 그건 0~n까지가 아니라 그냥 n의 값이 나올것
    
    입력 값이 난수의 마지막 값이 되어야 한다...
    
    case2. n번 반복문 시작하여 난수를 생성해서 1이 나온 값을 리턴? -> 0에서 n까지의 난수가 아닌, 0,1,2,3 차례대로 리턴
    '''
    for i in range(n):
        print("index", i)
        random_num = get_1_or_0()
        print("random_num",random_num)
        if random_num == 1:
            return i

print(get_random(50))
    