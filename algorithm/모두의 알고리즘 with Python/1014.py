# 순차 탐색 알고리즘
'''
- 문제 : 
주어진 리스트에 특정한 값이 있는지 찾아 그 위치를 돌려주는 알고리즘을 만들어 보세요. 
리스트에 찾는 값이 없다면 -1을 돌려줍니다
- 입력 : 리스트, 특정 값
- 출력 : 값이 있다면 값의 인덱스, 없다면 -1
'''

'''
알고리즘 설계
1. for : 주어진 리스트를 반복해 돌면서, 값이 있는지 조회
2. if : 있다면 list.index(값) 메서드를 활용해 데이터를 리턴
3. if : 없다면 -1을 리턴
'''


def search_number(target_list, target_num):
    '''
    1. target_list, target_num을 함수의 인자로 받음
    2. target_list는 입력값, target_num는 입력값으로 지정
    3. in메서드로 target_num이 있는지 확인
    4. 있다면 해당 값의 인덱스를 return
    5. 없다면 -1 return
    '''
    
    

    if target_num in target_list:
        return target_list.index(target_num)
    return -1

# 반복문 버전
def search_num(target_list, target_num):
    for case_number in target_list:
        if case_number == target_num:
            return target_list.index(case_number)
    return -1

input_number_list = [17, 92, 18, 33, 58, 7, 33, 42]
print(search_number(input_number_list, 18))
print(search_number(input_number_list, 33))
print(search_number(input_number_list, 900))
