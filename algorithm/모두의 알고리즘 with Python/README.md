# ๐ฃ ๋ชจ๋์ ์๊ณ ๋ฆฌ์ฆ with Python
- ๋งํฌ๋ค์ด ํ ๊ธ
```
<details>
<summary></summary>
<div markdown="1">


</div>
</details>
```


# Section 01. ์๊ณ ๋ฆฌ์ฆ์ด๋?
    
    - ์ด๋ค ๋ฌธ์ ๋ฅผ ํ๊ธฐ ์ํ ์ ์ฐจ๋ ๋ฐฉ๋ฒ
    - ์ฃผ์ด์ง ์๋ ฅ์ ๋ณด๋ฅผ ์ํ๋ ์ถ๋ ฅ์ ๋ณด๋ก ๋ง๋๋ ์ผ๋ จ์ ๊ณผ์ ์ ๊ตฌ์ฒด์ ์ด๊ณ  ๋ช๋ฃํ๊ฒ ์ ์ ๊ฒ

## ๋ฌธ์ . ์ ๋๊ฐ ๊ตฌํ๊ธฐ

<details>
<summary>์๊ณ ๋ฆฌ์ฆ ์ค๊ณ</summary>
<div markdown="1">

    - 0๋ถํฐ ํน์  ์์ ํด๋นํ๋ ๊ฑฐ๋ฆฌ์ ๊ฐ์ ์๋ฏธํ๋ ์ ๋๊ฐ์ ํ๋ก๊ทธ๋๋ฐ์ผ๋ก ๊ตฌํํ์
    - ๋ฌธ์  : ์ด๋ค ์ซ์์ ์ ๋๊ฐ ๊ตฌํ๊ธฐ
    - ์๋ ฅ : ์ ๋๊ฐ์ ๊ตฌํ  ์ค์ a
    - ์ถ๋ ฅ : a์ ์ ๋๊ฐ

    <br>

    1. a๊ฐ 0๋ณด๋ค ํฌ๊ฑฐ๋ ๊ฐ์์ง ํ์ธํ๊ณ , ๊ฐ๋ค๋ฉด a๋ฅผ ๊ฒฐ๊ณผ๋ก ๋ฐํ
    2. 1์ด ์๋๋ผ๋ฉด(a๊ฐ 0๋ณด๋ค ์์ผ๋ฉด) -a๋ฅผ ๊ฒฐ๊ณผ๋ก ๋ฐํ

</div>
</details>

<details>
<summary>0101.๋ถํธ ํ๋จ</summary>
<div markdown="1">

```python
def abs_sign(a):
    if a >= 0:
        return a
    else:
        return -a


print(abs_sign(-3))
```
์์ ์๊ณ ๋ฆฌ์ฆ์ ์ค๊ณํ ๋ฐฉ์๊ณผ ๋์ผํ๊ฒ ์ฝ๋๋ฅผ ๊ตฌํ

</div>
</details>

<details>
<summary>0102. ์ ๊ณฑ๊ทผ ํ์ฉ</summary>
<div markdown="1">

```python
import math


def abs_square(a):
    b = a * a
    return math.sqrt(b)


print(abs_square(-7))
```

    - ์ค์์ ์ ๊ณฑ์๋ ์ธ์ ๋ ์์๋ผ๋ ๊ฒ์ ํ์ฉํ ์๊ณ ๋ฆฌ์ฆ.
    1. ์๋ ฅ ์๋ฅผ ์ ๊ณฑํจ
    2. ์ ๊ณฑ์๋ฅผ ์ ๊ณฑ๊ทผ์ฒ๋ฆฌํ์ฌ ๋ฐํ

    <br>

    - math ๋ผ์ด๋ธ๋ฌ๋ฆฌ๋ฅผ ํ์ฉ, math.sqrt ๋ฉ์๋๊ฐ ์ ๊ณฑ๊ทผ์ ํด๋นํจ
    - ๋ถ๊ธฐ๋ฌธ์ ์ฌ์ฉํ์ง ์๊ณ ๋ ์งํํ์ฌ ๋ชจ๋  ์ผ์ด์ค๋ฅผ ์ปค๋ฒํ๋ค๋ ์ ์ ์ฃผ๋ชฉ.

</div>
</details>

## ๋ฌธ์ . 1๋ถํฐ n๊น์ง์ ํฉ ๊ตฌํ๊ธฐ

<details>
<summary>์๊ณ ๋ฆฌ์ฆ ์ค๊ณ</summary>
<div markdown="1">

    - ๋ฌธ์  : 1๋ถํฐ n๊น์ง์ ํฉ์์ ์ด๋ค ์๊ฐ ๋ค์ด๊ฐ๋๋ผ๋ ๋์ผํ ๊ฐ์ ๊ณ์ฐํ  ์ ์์ด์ผํจ
    - ์๋ ฅ : ๋ง์ง๋ง ํฉํ  ์ซ์ 
    - ์ถ๋ ฅ : 1๋ถํฐ n๊น์ง ๋ํ ๊ฐ

    <br>

    - ์ค๊ณํ๊ธฐ
    - 1๋ํ๊ธฐ2๋ฅผ ๊ณ์ฐํ ๊ฒฐ๊ณผ๋ฅผ ์ ์ฅ, ์ ์ฅํ ๊ฒฐ๊ณผ์ 3์ ๊ณ์ฐํ ๊ฒฐ๊ณผ๋ฅผ ๋ค์ ์ ์ฅ, ...
    - ์๋ ฅํ ๋ง์ง๋ง ์ซ์๋งํผ ๋ฐ๋ณตํ๊ธฐ

</div>
</details>    

<details>
<summary>0103. ํฉ ์ ์ฅ ๋ฐฉ์</summary>
<div markdown="1">

```python
def sum_n(n):
    s = 0
    for i in range(1, n+1):
        s = s + 1
    return s
```

</div>
</details>

<details>
<summary>0104. ๊ฐ์ฐ์ค ๋ฐฉ์</summary>
<div markdown="1">

```python
def sum_n(n):
    return n * (n+1) // 2 # ์ฌ๋์ ๋ ๊ฐ(//)๋ ์ ์ ๋๋์์ ์๋ฏธ
```

</div>
</details>

## ์๋ ฅ ํฌ๊ธฐ์ ๊ณ์ฐ ํ์
    - ์๊ณ ๋ฆฌ์ฆ์์ ํ์ํ ์๋ ฅ์ ํฌ๊ธฐ๊ฐ ์ฑ๋ฅ์ ์ํฅ์ ์ฃผ๋ ๊ฒฝ์ฐ๊ฐ ์๋ค.
    - 1๋ถํฐ n๊น์ง์ ํฉ ์๊ณ ๋ฆฌ์ฆ์ ์์๋ก ๋ค์ด ๋น๊ตํด๋ณด์

### ๊ฐ ์ ์ฅ ์๊ณ ๋ฆฌ์ฆ
    - ๊ฐ ์ ์ฅ ์๊ณ ๋ฆฌ์ฆ์ ์๋ ฅํ ๊ฐ ๋งํผ 1๋ถํฐ ํ๋์ฉ ๊ฐ์ ๋ํด๊ฐ๋ฉด์ ์ ์ฅํ๋ ๋ฐฉ์์ผ๋ก ๋ก์ง์ด ์ค๊ณ๋์ด ์๋ค.
    - ์์ ์ซ์์ ๊ฒฝ์ฐ์๋ 1๋ถํฐ 10๊น์ง ์ด 10๋ฒ์ ์ฐ์ฐ์ ํ๊ฒ ๋์ง๋ง 1000์ ์๋ ฅํ๋ค๋ฉด 1000๋ฒ ์ฐ์ฐ๋์ด์ผ ํ๋ค.
    - ๊ฐ ์ ์ฅ ์๊ณ ๋ฆฌ์ฆ์ n๋ฒ์ ์ฐ์ฐํ๋ ์๊ณ ๋ฆฌ์ฆ์ด๋ค.
### ๊ฐ์ฐ์ค ๋ฐฉ๋ฒ
    - ๊ฐ์ฐ์ค ๋ฐฉ๋ฒ์ 1๋ถํฐ n๊น์ง์ ํฉ๊ณผ ๊ด๋ จ๋ ์์์ ์๊ณ ๋ฆฌ์ฆ์ ์ ์ฉํ๋ ๋ฐฉ๋ฒ์ด๋ค.
    - n * (n+1) / 2 ๋ ๊ณฑํ๊ธฐ, ๋ํ๊ธฐ, ๋๋๊ธฐ ์ฐ์ฐ์ผ๋ก ๊ตฌ์ฑ๋์ด ์๋ค.
    - ์ด๋ค ์ซ์๊ฐ ๋ค์ด์ค๋๋ผ๋ ๊ฐ์ฐ์ค ๋ฐฉ๋ฒ ์๊ณ ๋ฆฌ์ฆ์ 3๋ฒ์ ์ฐ์ฐํ๋ ์๊ณ ๋ฆฌ์ฆ์ด๋ค.

## ๋น์ค ํ๊ธฐ๋ฒ
    - ์ด๋ค ์๊ณ ๋ฆฌ์ฆ์ด ๋ฌธ์ ๋ฅผ ํ๊ธฐ ์ํด ์ฐ์ฐ์ ๋ณต์กํจ์ ์ ๋๋ก ๋ํ๋ธ ๊ฒ์ ๋ณต์ก๋(Complexity)๋ผ๊ณ  ํ๋ค.
    - ๋ณต์ก๋๋ฅผ ํํํ๋ ๋ฐฉ๋ฒ ์ค์ ๊ฐ์ฅ ๋ฒ์ฉ์ ์ผ๋ก ์ฌ์ฉํ๋ ๊ฒ์ด ๋น์ค(Big O) ํ๊ธฐ๋ฒ์ด๋ค.
    - ๊ณ์ฐ์ ํ์์์ฒด๋ ์๋ฏธ๊ฐ ์๋์ ์ผ๋ก ์ ์ผ๋ฏ๋ก n,n์ ๊ณฑ, 1๊ณผ ๊ฐ์ด ์ถ์ฝํ์ฌ ํํํ๋ค
    - ๊ฐ ์ ์ฅ ์๊ณ ๋ฆฌ์ฆ์ n๋ฒ ์ฐ์ฐํ๋ฏ๋ก O(n)์ผ๋ก ํํํ๋ค. 
    - ๊ฐ์ฐ์ค ๋ฐฉ๋ฒ์ ๊ฒฝ์ฐ 3๋ฒ ์ฐ์ฐํ๋ฏ๋ก O(3)์ผ๋ก ํํํ๋, ์์๋ ์๋ฏธ๊ฐ ๋์ผํ๋ฏ๋ก O(1)๋ก ํต์ผํ๋ค.
    - ๋น์คํ๊ธฐ๋ฒ์ผ๋ก ์๊ณ ๋ฆฌ์ฆ์ ๋ณต์ก๋๋ฅผ ํ์ํ๊ณ , ์ฐ์ฐ์๋๊ฐ ๋น ๋ฅธ ์๊ณ ๋ฆฌ์ฆ์ ์ฑํํ  ์ ์์ด์ผ ํ๋ค.
    - ๋จ์ํ ์๊ณ ๋ฆฌ์ฆ์ ์ค๊ณํ๊ณ  ๊ตฌํํ๋ ๊ฒ์ ๋ฉ์ถ๋ ๊ฒ์ด ์๋๋ผ, ์ค์ ๋ก ์๋ํ๋ ์๋๊ฐ ๋น ๋ฅธ์ง์ ๋ํ ๊ณ ๋ฏผ์ ํด์ผํ๋ค!

## ๋ฌธ์ . ์ต๋๊ฐ ์ฐพ๊ธฐ
    
<details>
<summary>์๊ณ ๋ฆฌ์ฆ ์ค๊ณ</summary>
<div markdown="1">

- ๋ฌธ์  : ์ฃผ์ด์ง n๊ฐ์ ์ซ์ ์ค์์ ๊ฐ์ฅ ํฐ ์๋ฅผ ์ฐพ์์ผ ํ๋ค.
- ์๋ ฅ : n๊ฐ ๋งํผ์ ์ซ์๋ฅผ ๊ฐ์ง ๋ฆฌ์คํธ
- ์ถ๋ ฅ : ๋ฆฌ์คํธ ์ค์ ๊ฐ์ฅ ํฐ ์
- ์ค๊ณ : ๋ฆฌ์คํธ์ ์ฒ์ ์ซ์๋ถํฐ ํ๋์ฉ ๋น๊ตํด ๋ณด๋ ๊ฒ์ ์ด๋จ๊น?

</div>
</details>

<details>
<summary>0105. ๊ฐ ์ ์ฅ ์๊ณ ๋ฆฌ์ฆ</summary>
<div markdown="1">

```python
def find_maxnum(numlist):
    '''
    1. ์ต๋๊ฐ์ ์ซ์๋ฆฌ์คํธ์ ์ฒซ๋ฒ์งธ ๊ฐ์ผ๋ก ๋ณ์ ์ง์ 
    2. ์ซ์๋ฆฌ์คํธ ๊ธธ์ด๋งํผ ๋ฐ๋ณต
    3. ์ซ์๋ฆฌ์คํธ[์ธ๋ฑ์ค] ๊ฐ์ด ์ต๋๊ฐ๋ณด๋ค ํด ๊ฒฝ์ฐ, ์ต๋๊ฐ์ผ๋ก ๋ณ๊ฒฝ
    4. ์๋ ๊ฒฝ์ฐ, ๊ทธ๋๋ก ์งํ
    5. ๋ฐ๋ณต๋ฌธ์ด ์ข๋ฃ๋ ์ดํ ์ต๋๊ฐ ๋ฆฌํด
    '''
    maxnum = numlist[0]

    for i in range(len(numlist)):
        if numlist[i] > maxnum:
            maxnum = numlist[i]
    return maxnum

test_list = [1,2,3,4,5,10,7]
print(find_maxnum(test_list))
```

    - ๋ฐ๋ณต๋ฌธ ๋งํผ ์ฐ์ฐ์ ๋ฐ๋ณตํ๋ฏ๋ก ๋ณต์ก๋๋ O(n)

</div>
</details>

<details>
<summary>0106. ์ต๋๊ฐ์ ์์น ์ฐพ๊ธฐ ์๊ณ ๋ฆฌ์ฆ</summary>
<div markdown="1">

```python
def find_maxnum_index(numlist):
    '''
    1. ์ต๋๊ฐ ๋ณ์ ์ ์ฅ
    2. ์ต๋๊ฐ์ ์์น ๋ณ์ ์ ์ฅ
    3. ์ซ์๋ฆฌ์คํธ๋งํผ ๋ฐ๋ณต๋ฌธ ์์ฑ
    4. ์ต๋๊ฐ๊ณผ ์ซ์๋ฆฌ์คํธ[์ธ๋ฑ์ค] ๊ฐ ๋น๊ต
    5. ๊ฐ์ด ํฌ๋ค๋ฉด ์ต๋๊ฐ ์ ์ฅ
    6. ์ต๋๊ฐ ์์น ๋ณ์๋ฅผ ์ธ๋ฑ์ค ๊ฐ์ผ๋ก ๋ณ๊ฒฝ
    7. ์๋๋ผ๋ฉด, ๊ทธ๋๋ก ์งํ
    8. ์ต๋๊ฐ ์์น ๋ณ์ ๋ฐํ
    '''
    maxnum = numlist[0]
    maxnum_index = 0
    for i in range(len(numlist)):
        if numlist[i] > maxnum:
            maxnum = numlist[i]
            maxnum_index = i
    return maxnum_index

test_list = [1,3,5,2,4,9,6,8]
print(find_maxnum_index(test_list))
```

- ์ญ์ ๋ฐ๋ณต๋ฌธ๋งํผ ์ฐ์ฐํด์ผ ํ๋ฏ๋ก O(n) ๋งํผ์ ๋ณต์ก๋๋ฅผ ๋ํ๋ธ๋ค

</div>
</details>

## ๋ฌธ์ . ๋๋ช์ด์ธ ๊ตฌํ๊ธฐ

    - ๋ฌธ์  : n๋ช์ ์ฌ๋๋ค ์ค์ ๊ฐ์ ์ด๋ฆ์ ๊ฐ์ง ์ฌ๋์ ์งํฉ์ผ๋ก ๋ง๋ค์ด๋ผ
    - ์๋ ฅ : ์ฌ๋ ์ด๋ฆ์ ๊ฐ์ผ๋ก ๊ฐ์ง๊ณ  ์๋ n๊ฐ์ ๋ฆฌ์คํธ
    - ์ถ๋ ฅ : ๊ฐ์ ์ด๋ฆ์ ์ฌ๋์ ๊ฐ์ง๊ณ  ์๋ ์งํฉ

<br>

    - ๊ฐ์ ๊ฐ์ ์ฐพ์๋ด๊ธฐ ์ํด์๋ ๋ฆฌ์คํธ์ ๊ฐ์ ๋์๊ฐ๋ฉด์ ๊ฐ์ ๋ฆฌ์คํธ ์์ ๊ฐ๊ณผ ๋น๊ตํด์ผ ํ๋ค.
    - ๋น๊ต๊ฐ ๋๋ฌ๋ค๋ฉด ๋ค์ ๊ฐ๋ ๋ฆฌ์คํธ์ ๊ฐ์ ๋์๊ฐ๋ฉด์ ๋น๊ตํด์ผ ํ๋ค.

<details>
<summary>๋๋ช์ด์ธ ์ฐพ๊ธฐ ์๊ณ ๋ฆฌ์ฆ</summary>
<div markdown="1">

```python
def find_sameone(list_people):
    '''
    5๊ฐ์ ์ด๋ฆ์ด ๋ค์ด์๋ ๋ฆฌ์คํธ
    1. ๋ฆฌ์คํธ์ ๊ธธ์ด๋ฅผ ๋ณ์์ ์ ์ฅ
    2. ๊ฒฐ๊ณผ๋ฅผ ์ ์ฅํ  ๋น ์งํฉ
    3. 0๋ถํฐ n-2๊น์ง ๋ฐ๋ณต -> ๋ชจ๋ ๋น๊ตํ์ผ๋ ๋งจ๋์ ๋น๊ตํ  ํ์๊ฐ ์๊ธฐ ๋๋ฌธ
    4. i+1 ๋ถํฐ n-1๊น์ง ๋ฐ๋ณต -> ๋น๊ต๋์1์ ์ฒ์๋ถํฐ, ๋น๊ต๋์2๋ ๊ทธ ๋ค์๋ถํฐ์ด๊ธฐ ๋๋ฌธ
    5. a[i]์ a[j]๊ฐ ๊ฐ๋ค๋ฉด, ์ด๋ฆ์ ๊ฒฐ๊ณผ ์งํฉ์ ์ ์ฅ
    '''
    len_list = len(list_people)
    sameone = set()
    for i in range(0, len_list-1):
        for j in range(i+1, len_list):
            if list_people[i] == list_people[j]:
                sameone.add(list_people[i])
    return sameone

test_list = ["ํฉ์์", "๊นํฌ์ ", "ํ๊ฑดํฌ", "๊นํ์ธ", "ํฉ์์"]
print(find_sameone(test_list))
```

</div>
</details>

# ์ฌ๊ท ํธ์ถ

    - ์ฌ๊ทํธ์ถ์ ํจ์ ์์์ ๋ค์ ํจ์๋ฅผ ํธ์ถํ๋ ํ์
    - ๋งํธ๋ฃ์์นด์ฒ๋ผ ์ธํ ์์ ์ธํ์ด ์๋ ๊ฒ์ฒ๋ผ 

## ๋ฌธ์ . ํฉํ ๋ฆฌ์ผ ๊ตฌํ๊ธฐ

    - ๋ฌธ์  : 1๋ถํฐ n๊น์ง์ ์ฐ์ํ ์ซ์๋ฅผ ๊ณฑํ๊ธฐ
    - ์๋ ฅ : ๋ง์ง๋ง ์ซ์ n
    - ์ถ๋ ฅ : 1๋ถํฐ n๊น์ง์ ์ซ์ ๊ณฑ

    <br>

    - ๊ฐ์ ์ ์ฅํด์ 1๋ถํฐ ๋ง์ง๋ง ์ซ์๊น์ง ๊ณฑํ ๊ฐ์ ์ ์ฅ, ๊ณฑํ๊ธฐ๋ฅผ ๋ฐ๋ณตํ๊ธฐ
    - O(n)์ ๋ณต์ก๋๊ฐ ํ์ํ๋ค

<details>
<summary>ํฉํ ๋ฆฌ์ผ ์๊ณ ๋ฆฌ์ฆ</summary>
<div markdown="1">

```python
def fact(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f
    
test_num = 3
print(fact(test_num)) 
```

</div>
</details>

## ๋ฌธ์ . ์ฌ๊ท ํธ์ถ
    - ๋ฌธ์  : ํจ์ ์์์ ํจ์๋ฅผ ํธ์ถํ์
    - ์๋ ฅ : ์์
    - ์ถ๋ ฅ : ์์

<details>
<summary>๋ฌดํ ํฌ๋ก</summary>
<div markdown="1">

```python
def inf_hello():
    print("hello")
    inf_hello()
inf_hello()
```

```shell
RecursionError: maximum recursion depth exceeded while calling a Python object
```

    - ํจ์๋ฅผ ์คํํ๋ฉด, ํจ์ ์์ ํจ์๋ฅผ ์คํํ๋ ๊ฒ์ ๋ฐ๋ณตํ๋ ๊ฒ์ด ๋๋์ง ์์ ๋ฐ์ํ๋ ์ค๋ฅ ๋ฉ์์ง

</div>
</details>

## ๋ฌธ์ . ์ต๋๊ณต์ฝ์ ๊ตฌํ๊ธฐ
    - ๋ฌธ์  : ๋ ๊ฐ์ ์ ์์ ์ต๋๊ณต์ฝ์๋ฅผ ๊ตฌํ๊ธฐ
    - ์๋ ฅ : ๋ ๊ฐ์ ์
    - ์ถ๋ ฅ : ๋ ์์ ์ต๋๊ณต์ฝ์

<br>

    - ๋ ์ ์ค ๋ ์์ ๊ฐ์ ๋ณ์๋ก ์ ์ฅ
    - ๋ณ์๋ก ๋ ์๊ฐ ๋ชจ๋ ๋๋ ์ง๋์ง ๊ฒ์ฌ
    - ์๋๋ผ๋ฉด ๋ณ์๋ฅผ 1๊ฐ์ ํ ๊ฒ์ฌ ๋ฐ๋ณต
    - ๋ง๋ค๋ฉด ํด๋น ์๋ฅผ ๋ฆฌํด

<details>
<summary>๊ฐ ์ ์ฅ ์๊ณ ๋ฆฌ์ฆ</summary>
<div markdown="1">

```python
def find_gcd(num1, num2):
    target_number = num1 if num1 > num2 else num2
    while target_number != 1:
        if num1 % target_number == 0 and num2 % target_number == 0:
            return target_number
        target_number -= 1

num1, num2 = 20, 12
print(find_gcd(num1,num2))
```

</div>
</details>

    - ์ ํด๋ฆฌ๋ ์๊ณ ๋ฆฌ์ฆ
    - ์ต๋๊ณต์ฝ์(a, b) = ์ต๋๊ณต์ฝ์(b, b%a) ์ด๋ค
    - ์ด๋ค ์์ 0์ ์ต๋๊ณต์ฝ์๋ ์๊ธฐ์์ ์ด๋ฏ๋ก ์ต๋๊ณต์ฝ์(a, 0) = a
    - ์ ๋ฒ์น๊ณผ ์ฌ๊ทํธ์ถ์ ์ฌ์ฉํ์ฌ ๋ฐ๋ณตํด์ ๋ฌธ์ ๋ฅผ ํ์ด

<details>
<summary>์ ํด๋ฆฌ๋ ์ต๋๊ณต์ฝ์ ์๊ณ ๋ฆฌ์ฆ</summary>
<div markdown="1">

```python
def find_gcd(num1, num2):
    min_num = min(num1, num2)
    max_num = max(num1, num2)
    if min_num == 0:
        return max_num
    # ํจ์๋ฅผ ์คํํ๊ณ  ๋๋๋๊ฒ ์๋๋ผ ํจ์๋ฅผ ์ธ์๋ฅผ ๋ฃ์ด ๋ฐํํด์ผ ํ๋ค!
    return find_gcd(min_num, max_num % min_num)
    
test1, test2 = 60, 24
result = find_gcd(test1, test2)
print(result)
```

    - ํธ๋ฌ๋ธ์ํ : ์ฌ๊ทํจ์๋ ํจ์๋ฅผ ์ฌ๊ทํธ์ถ ํ  ๋ ๋ฐํํ๋ ๊ฒ์ผ๋ก ์๋ํ๋ค

</div>
</details>

## ๋ฌธ์ . ํ๋ธ์ดํ
    - [LINK](https://www.youtube.com/watch?v=uSSC0aKXbWQ)
    - ๋ฌธ์  : ํ ๋ฒ์ ์ฎ๊ธธ ์ ์๋ ์๋ฐ์ ์์ ์๋ฐ ์์ ๋์ง ์์ผ๋ฉด์ n๊ฐ์ ์๋ฐ ๋ชจ๋ ๋ง์ง๋ง ๊ธฐ๋ฅ์ผ๋ก ์ฎ๊ธฐ์์ค
    - ์๋ ฅ : ์ฎ๊ธฐ๋ ค๋ ์๋ฐ n๊ฐ
    - ์ถ๋ ฅ : ์๋ฐ์ ์ฎ๊ธฐ๋ ์์

### ์๋ฐ์ด ๋ ๊ฐ์ผ ๊ฒฝ์ฐ
    0. ์ฒซ ๋ฒ์งธ ๊ธฐ๋ฅ์ ๋ ๊ฐ์ ์๋ฐ์ด ๋์ฌ์๋ค
    1. ์์ ์๋ฐ์ ๋ ๋ฒ์งธ ๊ธฐ๋ฅ์ผ๋ก ์ด๋ํ๋ค
    2. ํฐ ์๋ฐ์ ์ธ ๋ฒ์งธ ๊ธฐ๋ฅ์ผ๋ก ์ด๋ํ๋ค. ์์ ์๋ฐ ํ๋๋ง ์ด๋ํ๋ฉด ๋๋๋ค(์ข๋ฃ์กฐ๊ฑด)
    3. ์์ ์๋ฐ์ ์ธ ๋ฒ์งธ ๊ธฐ๋ฅ์ผ๋ก ์ด๋ํ๋ค(๋)
### ์๋ฐ์ด ์ธ ๊ฐ์ผ ๊ฒฝ์ฐ
    0. ์ฒซ ๋ฒ์งธ ๊ธฐ๋ฅ์ ์ธ ๊ฐ์ ์๋ฐ์ด ๋์ฌ์๋ค
    1. ์์ ์๋ฐ์ ์ธ ๋ฒ์งธ ๊ธฐ๋ฅ์ผ๋ก ์ด๋ํ๋ค
    2. ์ค๊ฐ ์๋ฐ์ ๋ ๋ฒ์งธ ๊ธฐ๋ฅ์ผ๋ก ์ด๋ํ๋ค
    3. ์์ ์๋ฐ์ ๋ ๋ฒ์งธ ๊ธฐ๋ฅ์ผ๋ก ์ด๋ํ๋ค(์๋ฐ ๋ ๊ฐ์ ๊ฒฝ์ฐ ์ข๋ฃ)
    4. ํฐ ์๋ฐ์ ์ธ ๋ฒ์งธ ๊ธฐ๋ฅ์ผ๋ก ์ด๋ํ๋ค
    5. ์์ ์๋ฐ์ ์ฒซ ๋ฒ์งธ ๊ธฐ๋ฅ์ผ๋ก ์ด๋ํ๋ค
    6. ์ค๊ฐ ์๋ฐ์ ์ธ ๋ฒ์งธ ๊ธฐ๋ฅ์ผ๋ก ์ด๋ํ๋ค. ์์ ์๋ฐ ํ๋๋ง ์ด๋ํ๋ฉด ๋๋๋ค(์ข๋ฃ์กฐ๊ฑด)
    7. ์์ ์๋ฐ์ ์ธ ๋ฒ์งธ ๊ธฐ๋ฅ์ผ๋ก ์ด๋ํ๋ค(๋)

### ์๊ณ ๋ฆฌ์ฆ ์์ฝ
    1. ์๋ฐ์ด ํ ๊ฐ๋ฉด ์ฎ๊ธฐ๋ฉด ๋(์ข๋ฃ์กฐ๊ฑด)
    2. ์๋ฐ์ด n ๊ฐ์ผ๋, 
        - 1๋ฒ ๊ธฐ๋ฅ์ ์๋ n๊ฐ์ ์๋ฐ ์ค n-1๊ฐ๋ฅผ 2๋ฒ ๊ธฐ๋ฅ์ผ๋ก ์ฎ๊น(3๋ฒ ๊ธฐ๋ฅ์ ๋ณด์กฐ ๊ธฐ๋ฅ์ผ๋ก ์ฌ์ฉ)
        - 1๋ฒ ๊ธฐ๋ฅ์ ๋จ์ ์๋ ๊ฐ์ฅ ํฐ ์๋ฐ์ 3๋ฒ ๊ธฐ๋ฅ์ผ๋ก ์ฎ๊น
        - 2๋ฒ ๊ธฐ๋ฅ์ ์๋ n-1๊ฐ ์๋ฐ์ ๋ค์ 3๋ฒ ๊ธฐ๋ฅ์ผ๋ก ์ฎ๊น(1๋ฒ ๊ธฐ๋ฅ์ ๋ณด์กฐ ๊ธฐ๋ฅ์ผ๋ก ์ฌ์ฉ) 
