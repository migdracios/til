# Python filter λ©μλ

# [π©λ νΌλ°μ€ λ§ν¬](https://wikidocs.net/22803)

# λͺ©μ 
    - filter λ©μλλ₯Ό μ¬μ©νμ¬ μ‘°κ±΄μ ν΄λΉνλ λ°μ΄ν° λ§μ μ λ³ν  μ μλ€.
    - filter λ©μλμμ μ¬μ©λλ lambdaμ λν΄ μ΄ν΄ν  μ μλ€.
    - filter λ©μλλ₯Ό μ¬μ©νμ¬ μ½λλ₯Ό κ°λμ± μκ² μ€μ΄λ λ¦¬ν©ν λ§ λΆμμ νκΈ° μν΄ μ°Έμ‘°νλ€.

# filter λ©μλλ₯Ό ν΅ν λ°μ΄ν° μ λ³
    - filter λ©μλλ₯Ό μ¬μ©ν΄ ν¨μλ‘ νΉμ  μ‘°κ±΄μΌλ‘ κ±Έλ¬μ§ μμλ€μ iterator κ°μ²΄λ₯Ό λ§λ€μ΄μ λ°νν©λλ€.
    - ν¨μμ κ²°κ³Όκ° μ°ΈμΈμ§ κ±°μ§μΈμ§μ λ°λΌ, ν΄λΉ μμλ₯Ό ν¬ν¨ν  μ§λ₯Ό κ²°μ ν©λλ€.

```python
a = [1,2,3,4]
result = []

def is_even(n):
    return True if n % 2 == 0 else False

result = filter(is_even, target)
print(list(result))
```
# lambda νμ
    - ν¨μλ₯Ό μΌνμ±μΌλ‘λ§ νΈμΆν  λ μ¬μ©λ¨
    - ν¨μ μ μΈμ νμν κΈ΄ μ½λλ₯Ό ν μ€λ‘ μ€μΌ μ μμ
    - filter, map λ±μ μ¬μ©λ¨

```python
def hap(x, y):
    return x + y

hap(10, 20)

###

(lambda x,y: x+y)(10, 20)
```

# νμ©
## λ°±μ€ 4344 νμ΄ μ€μμ
    - ν¨μ λ΄λΆ λ‘μ§ μ€μμ, λ¦¬μ€νΈ μμ μλ κ°μ μ‘°ννλ©΄μ νΉμ  μ‘°κ±΄μ λ§μ‘±νλ λ°μ΄ν°λ§μ μ λ³ν λ€ κ·Έ λ°μ΄ν°λ€μ κ°―μλ₯Ό λ³μλ‘ μ μΈν΄μΌ νλ μν©
    - λ°λ³΅λ¬Έμ μ¬μ©ν΄μΌλ§ νλ μν©μμ filterμ lambdaλ‘ ν μ€λ‘ μ§§κ² μ λ¦¬κ° κ°λ₯νμ

```python
count_morethan_average = len(list(filter(lambda x: x>average_num, testcase_list[0][1:])))
```
