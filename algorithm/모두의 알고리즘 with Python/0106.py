# 최댓값 알고리즘
## 값 위치 찾기

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