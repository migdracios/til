# 최댓값 찾기
# 단순 비교 알고리즘

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
