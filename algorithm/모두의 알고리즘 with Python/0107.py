# 동명이인 찾기 알고리즘
## 값 저장 비교 알고리즘

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
                
        
    