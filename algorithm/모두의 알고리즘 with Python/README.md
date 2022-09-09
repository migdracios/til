# 🗣 모두의 알고리즘 with Python
- 마크다운 토글
```
<details>
<summary></summary>
<div markdown="1">


</div>
</details>
```


# Section 01. 알고리즘이란?
    
    - 어떤 문제를 풀기 위한 절차나 방법
    - 주어진 입력정보를 원하는 출력정보로 만드는 일련의 과정을 구체적이고 명료하게 적은 것

## 문제. 절댓값 구하기

<details>
<summary>알고리즘 설계</summary>
<div markdown="1">

    - 0부터 특정 수에 해당하는 거리의 값을 의미하는 절댓값을 프로그래밍으로 구현하자
    - 문제 : 어떤 숫자의 절댓값 구하기
    - 입력 : 절댓값을 구할 실수 a
    - 출력 : a의 절댓값

    <br>

    1. a가 0보다 크거나 같은지 확인하고, 같다면 a를 결과로 반환
    2. 1이 아니라면(a가 0보다 작으면) -a를 결과로 반환

</div>
</details>

<details>
<summary>0101.부호 판단</summary>
<div markdown="1">

```python
def abs_sign(a):
    if a >= 0:
        return a
    else:
        return -a


print(abs_sign(-3))
```
위의 알고리즘을 설계한 방식과 동일하게 코드를 구현

</div>
</details>

<details>
<summary>0102. 제곱근 활용</summary>
<div markdown="1">

```python
import math


def abs_square(a):
    b = a * a
    return math.sqrt(b)


print(abs_square(-7))
```

    - 실수의 제곱수는 언제나 양수라는 것을 활용한 알고리즘.
    1. 입력 수를 제곱함
    2. 제곱수를 제곱근처리하여 반환

    <br>

    - math 라이브러리를 활용, math.sqrt 메서드가 제곱근에 해당함
    - 분기문을 사용하지 않고도 진행하여 모든 케이스를 커버했다는 점을 주목.

</div>
</details>

## 문제. 1부터 n까지의 합 구하기

<details>
<summary>알고리즘 설계</summary>
<div markdown="1">

    - 문제 : 1부터 n까지의 합에서 어떤 수가 들어가더라도 동일한 값을 계산할 수 있어야함
    - 입력 : 마지막 합할 숫자 
    - 출력 : 1부터 n까지 더한 값

    <br>

    - 설계하기
    - 1더하기2를 계산한 결과를 저장, 저장한 결과와 3을 계산한 결과를 다시 저장, ...
    - 입력한 마지막 숫자만큼 반복하기

</div>
</details>    

<details>
<summary>0103. 합 저장 방식</summary>
<div markdown="1">

```python
def sum_n(n):
    s = 0
    for i in range(1, n+1):
        s = s + 1
    return s
```

</div>
</details>

<details>
<summary>0104. 가우스 방식</summary>
<div markdown="1">

```python
def sum_n(n):
    return n * (n+1) // 2 # 슬래시 두 개(//)는 정수 나눗셈을 의미
```

</div>
</details>

## 입력 크기와 계산 횟수
    - 알고리즘에서 필요한 입력은 크기가 성능에 영향을 주는 경우가 있다.
    - 1부터 n까지의 합 알고리즘을 예시로 들어 비교해보자

### 값 저장 알고리즘
    - 값 저장 알고리즘은 입력한 값 만큼 1부터 하나씩 값을 더해가면서 저장하는 방식으로 로직이 설계되어 있다.
    - 작은 숫자의 경우에는 1부터 10까지 총 10번의 연산을 하게 되지만 1000을 입력한다면 1000번 연산되어야 한다.
    - 값 저장 알고리즘은 n번을 연산하는 알고리즘이다.
### 가우스 방법
    - 가우스 방법은 1부터 n까지의 합과 관련된 수식을 알고리즘에 적용하는 방법이다.
    - n * (n+1) / 2 는 곱하기, 더하기, 나누기 연산으로 구성되어 있다.
    - 어떤 숫자가 들어오더라도 가우스 방법 알고리즘은 3번을 연산하는 알고리즘이다.

## 빅오 표기법
    - 어떤 알고리즘이 문제를 풀기 위해 연산의 복잡함을 정도로 나타낸 것을 복잡도(Complexity)라고 한다.
    - 복잡도를 표현하는 방법 중에 가장 범용적으로 사용하는 것이 빅오(Big O) 표기법이다.
    - 계산의 횟수자체는 의미가 상대적으로 적으므로 n,n제곱, 1과 같이 축약하여 표현한다
    - 값 저장 알고리즘은 n번 연산하므로 O(n)으로 표현한다. 
    - 가우스 방법의 경우 3번 연산하므로 O(3)으로 표현하나, 상수는 의미가 동일하므로 O(1)로 통일한다.
    - 빅오표기법으로 알고리즘의 복잡도를 파악하고, 연산속도가 빠른 알고리즘을 채택할 수 있어야 한다.
    - 단순히 알고리즘을 설계하고 구현하는 것에 멈추는 것이 아니라, 실제로 작동하는 속도가 빠른지에 대한 고민을 해야한다!

## 문제. 최댓값 찾기
    
<details>
<summary>알고리즘 설계</summary>
<div markdown="1">

- 문제 : 주어진 n개의 숫자 중에서 가장 큰 수를 찾아야 한다.
- 입력 : n개 만큼의 숫자를 가진 리스트
- 출력 : 리스트 중의 가장 큰 수
- 설계 : 리스트의 처음 숫자부터 하나씩 비교해 보는 것은 어떨까?

</div>
</details>

<details>
<summary>0105. 값 저장 알고리즘</summary>
<div markdown="1">

```python
def find_maxnum(numlist):
    '''
    1. 최댓값을 숫자리스트의 첫번째 값으로 변수 지정
    2. 숫자리스트 길이만큼 반복
    3. 숫자리스트[인덱스] 값이 최댓값보다 클 경우, 최댓값으로 변경
    4. 아닐 경우, 그대로 진행
    5. 반복문이 종료된 이후 최댓값 리턴
    '''
    maxnum = numlist[0]

    for i in range(len(numlist)):
        if numlist[i] > maxnum:
            maxnum = numlist[i]
    return maxnum

test_list = [1,2,3,4,5,10,7]
print(find_maxnum(test_list))
```

    - 반복문 만큼 연산을 반복하므로 복잡도는 O(n)

</div>
</details>

<details>
<summary>0106. 최댓값의 위치 찾기 알고리즘</summary>
<div markdown="1">

```python
def find_maxnum_index(numlist):
    '''
    1. 최댓값 변수 저장
    2. 최댓값의 위치 변수 저장
    3. 숫자리스트만큼 반복문 생성
    4. 최댓값과 숫자리스트[인덱스] 값 비교
    5. 값이 크다면 최댓값 저장
    6. 최댓값 위치 변수를 인덱스 값으로 변경
    7. 아니라면, 그대로 진행
    8. 최댓값 위치 변수 반환
    '''
    maxnum = numlist[0]
    maxnum_index = 0
    for i in range(len(numlist)):
        if numlist[i] > maxnum:
            maxnum = numlist[i]
            maxnum_index = i
    return maxnum_index

test_list = [1,3,5,2,4,9,6,8]
print(find_maxnum_index(test_list))
```

- 역시 반복문만큼 연산해야 하므로 O(n) 만큼의 복잡도를 나타낸다

</div>
</details>

## 문제. 동명이인 구하기

    - 문제 : n명의 사람들 중에 같은 이름을 가진 사람을 집합으로 만들어라
    - 입력 : 사람 이름을 값으로 가지고 있는 n개의 리스트
    - 출력 : 같은 이름의 사람을 가지고 있는 집합

<br>

    - 같은 값을 찾아내기 위해서는 리스트의 값을 돌아가면서 같은 리스트 안의 값과 비교해야 한다.
    - 비교가 끝났다면 다음 값도 리스트의 값을 돌아가면서 비교해야 한다.

<details>
<summary>동명이인 찾기 알고리즘</summary>
<div markdown="1">

```python
def find_sameone(list_people):
    '''
    5개의 이름이 들어있는 리스트
    1. 리스트의 길이를 변수에 저장
    2. 결과를 저장할 빈 집합
    3. 0부터 n-2까지 반복 -> 모두 비교했으니 맨끝은 비교할 필요가 없기 때문
    4. i+1 부터 n-1까지 반복 -> 비교대상1은 처음부터, 비교대상2는 그 다음부터이기 때문
    5. a[i]와 a[j]가 같다면, 이름을 결과 집합에 저장
    '''
    len_list = len(list_people)
    sameone = set()
    for i in range(0, len_list-1):
        for j in range(i+1, len_list):
            if list_people[i] == list_people[j]:
                sameone.add(list_people[i])
    return sameone

test_list = ["황영상", "김희정", "한건희", "김태인", "황영상"]
print(find_sameone(test_list))
```

</div>
</details>

# 재귀 호출

    - 재귀호출은 함수 안에서 다시 함수를 호출하는 행위
    - 마트료시카처럼 인형 안에 인형이 있는 것처럼 

## 문제. 팩토리얼 구하기

    - 문제 : 1부터 n까지의 연속한 숫자를 곱하기
    - 입력 : 마지막 숫자 n
    - 출력 : 1부터 n까지의 숫자 곱

    <br>

    - 값을 저장해서 1부터 마지막 숫자까지 곱한 값을 저장, 곱하기를 반복하기
    - O(n)의 복잡도가 필요하다

<details>
<summary>팩토리얼 알고리즘</summary>
<div markdown="1">

```python
def fact(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f
    
test_num = 3
print(fact(test_num)) 
```

</div>
</details>

## 문제. 재귀 호출
    - 문제 : 함수 안에서 함수를 호출하자
    - 입력 : 없음
    - 출력 : 없음

<details>
<summary>무한 헬로</summary>
<div markdown="1">

```python
def inf_hello():
    print("hello")
    inf_hello()
inf_hello()
```

```shell
RecursionError: maximum recursion depth exceeded while calling a Python object
```

    - 함수를 실행하면, 함수 안의 함수를 실행하는 것을 반복하는 것이 끝나지 않아 발생하는 오류 메시지

</div>
</details>

## 문제. 최대공약수 구하기
    - 문제 : 두 개의 정수의 최대공약수를 구하기
    - 입력 : 두 개의 수
    - 출력 : 두 수의 최대공약수

<br>

    - 두 수 중 더 작은 값을 변수로 저장
    - 변수로 두 수가 모두 나눠지는지 검사
    - 아니라면 변수를 1감소 후 검사 반복
    - 맞다면 해당 수를 리턴

<details>
<summary>값 저장 알고리즘</summary>
<div markdown="1">

```python
def find_gcd(num1, num2):
    target_number = num1 if num1 > num2 else num2
    while target_number != 1:
        if num1 % target_number == 0 and num2 % target_number == 0:
            return target_number
        target_number -= 1

num1, num2 = 20, 12
print(find_gcd(num1,num2))
```

</div>
</details>

    - 유클리드 알고리즘
    - 최대공약수(a, b) = 최대공약수(b, b%a) 이다
    - 어떤 수와 0의 최대공약수는 자기자신이므로 최대공약수(a, 0) = a
    - 위 법칙과 재귀호출을 사용하여 반복해서 문제를 풀이

<details>
<summary>유클리드 최대공약수 알고리즘</summary>
<div markdown="1">

```python
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
```

    - 트러블슈팅 : 재귀함수는 함수를 재귀호출 할 때 반환하는 것으로 작동한다

</div>
</details>

## 문제. 하노이탑
    - 문제 : 한 번에 옮길 수 없는 원반을 작은 원반 위에 놓지 않으면서 n개의 원반 모두 마지막 기둥으로 옮기시오
    - 입력 : 옮기려는 원반 n개
    - 출력 : 원반을 옮기는 순서

### 원반이 두 개일 경우
    0. 첫 번째 기둥에 두 개의 원반이 놓여있다
    1. 작은 원반을 두 번째 기둥으로 이동한다
    2. 큰 원반을 세 번째 기둥으로 이동한다. 작은 원반 하나만 이동하면 끝난다(종료조건)
    3. 작은 원반을 세 번째 기둥으로 이동한다(끝)
### 원반이 세 개일 경우
    0. 첫 번째 기둥에 세 개의 원반이 놓여있다
    1. 작은 원반을 세 번째 기둥으로 이동한다
    2. 중간 원반을 두 번째 기둥으로 이동한다
    3. 작은 원반을 두 번째 기둥으로 이동한다(원반 두 개의 경우 종료)
    4. 큰 원반을 세 번째 기둥으로 이동한다
    5. 작은 원반을 첫 번째 기둥으로 이동한다
    6. 중간 원반을 세 번째 기둥으로 이동한다. 작은 원반 하나만 이동하면 끝난다(종료조건)
    7. 작은 원반을 세 번째 기둥으로 이동한다(끝)

### 알고리즘 요약
    1. 원반이 한 개면 옮기면 끝(종료조건)
    2. 원반이 n 개일때, 
        - 1번 기둥에 있는 n개의 원반 중 n-1개를 2번 기둥으로 옮김(3번 기둥을 보조 기둥으로 사용)
        - 1번 기둥에 남아 있는 가장 큰 원반을 3번 기둥으로 옮김
        - 2번 기둥에 있는 n-1개 원반을 다시 3번 기둥으로 옮김(1번 기둥을 보조 기둥으로 사용) 