# 평균은 넘겠지 알고리즘

'''
문제
---
대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.

첫째 줄에는 테스트 케이스의 개수 C가 주어진다.

둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.
---
입력 
5
5 50 50 70 80 100
7 100 95 90 80 70 60 50
3 70 90 80
3 70 90 81
9 100 99 98 97 96 95 94 93 91
출력
40.000%
57.143%
33.333%
66.667%
55.556%
'''

'''
알고리즘 로직 설계

1. 테스트케이스의 수를 입력받음
2. 테스트케이스를 모두 담을 빈 리스트 선언
3. 테스트케이스 번호를 인자로 담아 저장함수 호출
4. 입력 받은 테스트케이스 수만큼 저장 함수를 재귀호출하여 리스트 저장
5. 리스트를 인자로 담아 출력함수를 호출하고 하나씩 pop하면서 재귀호출해 결과를 프린트
'''

# 테스트케이스 리스트 저장 함수
def save_score_list(testcase_num, testcase_list):
    '''
    1. 테스트케이스 수, 빈 리스트를 인자로 받음
    2. 테스트케이스의 수 만큼 반복해서 리스트에 어펜딩해야하므로 테스트케이스 수가 0이 되면 리스트를 리턴, 아니면 재개
    3. 인자로 받은 리스트에 테스트케이스를 입력받아 어펜딩
    4. 테스트케이스 수를 1 감소시키고 데이터가 들어간 리스트를 담아 재귀호출
    '''
    if testcase_num == 0 : return testcase_list
    testcase_list.append(list(map(int, input().split())))
    return save_score_list(testcase_num-1, testcase_list)   


# 테스트케이스 평균 비율 출력 함수
def find_avg_per(testcase_list):
    '''
    1. 테스트케이스가 모두 담긴 리스트만 입력 받음
    2. 테스트케이스의 0번째 리스트를 호출해 리스트(처음부터 0번째 인덱스까지)의 합 / 0번째 인덱스로 평균값 계산
    3. 계산한 평균 값을 조건으로 filter하여 평균 값을 넘는 데이터만 선별
    4. 선별한 데이터 / 0번째 인덱스로 평균 비율 계산
    5. fstring을 활용하여 3번째 자릿수까지 퍼센테이지로 출력
    '''
    if testcase_list == [] : return
    average_num = sum(testcase_list[0][1:]) / testcase_list[0][0]
    count_morethan_average = len(list(filter(lambda x: x>average_num, testcase_list[0][1:])))
    '''for testcase in testcase_list[0][1:]:
        if testcase > average_num:
            count_morethan_average += 1'''
    average_per = count_morethan_average / testcase_list[0][0]
    print(f"{average_per*100:.3f}%")
    del testcase_list[0]
    return find_avg_per(testcase_list)
    
testcase_num = int(input())
testcase_list = save_score_list(testcase_num, testcase_list=[])
find_avg_per(testcase_list)