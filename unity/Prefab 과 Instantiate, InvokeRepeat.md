# ๐ฉPrefab๊ณผ Instantiate, InvokeRepeat.md
- Unity์ ํ๋ฆฌํน ์์คํ์ ์ด์ฉํ๋ฉด **๊ฒ์ ์ค๋ธ์ ํธ๋ฅผ ์์ฑ, ์ค์  ๋ฐ ์ ์ฅํ  ์ ์์ผ๋ฉฐ, ํด๋น ๊ฒ์ ์ค๋ธ์ ํธ์ ๋ชจ๋  ์ปดํฌ๋ํธ, ํ๋กํผํฐ ๊ฐ, ์์ ๊ฒ์ ์ค๋ธ์ ํธ๋ฅผ ์ฌ์ฌ์ฉ ๊ฐ๋ฅํ ์์์ผ๋ก ๋ง๋ค ์ ์๋ค.** 
- ๋ฏธ๋ ํ๋ก์ ํธ์์ ํจ์๋ฅผ ํ์ฉํ์ฌ ํ๋ฆฌํน์ ์ ์ฉํ๋ ๋ฐฉ๋ฒ์ ์์๋ก ์ถ๊ฐ

<br>

## ๐พ๋ฏธ๋ํ๋ก์ ํธ. ๋น๋ฌผ๋ฐ๊ธฐ๊ฒ์
    - ๋น๋ฌผ์ ๋ฐ์๋ด๋ฉด ์ ์๋ฅผ ํ๋ํ๋ ๊ฒ์ ์์คํ์์ ๋น๋ฐฉ์ธ ์คํ๋ผ์ดํธ๋ฅผ ์์ฑ
    - ๋น๋ฐฉ์ธ ์คํ๋ผ์ดํธ๋ฅผ ํ ๊ฐ๊ฐ ์๋, ์ฌ๋ฌ ๊ฐ๋ก ์นดํผํ๊ธฐ ์ํด์๋ ํ๋ฆฌํน๊ณผ ์ธ์คํด์์์ดํธ๊ฐ ํ์
    
<br>
    
### โPrefab ๋ง๋ค๊ธฐ
1. ์์ฑํ ์คํ๋ผ์ดํธ๋ฅผ ์์ ํด๋์์ ์๋ก์ด ๋๋ ํ ๋ฆฌ prefab์ ๋ง๋ค๊ธฐ
2. prefab ํด๋์ ์คํ๋ผ์ดํธ๋ฅผ ๋๋๊ทธ์ค ๋๋กญ

### โInstantiate ํ๊ธฐ
1. gameManager ์ค๋ธ์ ํธ์ ์ฝ์๋ gameManager.cs ์คํฌ๋ฆฝํธ๋ฅผ ์ด์ด ์ฝ๋๋ฅผ ์์ฑํ๋ค
2. makeRain ํจ์๋ฅผ ๋ง๋ค์ด Instantiate ํจ์๋ฅผ ๋ด์ ํจ์๋ฅผ ์์ฑ
3. Instantiate ํจ์๋ก ๋น๋ฐฉ์ธ ์คํ๋ผ์ดํธ๋ฅผ ์์ฑํ๋ค
 

### โInvokeRepeat ํจ์๋ก ๋ฐ๋ณต ํธ์ถํ๊ธฐ
1. InvokeRepeat("ํธ์ถํ  ํจ์ ์ด๋ฆ", 0, ๊ฐ๊ฒฉ ์๊ฐ); ์ ์ฌ์ฉํ์ฌ Instantiate ํจ์๋ฅผ ๋ฐ๋ณต ํธ์ถํ๋ค

<br>

## ๐ฅํธ๋ฌ๋ธ ์ํ. ํจ์ ํธ์ถ ์์น ํ์ธํ๊ธฐ!
    - ํท๊ฐ๋ฆฌ์ง ๋ง์์ผ ํ  ์ ์ Instantiate ํ  ํจ์๋ฅผ ๋ง๋ค๊ณ , InvokeRepeat ํจ์์์ ํด๋น ํจ์๋ฅผ ํธ์ถํด์ผ ํจ
    - update ํจ์์ Instantiate ํจ์๋ฅผ ํธ์ถํ๋ค๋ฉด, ํ๋ ์ ๋ณ๋ก ๊ฐ์ฒด ์์ฑ์ ๋ฐ๋ณต ์คํํ๋ฏ๋ก ์๋ฅด๋ฅด ๋น๋ฐฉ์ธ์ด ์์์ง
    
<br>

<details>
<summary>๐ํจ์๋ฅผ Update์ ๋ด์๋ฒ๋ฆฌ๋ฉด?</summary>
<div markdown="1">

![ezgif com-gif-maker](https://user-images.githubusercontent.com/97969957/190846838-cec72dfa-0b45-4389-bf9a-55deb3b629aa.gif)

</div>
</details>

<br>

## ๐ป์ ์ฉ ์ฝ๋
```C#

public class gameManager : MonoBehaviour
{
    public GameObject rain;
    
    // Start is called before the first frame update
    void Start()
    {
        InvokeRepeating("makeRain", 0, 0.5f);
    }

    void makeRain()
    {
        Instantiate(rain);
    }
```
