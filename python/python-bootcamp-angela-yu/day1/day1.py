# https://replit.com/@appbrewery/band-name-generator-end // 만들게 될 프로그램 - 밴드이름 제너레이터

# https://replit.com/@appbrewery/day-1-printing-start // print() 배우기
# print("Hello World!") 
'''
print() 안에 "" 더블 쿼팅 되어 있는 내용은 프로그래밍 된 코드가 아니다. 
이런 형태의 텍스트를 Strings : 문자열(글자들의 연속적인 집합) 이라고 부른다
큰 따옴표는 문자의 시작과 끝을 알린다

이것을 빠뜨리면, 코드에 힌트가 나타나게 된다. 힌트는 금방 눈치챌 수 있을 것이다.
이럴 때 나오는 에러가 SyntaxError -> 당황하지 말고, 구글링하자
'''

# ----------------------------------------------------------------------------------------------------------------------------------------------

# TEST
'''
아래와 같이 나오도록 하시오

Day 1 - Python Print Function
The function is declared like this:
print('what to print')
'''

print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')") # 왜 작은 따옴표를 썼을까?
'''
따옴표로만 묶는다면, 모두 문자열이다. 컴퓨터는 신경쓰지 않는다.
하지만, 큰 따옴표 안에 큰 따옴표로 또 넣으려고 한다면, 제대로 작동하지 않는다. SyntaxError 발생
따옴표가 두 쌍이 총 네 개가 있다면, 우리가 원하는 사이의 문자가 아니라, 따옴표의 시작과 끝, 시작과 끝을 문자로 해석하고 나머지는 코드로 해석한다
"123"345"456"이라면, 123과 456은 문자열, 345는 코드가 되는 것이다.
따라서, 작은 따옴표가 존재하는 것이다.
'''