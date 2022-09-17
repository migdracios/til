# 셀프 넘버 알고리즘

'''
- 문제
---
셀프 넘버는 1949년 인도 수학자 D.R. Kaprekar가 이름 붙였다. 양의 정수 n에 대해서 d(n)을 n과 n의 각 자리수를 더하는 함수라고 정의하자. 예를 들어, d(75) = 75+7+5 = 87이다.

양의 정수 n이 주어졌을 때, 이 수를 시작해서 n, d(n), d(d(n)), d(d(d(n))), ...과 같은 무한 수열을 만들 수 있다. 

예를 들어, 33으로 시작한다면 다음 수는 33 + 3 + 3 = 39이고, 그 다음 수는 39 + 3 + 9 = 51, 다음 수는 51 + 5 + 1 = 57이다. 이런식으로 다음과 같은 수열을 만들 수 있다.

33, 39, 51, 57, 69, 84, 96, 111, 114, 120, 123, 129, 141, ...

n을 d(n)의 생성자라고 한다. 위의 수열에서 33은 39의 생성자이고, 39는 51의 생성자, 51은 57의 생성자이다. 생성자가 한 개보다 많은 경우도 있다. 예를 들어, 101은 생성자가 2개(91과 100) 있다. 

생성자가 없는 숫자를 셀프 넘버라고 한다. 100보다 작은 셀프 넘버는 총 13개가 있다. 1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 97

10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
---
- 입력 : 없음
- 출력
1
3
5
7
9
...
9993

'''


# #테스트 1번
# def kaprekar(number):
#     # 알고리즘 설계
#     '''
#     1. n과 각 자릿 수를 더하는 함수 생성
#     2. 함수 재귀호출
#     '''
#     # 함수 설계
#     '''
#     1. number를 함수의 인자로 받음
#     2. number를 문자열로 바꿔 각 길이만큼 반복해 리스트로 만듦
#     3. number와 리스트를 sum한 값과 더함, print로 해당 숫자를 출력
#     4. 더한 값을 인자로 함수 재귀호출
#     5. 10000보다 크거나 같다면 함수리턴
#     '''
#     number_list = list(int(num) for num in str(number))
#     kaprekar_number = number + sum(number_list)
#     # print(f"더한 값은 {kaprekar_number}")
#     if kaprekar_number >= 10000: return
#     return kaprekar(kaprekar_number)

# kaprekar(1)

import sys
sys.setrecursionlimit(10**7)


# 테스트 2번
'''
알고리즘 설계
- 1부터 시작해서 카프레카 함수의 결괏값으로 나온 숫자를 1부터 1만까지의 리스트에서 제거
- 카프레카 함수의 결괏값이 1만이 넘는다면 함수 종료
- 카프레카 함수가 종료되면 리스트 print로 출력
'''

def kaprekar(number, selfnum_list):
    '''
    1. number과 selfnum_list를 인자로 받음
    2. number를 문자열로 바꿔 각 길이만큼 반복해 리스트로 만듦
    3. number와 리스트를 sum한 값과 더해 result 변수로 할당
    4. 더한 값이 10000이 넘는다면 selfnum_list 반환
    5. 넘지 않는다면 result, selfnum_list를 인자로 셀프넘버 함수 호출
    6. number+1, selfnum_lsit를 인자로 담아 재귀호출
    '''
    number_list = list(int(num) for num in str(number))
    result = number + sum(number_list)
    if result >= 10000: return selfnum_list
    selfnum_list = make_selfnum_list(result, selfnum_list)
    return kaprekar(number+1, selfnum_list)
    
def make_selfnum_list(number, selfnum_list):
    '''
    1. number, selfnum_list를 인자로 받음
    2. selfnum_list에서 number 값을 제거
    3. selfnum_list 반환
    '''
    if not number in selfnum_list: return selfnum_list
    selfnum_list.remove(number)
    return selfnum_list

init_list = [i for i in range(1, 10001)]
selfnum_list = kaprekar(1, init_list)
for i in selfnum_list:
    print(selfnum_list)





    
    
    
