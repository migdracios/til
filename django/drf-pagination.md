## 🕵️‍♀️DRF 공식문서로 Pagination을 구현하자
마크다운 토글코드
```shell
<details>
<summary>TITLE</summary>
<div markdown="1">

CONTENT

</div>
<details>
```

<details>
<summary>🔥구현 목표</summary>
<div markdown="1">

- DRF 공식문서를 참조하여 View를 구현한다
- 공식문서를 참조하여 Request와 Response를 동일하게 구현한다
- Generic View를 참조하여 구현하고, 그 사용법을 숙지한다

</div>
<details>

<details>
<summary>👁‍🗨 레퍼런스</summary>
<div markdown="1">

### [📜DRF 공식문서 - Viewset](https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/)

### [📜DRF 공식문서Pagination](https://www.django-rest-framework.org/api-guide/pagination/)

</div>
<details>

<details>
<summary>🖋 학습포인트</summary>
<div markdown="1">

## 🖋APIView와, Generic View, Viewset은 어떤 차이점이 있는가?

- DRF에서 구현할 수 있는 View 구현 방법은 APIView, Generic View, Viewset 세 가지로 구분된다.
- APIView는 RestAPI 방식으로 HTTP Method를 함수로 가지고 있는 CBV 형식의 View 구현 방법이다. URL에 View만 as_view() 형식으로 연결해두면 HTTP Request Method에 따라서 해당 Method의 이름에 맞는 함수를 호출한다
- Generic View는 이미 구현되어 있는 View를 상속받아 기능을 그대로 구현하는 방법이다. 검색, 필터 등 특정 API를 상속받아 정해진 형식의 필드를 작성하는 것만으로 빠르게 View를 구현 가능하다.
- Viewset은 APIView와 Generic View를 합친 형태이며, 리스트 보기를 포함한 REST API를 모두 독특하게 가지고 있는 메서드와 연결하여 모두 구현이 가능한 CBV이며, 또한 미리 구현되어 있는 API를 상속하는 것으로 빠르게 View를 구현할 수도 있다. Viewset은 URL에서 변수로 뷰를 as_view() 안에서 list, retrieve, create, update, destroy 등의 메서드와 매핑하여 선언한 뒤, UrlPatterns 안에서 변수를 호출하는 것으로 구현이 가능하다.

## 🖋Pagination의 구현순서를 리마인드

- [setting.py](http://setting.py) 에 REST_FRAMEWORK  안에 공식문서 example을 활용하여 코드 기재
- 페이지네이션을 적용할 앱에 [views.py](http://views.py) 로 이동하여 ViewSet을 상속받은 클래스를 작성한 후, 모델과 시리얼라이저, 페이지 넘버를 기재한다
- [urls.py](http://urls.py) 에 pagination으로 이동할 경로를 지정해줌으로 페이지네이션을 구현할 수 있다

## 🖋공식문서 어떻게 읽었나?

- PageNumberPagination을 참조했음!

### 페이지네이션 API Request&Response

💡아! 페이지네이션은 이렇게 요청하고, 데이터를 반환하는구나!

```python
# Request
GET https://api.example.org/accounts/?page=4

# Response
HTTP 200 OK
{
    "count": 1023,
    "next": "https://api.example.org/accounts/?page=5",
    "previous": "https://api.example.org/accounts/?page=3",
    "results": [
       …
    ]
}
```

### 페이지네이션을 구현하기 위해 셋업

💡[settings.py](http://settings.py) 에서 REST_FRAMEWORK라는 변수 안에 페이지네이션을 따로 넣어주는구나!

```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100
}
```

### 기본적인 페이지네이션 코드 스타일

💡아 페이지네이션은 이걸 가져다가 쓰면 되겠구나!

- 쿼리셋은 원하는 데이터 형식이구나! 나는 아카이브모델을 가져와서 쓰면 되겠다!
- 시리얼라이저 클래스는 시리얼라이저 가져다 붙이면 되구나!
- 페이지네이션 클래스는 이미 만들어진 페이지네이션을 가져다 붙이면 되구나! 공식문서 보고 훔쳐야지

```python
class BillingRecordsView(generics.ListAPIView):
    queryset = Billing.objects.all()
    serializer_class = BillingRecordsSerializer
    pagination_class = LargeResultsSetPagination
```

### 필요한 라이브러리 임포트

```python
# views.py의 페이지네이션 클래스에 붙일 라이브러리
from rest_framework.pagination import PageNumberPagination

# views.py의 제너릭 뷰를 상속받기 위한 라이브러리
from rest_framework import generics
```

</div>
<details>

<details>
<summary>💾구현코드 - Viewset</summary>
<div markdown="1">

```python
#setting.py

REST_FRAMEWORK = {
	'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
	'PAGE_SIZE': 15,
}
```

```python
#Archive view 작성
from rest_framework import viewsets

class ArchaivePaginationViewSet(viewsets.ModelViewSet):
    queryset = ArchiveModel.objects.all()
    serializer_class = ArchiveSerializer
    pagination_class = PageNumberPagination
```

```python
#urls.py

from .views import ArchaivePaginationViewSet
pagination = ArchaivePaginationViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = [
	path('pagination/', pagination, name='archive_pagination'),
]
```

</div>
<details>

<details>
<summary>💾구현코드 - Generic View</summary>
<div markdown="1">

```python
#setting.py

REST_FRAMEWORK = {
	'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
	'PAGE_SIZE': 15,
}
```

```python
#urls.py

urlpatterns = [
	path('pagination/', views.ArchaivePagination.as_view(), name='archive_pagination'),
]
```

```python
# Archive view 작성

class ArchaivePagination(generics.ListAPIView):
    queryset = ArchiveModel.objects.all()
    serializer_class = ArchiveSerializer
    pagination_class = PageNumberPagination
```

</div>
<details>
