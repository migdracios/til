# 최대공약수 알고리즘
# 값 비교

def find_gcd(num1, num2):
    # target_number = num1 if num1 > num2 else num2
    target_number = min(num1, num2)
    while target_number != 1:
        if num1 % target_number == 0 and num2 % target_number == 0:
            return target_number
        target_number -= 1

num1, num2 = 20, 12
print(find_gcd(num1,num2))
     