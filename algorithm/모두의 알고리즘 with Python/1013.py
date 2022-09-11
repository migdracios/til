# 하노이 탑 알고리즘

'''
입력 : 옮기려는 원반의 개수 n
출발 기둥, 도착 기둥, 보조 기둥 변수로 사용
출력 : 원반을 옮기는 순서
'''

def hanoi(n, from_pos, to_pos, aux_pos):
    # 원반이 한 개일 경우 바로 종료
    if n == 1:
        print(from_pos, "->", to_pos)
        return
    
    # 원반이 한 개가 아닐 경우,
    # n-1개를 중간목적지인 aux_pos로 이동, to_pos를 보조로 사용
    hanoi(n-1, from_pos, aux_pos, to_pos)
    print(from_pos, "->", to_pos)
    hanoi(n-1, from_pos, to_pos, aux_pos)
    
hanoi(3,1,3,2)