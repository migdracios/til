# Python list 자료형 원소 삭제

# [🚩레퍼런스 링크](https://wikidocs.net/16040)

# 목적
    - list 자료형을 삭제하는 방법은 del 키워드를 사용하여 데이터를 삭제할 수 있다.
    - 특정 인덱스의 자료형을 찾아 그것만 삭제하기 위해서 참조했다.
    
## del 키워드를 통한 삭제
    - del 리스트이름[인덱스번호] 와 같이 코딩하여 특정 인덱스 번호의 자료를 제거할 수 있다.

```python
a = [1,2,3,4,5,6,7]
del a[1]
print(a) # --> [1,3,4,5,6,7]
```

# 활용
## 백준 4344번 풀이 중에서
    - 함수 내부 로직 중에서, 0번째를 자꾸 쓰게 되는 재귀호출 알고리즘을 설계
    - 0번째라는 인덱스를 변하게 하지 않을 것이므로 0번째 값을 빼주면서 반복할 의도
    - 0번째 값을 del 키워드로 삭제 후 재귀호출
```python
def find_avg_per(testcase_list):
    if testcase_list == [] : return
    average_num = sum(testcase_list[0][1:]) / testcase_list[0][0]
    count_morethan_average = len(list(filter(lambda x: x>average_num, testcase_list[0][1:])))
    average_per = count_morethan_average / testcase_list[0][0]
    print(f"{average_per*100:.3f}%")
    del testcase_list[0]
    return find_avg_per(testcase_list)
```