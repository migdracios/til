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
    hanoi(n-1, aux_pos, to_pos, from_pos)
    



def hanoi2(disk, start_post, end_post, support_post):
    # 원반 한 개
    if disk == 1:
        print(f"{start_post}-->{end_post}")
        return
    # 원반 두 개 이상
    # 마지막 원반 전까지 support_post로 이동, end_post가 보조 기둥으로 활용
    hanoi2(disk-1, start_post, support_post, end_post)
    # 마지막 원반을 end_post로 이동
    print(print(f"{start_post}-->{end_post}"))
    
hanoi2(3,1,3,2)