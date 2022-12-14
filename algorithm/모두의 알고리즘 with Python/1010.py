# 팩토리얼 알고리즘
## 재귀호출 방식

def fact(n):
    '''
    1. 0! = 1, 1! = 1 의 경우라면 1을 리턴하는 조건문
    2. 아니라면, 재귀호출을 통해서 곱계산 실행
    3. 다시 조건문과 연속 계산
    4. 재귀호출로 인해서 실행되는 입력값이  1이 될때까지 계속 호출하며
    5. 마지막에 fact(1) = 1 로 반환되어 이전 값에 1을 곱하고 재귀호출은 종료된다.
    '''
    if n <= 1:
        return 1
    return n*fact(n-1)

print(fact(5))