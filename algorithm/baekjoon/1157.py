# 최빈값 알고리즘

'''
- 문제 : 
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
- 입력 : 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
- 출력 : 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
'''
  
'''
알고리즘 설계
1. 문자열을 입력 받음
2. 입력 받은 문자열을 대문자로 변환(대소문자를 구분하지 않기 때문)
3. 알파벳의 길이 만큼의 0이 담겨있는 리스트를 선언
4. for 입력받은 문자열을 반복하면서 ord 메서드를 활용하여 해당 알파벳 숫자 인덱스에 카운트
5. max 메서드를 사용하여 리스트 내의 최빈 횟수를 변수에 선언
6. 같은 횟수의 최빈값을 감안하여 빈 리스트 선언
7. for if 알파벳 리스트를 enumerate로 반복하여 리스트 내부 값이 최빈 횟수와 같다면
8. 그 인덱스 번호를 최빈값 리스트에 저장
9. if 리스트의 길이가 2 이상이라면, ?를 출력
10. 아니라면 리스트 0번째 값을 chr, ord 메서드를 활용하여 알파벳을 대문자로 출력
'''

text = input()
text = text.upper()
list_alpha = [0] * 26

for i in text:
    i = ord(i) - ord("A")
    list_alpha[i] += 1
    
maxnum = max(list_alpha)
maxnum_list = []
for i,count in enumerate(list_alpha):
    if count == maxnum:
        maxnum_list.append(list_alpha.index(count))
        
print("?") if len(maxnum_list) >= 2 else print(chr(ord("A")+maxnum_list[0]))