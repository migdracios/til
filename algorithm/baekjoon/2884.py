# 알람시계 알고리즘

'''
- 문제 : 원래 설정할 시간을 설정하면 45분 일찍 울리는 알람시계
- 입력 : 시각과 분을 각각 공백을 간격으로 입력
- 출력 : 45분 빠른 시각과 분을 각각 공백 간격으로 출력
'''

def alarm(hour, minute):
    '''
    1. 분에 15를 더한다.
    2. 시각에 1을 뺀다.
    3. 만약 숫자가 0이라면, 24로 변경
    '''
    minute += 15
    if hour == 0:
        hour = 24
    hour -= 1
    print(hour,minute)
    
hr, min = map(int, input().split())
alarm(hr, min)
    
    
    