# Django





## 👨‍🎓 학습목표

- 게시판만들기 (CRUD구현)

- 이미지 활용
- 로그인/로그아웃 
- 회원가입/회원수정/회원탈퇴
- 비밀번호 변경







### 1. VENV 및 환경준비

```
- venv 설치
python -m venv venv

- venv 실행
source venv/Scripts/activate

- README.md와 gitignore설치
touch README.md .gitignore

- 첫 git 업로드

- gitignore gitignore.io에서 필요내용 채우기

- requirements.txt 파일이 있다면 내용 설치
pip install -r requirements.txt

- Django 설치가 없다면 설치
pip install django

- Project 설치
django-admin startproject 프로젝트명 .

- App 설치
python manage.py startapp 앱이름

- 관리자 페이지
python manage.py createsuperuser


```







### 2. CRUD만들기



#### 1) MTV구축

##### (1) Models 단

###### ① models.py

```
- models.py 
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


- Migrations
djanogo가 model에 생긴 변화를 반영
python manage.py makemigrations

- migrate
DB에 마이그레이션을 반영
python manage.py migrate

- sqlmigrate
마이그레이션에 대한 SQL 구문을 확인
python manage.py sqlmigrate 앱이름 번호

-showmigrations
프로젝트의 마이그레이션 상태를 확인
python manage.py showmigrations

```

model field의 공식내용

https://docs.djangoproject.com/en/3.2/ref/models/fields/#textfield



###### ② ORM 사용시

```
shell_plus사용법과 DB API구문 ORM

이용전
pip install ipython
pip install django-extensions 설치후
반드시 INSTALLED_APPS = [
		'django_extensions',
] 앱 등록

사용시
python manage.py shell_plus

- READ
# 전체 article 객체 조회방법
클래스명.objects.all()

- CREATE
# 특정 테이블에 새로운 행을 추가
인스턴스 = 클래스() ex) article = Article()

# 인스턴스 변수에 value할당
인스턴스.title 
ex) Article.title = 'first'
    Article.content = 'django'
    
    
# 반드시 저장해야지 반영
article.save()

# 값 확인 1
클래스명.objects.all()

# 값 확인 2
인스턴스.value

# 값 확인 3
클래스명.objects.create(key='value', key='value')


- UPDATE
# 값을 확인
인스턴스 = 클래스명.objects.get(pk=1)

# 값을 변경하고 저장
인스턴스.key = 'value'
인스턴스.save()

# 변경확인
인스턴스.key

- DELETE
# 삭제


```

QuerySet API reference

https://docs.djangoproject.com/en/3.2/ref/models/querysets/



###### ③ admin 등록

```python
# admin.py

from django.contrib import admin
# models의 클래스를 불러오기
from .models import Article

# admin site에 models클래스를 등록시킨다.
# Register your models here.
admin.site.register(Article)
```

1. models의 클래스를 불러오기

2. admin site에 models클래스를 등록시킨다.

https://docs.djangoproject.com/en/3.2/ref/contrib/admin/





##### (2) Views 단계

###### ⓞ 앱등록

```python
# settings에 공용템플릿 등록

경로

BASE_DIR / '폴더명' / 'templates'

BASE_DIR / 'templates'

```



**urls역할**

```python
# urls.py에서 쓸 수 있는 클래스
from django.contrib import admin
from django.urls import path
from 프로젝트명 import views
(HTTP 요철을 알맞은 view로 전달)
```



**views역할**

```python
# views.py
from django.shortcuts import render


# HTTP 요청을 수신하고 HTTP 응답을 반환하는 함수작성

def index(request):
    return render(request, 'index.html')

# Model을 통해 요청에 맞는 필요 데이터에 접근
# Teplate에게 HTTP 응답 서식을 맡김
```



**Templates**

```python
# 실제 내용을 보여주는 파일
# Template 파일 경로의 기본 값은 app폴더 안의 templates 폴더로 지정되어 있다. 
```





###### ① R



index

```python
# urls.py
```



```python
# views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm

from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required


# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.order_by('-pk')
    
    context = {
        'articles': articles,
    }
    
    return render(request, 'articles/index.html', context)
```



```django
# 개별 템플릿

{% extends 'base.html' %}

{% block content %}
  <h1>Articles</h1>
  {% if request.user.is_authenticated %}
    <a href="{% url 'articles:create' %}">[CREATE]</a>
  {% else %}
    <a href="{% url 'accounts:login' %}">[새 글을 작성하려면 로그인하세요.]</a>
  {% endif %}
  <hr>
  {% for article in articles %}
    <p>글 번호 : {{ article.pk }}</p>
    <p>글 제목 : {{ article.title }}</p>
    <p>글 내용 : {{ article.content }}</p>
    <a href="{% url 'articles:detail' article.pk %}">[DETAIL]</a>
    <hr>
  {% endfor %}
{% endblock content %}

```



detail

```python
# urls.py
```



```python
# views.py

@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

```



```django
# 개별 템플릿

{% extends 'base.html' %}

{% block content %}
  <h2>DETAIL</h2>
  <h3>{{ article.pk }} 번째 글</h3>
  <hr>
  <p>제목 : {{ article.title }}</p>
  <p>내용 : {{ article.content }}</p>
  <p>작성시각 : {{ article.created_at }}</p>
  <p>수정시각 : {{ article.updated_at }}</p>
  <hr>
  <a href="{% url 'articles:update' article.pk %}">[UPDATE]</a>
  <form action="{% url 'articles:delete' article.pk %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="DELETE">
  </form>
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock content %}

```





###### ② C



create

```python
# urls.py
```



```python
# views.py

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
```



```django
# 개별 템플릿

{% extends 'base.html' %}

{% block content %}
  <h1>CREATE</h1>
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="작성">
  </form>
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock content %}

```



###### ③ U



update

```python
# urls.py
```



```python
# views.py

@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)
```



```django
# 개별 템플릿

{% extends 'base.html' %}

{% block content %}
  <h1>UPDATE</h1>
  <form action="{% url 'articles:update' article.pk %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="수정">
  </form>
  <hr>
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock content %}

```





###### ④ D



delete

```python
# urls.py
```



```python
# views.py

@login_required
@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        article.delete()
    return redirect('articles:index')
```





종합

```python
# views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm

from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required


# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.order_by('-pk')
    
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


@login_required
@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        article.delete()
    return redirect('articles:index')


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)

```



##### (3) Templates 단계







### 3. Form과 ModelForm이 CRUD에 미치는 영향

#### 1) Form 기능이 필요한 이유

form에 들어가는 key와 value값이 수억 수조개라면 하나하나 입력하기란 어려울 것이다. 이것을 form기능을 통해 단순화하고 자동화 할 수 있다.

```python
# forms.py를 새로 만든다.
# 장고내에서 forms의 기능을 불러온다
from django import forms

class ArticleForm(forms.Form):
	title = forms.CharField(max_length=10)
    content = forms.CharField()
    

```

```python
# views.py
from .forms import ArticleForm

```

```django
- label & input 쌍에 대한 3가지 출력옵션
{{ form.as_p }}

- input 요소 표현 방법 2가지
1. Form fields - 유효성 검사 처리
2. Widgets - input 속성의 단순한 렌더링 처리
```

Form rendering options

https://docs.djangoproject.com/en/3.2/topics/forms/#form-rendering-options

django form rendering options

https://docs.djangoproject.com/en/3.2/ref/forms/widgets/



#### 2) ModelForm기능이 필요한 이유

models.py에서 필드를 정의했는데 forms.py에서 또 필드를 정의 한다고??? DRY에 위반!!!

```python
# forms.py

from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'

```

modelfielf와 formfield 비교

https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/

selecting-the-fields-to-use(왜 교재방식과 공식문서가 다르지?)

https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/#selecting-the-fields-to-use



```python
# views.py


```





#### 3) HTTP requests 처리

```python
# views.py


```

django shortcuts - render(), redirect(), get_object_or_404()

https://docs.djangoproject.com/en/3.2/topics/http/shortcuts/



### 4. 이미지넣기

#### 1) Static files

① INSTALLED_APPS 확인

② STATIC_URL 정의

③ 템플릿 테그입력과 STATIC_ROOT에 연결

④ 앱에 저장

```python
# settings.py

STATIC_URL = '/static/'

# STATIC_ROOT = BASE_DIR / 'staticfiles'
# 명령어 python manage.py collectstatic


STATICFILES_DIRS = [
    BASE_DIR / 'static',
]


```



```django
{# base.html에 적용 #}
```



```django
{# 개별.html에 적용 #}
```





#### 2) Media files

##### (1) Media 준비

```python
# 프로젝트 urls.py에 추가

from django.conf import settings
from django.conf.urls.static import static


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```



```python
# settings.py에 추가

STATIC_URL = '/static/'
# STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

MEDIA_ROOT = BASE_DIR / 'media'

MEDIA_URL = '/media/'

```



```python
# models.py에 추가

def aritlces_image_path(instance, filename):
    return f'user_{instance.user.pk}/{filename}'


class Article(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)

```

models.py가 바뀌어서 migrations해주기





models.py

```python
from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill


def articles_image_path(instance, filename):
    return f'user_{instance.pk}/{filename}'


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # 이미지필드 사용법!!
    # image = models.ImageField(upload_to='images/', blank=True)
    # image = models.ImageField(upload_to='%Y/%m/%d/', blank=True)
    # image = models.ImageField(upload_to=articles_image_path, blank=True)
    
    
    # image = ProcessedImageField(
    #     upload_to='thumbnails/',
    #     processors=[ResizeToFill(100, 50)],
    #     format='JPEG',
    #     options={'quality': 60}
    # )
    image = models.ImageField(upload_to='origins/', blank=True)
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(100, 50)],
        format='JPEG',
        options={'quality': 90},
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

```





##### (2) Media create

```python
# view.py

{% extends 'base.html' %}

{% block content %}
  <h1>CREATE</h1>
  <form action="{% url 'articles:create' %}" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="작성">
  </form>
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock content %}

```



```django
{# enctype #}

{% extends 'base.html' %}

{% block content %}
  <h1>CREATE</h1>
  <form action="{% url 'articles:create' %}" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="작성">
  </form>
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock content %}

```







##### (3) Media read



base.html

```django
{# base.html #}

{% load static %}

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">
  <title>중고나라 {% block title %}{% endblock title %} </title>
</head>
<body>
  {% include 'navbar.html' %}
  <img src="{% static 'images/sample-img-2.jpg' %}" alt="sample image second">
  <div class="container">    
    {% block content %}
    {% endblock content %}
  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj" crossorigin="anonymous"></script>
</body>
</html>

```





index

```python
# views.py

@require_safe
def index(request):
    articles = Article.objects.order_by('-pk')
    
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)
```



```django
{% extends 'base.html' %}

{% block content %}
  <h1>Articles</h1>
  <a href="{% url 'articles:create' %}">[CREATE]</a>
  <hr>
  {% for article in articles %}
    <p>글 번호 : {{ article.pk }}</p>
    <p>글 제목 : {{ article.title }}</p>
    <p>글 내용 : {{ article.content }}</p>
    <a href="{% url 'articles:detail' article.pk %}">[DETAIL]</a>
    <hr>
  {% endfor %}
{% endblock content %}

```





detail

```python
# views.py

@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)
```

```django
{# if문으로 나눠준다 #}

{% extends 'base.html' %}
{% load static %}

{% block content %}
  <img src="{% static 'articles/sample-img-1.png' %}" alt="sample image">

  <h2>DETAIL</h2>
  <h3>{{ article.pk }} 번째 글</h3>
  {% if article.image %}
    <img src="{{ article.image_thumbnail.url }}" alt="{{ article.image_thumbnail }}">
  {% else %}
    <img src="{% static 'images/default.jpg' %}" alt="default image">
  {% endif %}
  
  <hr>
  <p>제목 : {{ article.title }}</p>
  <p>내용 : {{ article.content }}</p>
  <p>작성시각 : {{ article.created_at }}</p>
  <p>수정시각 : {{ article.updated_at }}</p>
  <hr>
  <a href="{% url 'articles:update' article.pk %}">[UPDATE]</a>
  <form action="{% url 'articles:delete' article.pk %}" method="POST">
    {% csrf_token %}
    <button>DELETE</button>
  </form>
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock content %}

```





##### (4) Media update

```python
# views.py

# request.FILES

@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)


```

```django
{# enctype #}

{% extends 'base.html' %}

{% block content %}
  <h1>UPDATE</h1>
  <form action="{% url 'articles:update' article.pk %}" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button>수정</button>
  </form>
  <hr>
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock content %}

```







#### 3) Image Upload

설치사항

```
$ python manage.py makemigrations
$ pip install Pillow

$ python manage.py makemigrations
$ python manage.py migrate

$ pip freeze > requirements.txt
```



#### 4) Image Resizing

이미지킷 설치

```
$ pip install django-imagekit

$ pip freeze > requirements.txt
```



```python
# settings.py

INSTALLED_APPS = [
    'imagekit',
]
```

```python
# models.py

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

 image = models.ImageField(upload_to='origins/')
    image_thumbnail = ImageSpecField(source='image',
                                      processors=[ResizeToFill(100, 100)],
                                      format='JPEG',
                                      options={'quality': 80})

```

models의 변화로 migrations



```python
# 개별.html


```



### 5. 로그인/로그아웃 

```django
{# base.html #}

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">
  <title>Document</title>
</head>
<body>
  <div class="container">
    {% if request.user.is_authenticated %}
      <h3>Hello, {{ user }}</h3>
      <a href="{% url 'accounts:update' %}">회원정보수정</a>
      <form action="{% url 'accounts:logout' %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="Logout">
      </form>
      <form action="{% url 'accounts:delete' %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="회원탈퇴">
      </form>
    {% else %}
      <a href="{% url 'accounts:login' %}">Login</a>
      <a href="{% url 'accounts:signup' %}">Signup</a>
    {% endif %}

    {% block content %}
    {% endblock content %}
  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj" crossorigin="anonymous"></script>
</body>
</html>

```







```python
# urls.py

from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('password/', views.change_password, name='change_password'),
]

```

```python
# views.py

from django.shortcuts import redirect, render
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import (
    AuthenticationForm, 
    UserCreationForm, 
    PasswordChangeForm
)
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm

# Create your views here.
@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 로그인 !
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('articles:index')
```



```django
{# login.html #}

{% extends 'base.html' %}

{% block content %}
  <h1>Login</h1>
  <form action="" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
{% endblock content %}
```





### 6. 회원가입/회원수정/비밀번호수정



```python
# forms.py

from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)
```



```python
# views.py


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect('articles:index') 


@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)

```



```django
{# 회원가입 #}

{% extends 'base.html' %}

{% block content %}
  <h1>Signup</h1>
  <form action="{% url 'accounts:signup' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
{% endblock content %}
```





```django
{# 회원정보수정 #}

{% extends 'base.html' %}

{% block content %}
  <h1>회원정보수정</h1>
  <form action="{% url 'accounts:update' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
{% endblock content %}
```







```django
{# 비밀번호변경 #}

{% extends 'base.html' %}

{% block content %}
  <h1>비밀번호 변경</h1>
  <form action="{% url 'accounts:change_password' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
{% endblock content %}
```

