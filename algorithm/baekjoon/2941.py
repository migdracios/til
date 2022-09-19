# 크로아티아 알파벳 알고리즘

'''
문제

크로아티아 알파벳	변경
č	c=
ć	c-
dž	dz=
đ	d-
lj	lj
nj	nj
š	s=
ž	z=

예를 들어, ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다. 
단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다. 
lj와 nj도 마찬가지이다. 
위 목록에 없는 알파벳은 한 글자씩 센다.

입력
ljes=njak
ddz=z=
nljj
c=c=

출력
6
3
3
2
'''

'''
알고리즘 설계
1. 크로아티아 알파벳을 리스트로 저장
2. in 메서드로 조회 및 카운트를 하는 함수 생성
3. 문자를 조회하고 카운트 체크 및 문자를 제거, 재귀함수 호출
'''
alphabet_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
count = 0


def num_croatia(text, count):
    '''
    함수 설계
    1. 문자열과 카운트를 인자로 호출됨
    2. for : 문자를 in 메서드로 특정 크로아티아 알파벳이 있는지 조회
    3. if : 있다면 해당 문자를 replace로 공백으로 만듦, 바뀐 문자와 count+1을 인자로 재귀호출
    4. if : 문자열에 더 이상 크로아티아 문자가 없어 반복문이 종료된 경우
    5. 문자열의 공백을 strip으로 제거한 뒤 len 메서드의 길이만큼 카운트에 추가, 카운트 return
    # '''
    if text.strip(" ") is None:
        return count
    for croatia_alphabet in alphabet_list:
        if croatia_alphabet in text:
            return num_croatia(text.replace(croatia_alphabet, " ", 1), count+1)
    count += len(text.replace(" ", ""))
    return count


input_text = input()
print(num_croatia(input_text, count))


'''
트러블슈팅
1. 반복문이 끝나도 문자열이 남아있음 -> 반복문이 끝난 이후 문자열의 길이만큼 카운트 해줌
2. 문자열을 제거했는데 그냥 알파벳+크로아티아 알파벳의 조합으로 크로아티아 알파벳이 되어버린 경우
-> 제거된 문자열을 공백으로 대체해서 합쳐지는 케이스 해결
3. 같은 문자열이 여러 개 있는 경우 한 번이 아니라 여러개를 삭제해버림 -> replace 세 번째 인자로 횟수를 1회로 고정
'''
