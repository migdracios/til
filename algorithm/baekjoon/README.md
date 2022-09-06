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