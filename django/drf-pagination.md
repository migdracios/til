## ๐ต๏ธโโ๏ธDRF ๊ณต์๋ฌธ์๋ก Pagination์ ๊ตฌํํ์
๋งํฌ๋ค์ด ํ ๊ธ์ฝ๋
```shell
<details>
<summary>TITLE</summary>
<div markdown="1">

CONTENT

</div>
<details>
```

<details>
<summary>๐ฅ๊ตฌํ ๋ชฉํ</summary>
<div markdown="1">

- DRF ๊ณต์๋ฌธ์๋ฅผ ์ฐธ์กฐํ์ฌ View๋ฅผ ๊ตฌํํ๋ค
- ๊ณต์๋ฌธ์๋ฅผ ์ฐธ์กฐํ์ฌ Request์ Response๋ฅผ ๋์ผํ๊ฒ ๊ตฌํํ๋ค
- Generic View๋ฅผ ์ฐธ์กฐํ์ฌ ๊ตฌํํ๊ณ , ๊ทธ ์ฌ์ฉ๋ฒ์ ์์งํ๋ค

</div>
</details>

<details>
<summary>๐โ๐จ ๋ ํผ๋ฐ์ค</summary>
<div markdown="1">

### [๐DRF ๊ณต์๋ฌธ์ - Viewset](https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/)

### [๐DRF ๊ณต์๋ฌธ์Pagination](https://www.django-rest-framework.org/api-guide/pagination/)

</div>
</details>

<details>
<summary>๐ ํ์ตํฌ์ธํธ</summary>
<div markdown="1">

## ๐APIView์, Generic View, Viewset์ ์ด๋ค ์ฐจ์ด์ ์ด ์๋๊ฐ?

- DRF์์ ๊ตฌํํ  ์ ์๋ View ๊ตฌํ ๋ฐฉ๋ฒ์ APIView, Generic View, Viewset ์ธ ๊ฐ์ง๋ก ๊ตฌ๋ถ๋๋ค.
- APIView๋ RestAPI ๋ฐฉ์์ผ๋ก HTTP Method๋ฅผ ํจ์๋ก ๊ฐ์ง๊ณ  ์๋ CBV ํ์์ View ๊ตฌํ ๋ฐฉ๋ฒ์ด๋ค. URL์ View๋ง as_view() ํ์์ผ๋ก ์ฐ๊ฒฐํด๋๋ฉด HTTP Request Method์ ๋ฐ๋ผ์ ํด๋น Method์ ์ด๋ฆ์ ๋ง๋ ํจ์๋ฅผ ํธ์ถํ๋ค
- Generic View๋ ์ด๋ฏธ ๊ตฌํ๋์ด ์๋ View๋ฅผ ์์๋ฐ์ ๊ธฐ๋ฅ์ ๊ทธ๋๋ก ๊ตฌํํ๋ ๋ฐฉ๋ฒ์ด๋ค. ๊ฒ์, ํํฐ ๋ฑ ํน์  API๋ฅผ ์์๋ฐ์ ์ ํด์ง ํ์์ ํ๋๋ฅผ ์์ฑํ๋ ๊ฒ๋ง์ผ๋ก ๋น ๋ฅด๊ฒ View๋ฅผ ๊ตฌํ ๊ฐ๋ฅํ๋ค.
- Viewset์ APIView์ Generic View๋ฅผ ํฉ์น ํํ์ด๋ฉฐ, ๋ฆฌ์คํธ ๋ณด๊ธฐ๋ฅผ ํฌํจํ REST API๋ฅผ ๋ชจ๋ ๋ํนํ๊ฒ ๊ฐ์ง๊ณ  ์๋ ๋ฉ์๋์ ์ฐ๊ฒฐํ์ฌ ๋ชจ๋ ๊ตฌํ์ด ๊ฐ๋ฅํ CBV์ด๋ฉฐ, ๋ํ ๋ฏธ๋ฆฌ ๊ตฌํ๋์ด ์๋ API๋ฅผ ์์ํ๋ ๊ฒ์ผ๋ก ๋น ๋ฅด๊ฒ View๋ฅผ ๊ตฌํํ  ์๋ ์๋ค. Viewset์ URL์์ ๋ณ์๋ก ๋ทฐ๋ฅผ as_view() ์์์ list, retrieve, create, update, destroy ๋ฑ์ ๋ฉ์๋์ ๋งคํํ์ฌ ์ ์ธํ ๋ค, UrlPatterns ์์์ ๋ณ์๋ฅผ ํธ์ถํ๋ ๊ฒ์ผ๋ก ๊ตฌํ์ด ๊ฐ๋ฅํ๋ค.

## ๐Pagination์ ๊ตฌํ์์๋ฅผ ๋ฆฌ๋ง์ธ๋

- [setting.py](http://setting.py) ์ REST_FRAMEWORK  ์์ ๊ณต์๋ฌธ์ example์ ํ์ฉํ์ฌ ์ฝ๋ ๊ธฐ์ฌ
- ํ์ด์ง๋ค์ด์์ ์ ์ฉํ  ์ฑ์ [views.py](http://views.py) ๋ก ์ด๋ํ์ฌ ViewSet์ ์์๋ฐ์ ํด๋์ค๋ฅผ ์์ฑํ ํ, ๋ชจ๋ธ๊ณผ ์๋ฆฌ์ผ๋ผ์ด์ , ํ์ด์ง ๋๋ฒ๋ฅผ ๊ธฐ์ฌํ๋ค
- [urls.py](http://urls.py) ์ pagination์ผ๋ก ์ด๋ํ  ๊ฒฝ๋ก๋ฅผ ์ง์ ํด์ค์ผ๋ก ํ์ด์ง๋ค์ด์์ ๊ตฌํํ  ์ ์๋ค

## ๐๊ณต์๋ฌธ์ ์ด๋ป๊ฒ ์ฝ์๋?

- PageNumberPagination์ ์ฐธ์กฐํ์!

### ํ์ด์ง๋ค์ด์ API Request&Response

๐ก์! ํ์ด์ง๋ค์ด์์ ์ด๋ ๊ฒ ์์ฒญํ๊ณ , ๋ฐ์ดํฐ๋ฅผ ๋ฐํํ๋๊ตฌ๋!

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
       โฆ
    ]
}
```

### ํ์ด์ง๋ค์ด์์ ๊ตฌํํ๊ธฐ ์ํด ์์

๐ก[settings.py](http://settings.py) ์์ REST_FRAMEWORK๋ผ๋ ๋ณ์ ์์ ํ์ด์ง๋ค์ด์์ ๋ฐ๋ก ๋ฃ์ด์ฃผ๋๊ตฌ๋!

```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100
}
```

### ๊ธฐ๋ณธ์ ์ธ ํ์ด์ง๋ค์ด์ ์ฝ๋ ์คํ์ผ

๐ก์ ํ์ด์ง๋ค์ด์์ ์ด๊ฑธ ๊ฐ์ ธ๋ค๊ฐ ์ฐ๋ฉด ๋๊ฒ ๊ตฌ๋!

- ์ฟผ๋ฆฌ์์ ์ํ๋ ๋ฐ์ดํฐ ํ์์ด๊ตฌ๋! ๋๋ ์์นด์ด๋ธ๋ชจ๋ธ์ ๊ฐ์ ธ์์ ์ฐ๋ฉด ๋๊ฒ ๋ค!
- ์๋ฆฌ์ผ๋ผ์ด์  ํด๋์ค๋ ์๋ฆฌ์ผ๋ผ์ด์  ๊ฐ์ ธ๋ค ๋ถ์ด๋ฉด ๋๊ตฌ๋!
- ํ์ด์ง๋ค์ด์ ํด๋์ค๋ ์ด๋ฏธ ๋ง๋ค์ด์ง ํ์ด์ง๋ค์ด์์ ๊ฐ์ ธ๋ค ๋ถ์ด๋ฉด ๋๊ตฌ๋! ๊ณต์๋ฌธ์ ๋ณด๊ณ  ํ์ณ์ผ์ง

```python
class BillingRecordsView(generics.ListAPIView):
    queryset = Billing.objects.all()
    serializer_class = BillingRecordsSerializer
    pagination_class = LargeResultsSetPagination
```

### ํ์ํ ๋ผ์ด๋ธ๋ฌ๋ฆฌ ์ํฌํธ

```python
# views.py์ ํ์ด์ง๋ค์ด์ ํด๋์ค์ ๋ถ์ผ ๋ผ์ด๋ธ๋ฌ๋ฆฌ
from rest_framework.pagination import PageNumberPagination

# views.py์ ์ ๋๋ฆญ ๋ทฐ๋ฅผ ์์๋ฐ๊ธฐ ์ํ ๋ผ์ด๋ธ๋ฌ๋ฆฌ
from rest_framework import generics
```

</div>
</details>

<details>
<summary>๐พ๊ตฌํ์ฝ๋ - Viewset</summary>
<div markdown="1">

```python
#setting.py

REST_FRAMEWORK = {
	'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
	'PAGE_SIZE': 15,
}
```

```python
#Archive view ์์ฑ
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
</details>

<details>
<summary>๐พ๊ตฌํ์ฝ๋ - Generic View</summary>
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
# Archive view ์์ฑ

class ArchaivePagination(generics.ListAPIView):
    queryset = ArchiveModel.objects.all()
    serializer_class = ArchiveSerializer
    pagination_class = PageNumberPagination
```

</div>
</details>
