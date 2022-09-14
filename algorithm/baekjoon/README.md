# 백준 알고리즘
- 마크다운 토글 코드
```shell
<details>
<summary>TITLE</summary>
<div markdown="1">

CONTENT

</div>
</details>
```

## 목차
- [🚩10869. 사칙연산](#10869-사칙연산)
- [🚩2588. 곱셈]()

## 10869. 사칙연산
- 문제 : 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 
- 입력 : 두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)
- 출력 : 첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.

<br>

- 자연수는 // 두개의 슬래시를 사용하여 나눗셈을 정수로 표현한다

```python
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
```

## 2588. 곱셈
- 문제 : 세 자릿수의 곱셈을 실행하는 과정을 프로그램으로 구현하시오
- 입력 : 첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다
- 출력 : 첫째 줄부터 넷째 줄까지 차례대로 (3), (4), (5), (6)에 들어갈 값을 출력한다.

<br>

- 두번째는 10을 세번째는 100을 곱해주어 더해주어야 원래 곱셈 값이 나온다

```python
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
```

## 2884. 알람 시계
- 문제 : 원래 설정할 시간을 설정하면 45분 일찍 울리는 알람시계
- 입력 : 시각과 분을 각각 공백을 간격으로 입력
- 출력 : 45분 빠른 시각과 분을 각각 공백 간격으로 출력

<br>

- 입력 시간이 45분에서 60분 사이라면 45분을 빼준다.
- 입력 시간이 45분 미만이라면 15를 더해주고 1시간을 빼주는 것으로 45분을 빼주는 것과 같아진다.
- 0시를 입력했다면 24시로 바꿔서 처리한다.

<details>
<summary>알람 시계 알고리즘</summary>
<div markdown="1">

```python
def alarm(hour, minute):
    '''
    1. 분에 15를 더한다.
    2. 시각에 1을 뺀다.
    3. 만약 숫자가 0이라면, 24로 변경
    4. 분이 45보다 크다면 더하기 대신 45빼기
    5. 45보다 분이 크다면 시각을 빼지 않음
    ---
    case1. 분이 45보다 큰 경우
    case2. 아닐 경우
    '''
    if minute >= 45:
        minute -= 45
        print(hour, minute)
        return 1    
    minute += 15
    if hour == 0:
        hour = 24
    hour -= 1
    print(hour,minute)
    return 1
    
hr, min = map(int, input().split())
alarm(hr, min)
```

</div>
</details>

## 1110. 더하기 사이클
    - 사이클을 돈다고 생각해서 재귀호출로 분석 및 풀이

```python
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
```