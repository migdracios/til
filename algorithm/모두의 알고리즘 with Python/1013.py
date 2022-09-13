# 하노이 탑 알고리즘

'''
입력 : 옮기려는 원반의 개수 n
출발 기둥, 도착 기둥, 보조 기둥 변수로 사용
출력 : 원반을 옮기는 순서
'''

# 정답
def hanoi(n, from_pos, to_pos, aux_pos):
    if n == 1:
        print(from_pos, "->", to_pos)
        return

    # n이 1이 아니라면, 여기로 내려옴    
    hanoi(n-1, from_pos, aux_pos, to_pos)
    # 함수를 반복 실행해서 return을 했을 때, 여기로 내려옴
    print(from_pos, "->", to_pos)
    # 나머지 원반을 목적지로 옮기는 재귀
    hanoi(n-1, aux_pos, to_pos, from_pos)
    



    