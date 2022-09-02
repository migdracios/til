# 🗣 모두의 알고리즘 with Python
- 마크다운 토글
```
<details>
<summary></summary>
<div markdown="1">


</div>
</details>
```


# 🎯알고리즘이란?
    
    - 어떤 문제를 풀기 위한 절차나 방법
    - 주어진 입력정보를 원하는 출력정보로 만드는 일련의 과정을 구체적이고 명료하게 적은 것

## 📜예시. 절댓값 구하기

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

## 📜예시. 1부터 n까지의 합 구하기

    



