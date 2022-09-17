# Unity TIL
게임개발엔진 Unity의 개발일지 저장소입니다. C# 관련 코드가 포함됩니다.

# 목차
- [🚩Prefab과 Instantiate]()


# Prefab과 Instantiate
- Unity의 프리팹 시스템을 이용하면 게임 오브젝트를 생성, 설정 및 저장할 수 있으며, 해당 게임 오브젝트의 모든 컴포넌트, 프로퍼티 값, 자식 게임 오브젝트를 재사용 가능한 에셋으로 만들 수 있습니다. 
- 미니 프로젝트에서 함수를 활용하여 프리팹을 적용하는 방법을 예시로 추가합니다.

## 💾미니프로젝트. 빗물받기게임
    - 빗물을 받아내면 점수를 획득하는 게임 시스템에서 빗방울 스프라이트를 생성했다
    - 빗방울 스프라이트를 한 개가 아닌, 여러 개로 카피하기 위해서는 프리팹과 인스턴시에이트가 필요하다
    
### ✍Prefab 만들기
1. 작성한 스프라이트를 에셋 폴더에서 새로운 디렉토리 prefab을 만든다
2. prefab 폴더에 스프라이트를 드래그앤 드롭

### ✍Instantiate 하기
1. gameManager 오브젝트에 삽입된 gameManager.cs 스크립트를 열어 코드를 작성한다
2. makeRain 함수를 만들어 Instantiate 함수를 담을 함수를 생성
3. Instantiate 함수로 빗방울 스프라이트를 생성한다
 

### ✍InvokeRepeat 함수로 반복 호출하기
1. InvokeRepeat("호출할 함수 이름", 0, 간격 시간); 을 사용하여 Instantiate 함수를 반복 호출한다

## 🔥트러블 슈팅. 함수 호출 위치 확인하기!
    - 헷갈리지 말아야 할 점은 Instantiate 할 함수를 만들고, InvokeRepeat 함수에서 해당 함수를 호출해야 함
    - update 함수에 Instantiate 함수를 호출한다면, 프레임 별로 객체 생성을 반복 실행하므로 와르르 빗방울이 쏟아짐

<details>
<summary>함수를 Update에 담아버리면?</summary>
<div markdown="1">



</div>
</details>


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