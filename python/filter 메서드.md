# Python filter 메서드

# [🚩레퍼런스 링크](https://wikidocs.net/22803)

# 목적
    - filter 메서드를 사용하여 조건에 해당하는 데이터 만을 선별할 수 있다.
    - filter 메서드에서 사용되는 lambda에 대해 이해할 수 있다.
    - filter 메서드를 사용하여 코드를 가독성 있게 줄이는 리팩토링 분석을 하기 위해 참조했다.

# filter 메서드를 통한 데이터 선별
    - filter 메서드를 사용해 함수로 특정 조건으로 걸러진 요소들을 iterator 객체를 만들어서 반환합니다.
    - 함수의 결과가 참인지 거짓인지에 따라, 해당 요소를 포함할 지를 결정합니다.

```python
a = [1,2,3,4]
result = []

def is_even(n):
    return True if n % 2 == 0 else False

result = filter(is_even, target)
print(list(result))
```
# lambda 형식
    - 함수를 일회성으로만 호출할 때 사용됨
    - 함수 선언에 필요한 긴 코드를 한 줄로 줄일 수 있음
    - filter, map 등에 사용됨

```python
def hap(x, y):
    return x + y

hap(10, 20)

###

(lambda x,y: x+y)(10, 20)
```

# 활용
## 백준 4344 풀이 중에서
    - 함수 내부 로직 중에서, 리스트 안에 있는 값을 조회하면서 특정 조건을 만족하는 데이터만을 선별한 뒤 그 데이터들의 갯수를 변수로 선언해야 하는 상황
    - 반복문을 사용해야만 하는 상황에서 filter와 lambda로 한 줄로 짧게 정리가 가능했음

```python
count_morethan_average = len(list(filter(lambda x: x>average_num, testcase_list[0][1:])))
```
