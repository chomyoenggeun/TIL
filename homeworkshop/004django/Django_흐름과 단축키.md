# Django





## ๐จโ๐ ํ์ต๋ชฉํ

- ๊ฒ์ํ๋ง๋ค๊ธฐ (CRUD๊ตฌํ)

- ์ด๋ฏธ์ง ํ์ฉ
- ๋ก๊ทธ์ธ/๋ก๊ทธ์์ 
- ํ์๊ฐ์/ํ์์์ /ํ์ํํด
- ๋น๋ฐ๋ฒํธ ๋ณ๊ฒฝ







### 1. VENV ๋ฐ ํ๊ฒฝ์ค๋น

```
- venv ์ค์น
python -m venv venv

- venv ์คํ
source venv/Scripts/activate

- README.md์ gitignore์ค์น
touch README.md .gitignore

- ์ฒซ git ์๋ก๋

- gitignore gitignore.io์์ ํ์๋ด์ฉ ์ฑ์ฐ๊ธฐ

- requirements.txt ํ์ผ์ด ์๋ค๋ฉด ๋ด์ฉ ์ค์น
pip install -r requirements.txt

- Django ์ค์น๊ฐ ์๋ค๋ฉด ์ค์น
pip install django

- Project ์ค์น
django-admin startproject ํ๋ก์ ํธ๋ช .

- App ์ค์น
python manage.py startapp ์ฑ์ด๋ฆ

- ๊ด๋ฆฌ์ ํ์ด์ง
python manage.py createsuperuser


```







### 2. CRUD๋ง๋ค๊ธฐ



#### 1) MTV๊ตฌ์ถ

##### (1) Models ๋จ

###### โ  models.py

```
- models.py 
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


- Migrations
djanogo๊ฐ model์ ์๊ธด ๋ณํ๋ฅผ ๋ฐ์
python manage.py makemigrations

- migrate
DB์ ๋ง์ด๊ทธ๋ ์ด์์ ๋ฐ์
python manage.py migrate

- sqlmigrate
๋ง์ด๊ทธ๋ ์ด์์ ๋ํ SQL ๊ตฌ๋ฌธ์ ํ์ธ
python manage.py sqlmigrate ์ฑ์ด๋ฆ ๋ฒํธ

-showmigrations
ํ๋ก์ ํธ์ ๋ง์ด๊ทธ๋ ์ด์ ์ํ๋ฅผ ํ์ธ
python manage.py showmigrations

```

model field์ ๊ณต์๋ด์ฉ

https://docs.djangoproject.com/en/3.2/ref/models/fields/#textfield



###### โก ORM ์ฌ์ฉ์

```
shell_plus์ฌ์ฉ๋ฒ๊ณผ DB API๊ตฌ๋ฌธ ORM

์ด์ฉ์ 
pip install ipython
pip install django-extensions ์ค์นํ
๋ฐ๋์ INSTALLED_APPS = [
		'django_extensions',
] ์ฑ ๋ฑ๋ก

์ฌ์ฉ์
python manage.py shell_plus

- READ
# ์ ์ฒด article ๊ฐ์ฒด ์กฐํ๋ฐฉ๋ฒ
ํด๋์ค๋ช.objects.all()

- CREATE
# ํน์  ํ์ด๋ธ์ ์๋ก์ด ํ์ ์ถ๊ฐ
์ธ์คํด์ค = ํด๋์ค() ex) article = Article()

# ์ธ์คํด์ค ๋ณ์์ valueํ ๋น
์ธ์คํด์ค.title 
ex) Article.title = 'first'
    Article.content = 'django'
    
    
# ๋ฐ๋์ ์ ์ฅํด์ผ์ง ๋ฐ์
article.save()

# ๊ฐ ํ์ธ 1
ํด๋์ค๋ช.objects.all()

# ๊ฐ ํ์ธ 2
์ธ์คํด์ค.value

# ๊ฐ ํ์ธ 3
ํด๋์ค๋ช.objects.create(key='value', key='value')


- UPDATE
# ๊ฐ์ ํ์ธ
์ธ์คํด์ค = ํด๋์ค๋ช.objects.get(pk=1)

# ๊ฐ์ ๋ณ๊ฒฝํ๊ณ  ์ ์ฅ
์ธ์คํด์ค.key = 'value'
์ธ์คํด์ค.save()

# ๋ณ๊ฒฝํ์ธ
์ธ์คํด์ค.key

- DELETE
# ์ญ์ 


```

QuerySet API reference

https://docs.djangoproject.com/en/3.2/ref/models/querysets/



###### โข admin ๋ฑ๋ก

```python
# admin.py

from django.contrib import admin
# models์ ํด๋์ค๋ฅผ ๋ถ๋ฌ์ค๊ธฐ
from .models import Article

# admin site์ modelsํด๋์ค๋ฅผ ๋ฑ๋ก์ํจ๋ค.
# Register your models here.
admin.site.register(Article)
```

1. models์ ํด๋์ค๋ฅผ ๋ถ๋ฌ์ค๊ธฐ

2. admin site์ modelsํด๋์ค๋ฅผ ๋ฑ๋ก์ํจ๋ค.

https://docs.djangoproject.com/en/3.2/ref/contrib/admin/





##### (2) Views ๋จ๊ณ

###### โ ์ฑ๋ฑ๋ก

```python
# settings์ ๊ณต์ฉํํ๋ฆฟ ๋ฑ๋ก

๊ฒฝ๋ก

BASE_DIR / 'ํด๋๋ช' / 'templates'

BASE_DIR / 'templates'

```



**urls์ญํ **

```python
# urls.py์์ ์ธ ์ ์๋ ํด๋์ค
from django.contrib import admin
from django.urls import path
from ํ๋ก์ ํธ๋ช import views
(HTTP ์์ฒ ์ ์๋ง์ view๋ก ์ ๋ฌ)
```



**views์ญํ **

```python
# views.py
from django.shortcuts import render


# HTTP ์์ฒญ์ ์์ ํ๊ณ  HTTP ์๋ต์ ๋ฐํํ๋ ํจ์์์ฑ

def index(request):
    return render(request, 'index.html')

# Model์ ํตํด ์์ฒญ์ ๋ง๋ ํ์ ๋ฐ์ดํฐ์ ์ ๊ทผ
# Teplate์๊ฒ HTTP ์๋ต ์์์ ๋งก๊น
```



**Templates**

```python
# ์ค์  ๋ด์ฉ์ ๋ณด์ฌ์ฃผ๋ ํ์ผ
# Template ํ์ผ ๊ฒฝ๋ก์ ๊ธฐ๋ณธ ๊ฐ์ appํด๋ ์์ templates ํด๋๋ก ์ง์ ๋์ด ์๋ค. 
```





###### โ  R



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
# ๊ฐ๋ณ ํํ๋ฆฟ

{% extends 'base.html' %}

{% block content %}
  <h1>Articles</h1>
  {% if request.user.is_authenticated %}
    <a href="{% url 'articles:create' %}">[CREATE]</a>
  {% else %}
    <a href="{% url 'accounts:login' %}">[์ ๊ธ์ ์์ฑํ๋ ค๋ฉด ๋ก๊ทธ์ธํ์ธ์.]</a>
  {% endif %}
  <hr>
  {% for article in articles %}
    <p>๊ธ ๋ฒํธ : {{ article.pk }}</p>
    <p>๊ธ ์ ๋ชฉ : {{ article.title }}</p>
    <p>๊ธ ๋ด์ฉ : {{ article.content }}</p>
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
# ๊ฐ๋ณ ํํ๋ฆฟ

{% extends 'base.html' %}

{% block content %}
  <h2>DETAIL</h2>
  <h3>{{ article.pk }} ๋ฒ์งธ ๊ธ</h3>
  <hr>
  <p>์ ๋ชฉ : {{ article.title }}</p>
  <p>๋ด์ฉ : {{ article.content }}</p>
  <p>์์ฑ์๊ฐ : {{ article.created_at }}</p>
  <p>์์ ์๊ฐ : {{ article.updated_at }}</p>
  <hr>
  <a href="{% url 'articles:update' article.pk %}">[UPDATE]</a>
  <form action="{% url 'articles:delete' article.pk %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="DELETE">
  </form>
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock content %}

```





###### โก C



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
# ๊ฐ๋ณ ํํ๋ฆฟ

{% extends 'base.html' %}

{% block content %}
  <h1>CREATE</h1>
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="์์ฑ">
  </form>
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock content %}

```



###### โข U



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
# ๊ฐ๋ณ ํํ๋ฆฟ

{% extends 'base.html' %}

{% block content %}
  <h1>UPDATE</h1>
  <form action="{% url 'articles:update' article.pk %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="์์ ">
  </form>
  <hr>
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock content %}

```





###### โฃ D



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





์ขํฉ

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



##### (3) Templates ๋จ๊ณ







### 3. Form๊ณผ ModelForm์ด CRUD์ ๋ฏธ์น๋ ์ํฅ

#### 1) Form ๊ธฐ๋ฅ์ด ํ์ํ ์ด์ 

form์ ๋ค์ด๊ฐ๋ key์ value๊ฐ์ด ์์ต ์์กฐ๊ฐ๋ผ๋ฉด ํ๋ํ๋ ์๋ ฅํ๊ธฐ๋ ์ด๋ ค์ธ ๊ฒ์ด๋ค. ์ด๊ฒ์ form๊ธฐ๋ฅ์ ํตํด ๋จ์ํํ๊ณ  ์๋ํ ํ  ์ ์๋ค.

```python
# forms.py๋ฅผ ์๋ก ๋ง๋ ๋ค.
# ์ฅ๊ณ ๋ด์์ forms์ ๊ธฐ๋ฅ์ ๋ถ๋ฌ์จ๋ค
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
- label & input ์์ ๋ํ 3๊ฐ์ง ์ถ๋ ฅ์ต์
{{ form.as_p }}

- input ์์ ํํ ๋ฐฉ๋ฒ 2๊ฐ์ง
1. Form fields - ์ ํจ์ฑ ๊ฒ์ฌ ์ฒ๋ฆฌ
2. Widgets - input ์์ฑ์ ๋จ์ํ ๋ ๋๋ง ์ฒ๋ฆฌ
```

Form rendering options

https://docs.djangoproject.com/en/3.2/topics/forms/#form-rendering-options

django form rendering options

https://docs.djangoproject.com/en/3.2/ref/forms/widgets/



#### 2) ModelForm๊ธฐ๋ฅ์ด ํ์ํ ์ด์ 

models.py์์ ํ๋๋ฅผ ์ ์ํ๋๋ฐ forms.py์์ ๋ ํ๋๋ฅผ ์ ์ ํ๋ค๊ณ ??? DRY์ ์๋ฐ!!!

```python
# forms.py

from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'

```

modelfielf์ formfield ๋น๊ต

https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/

selecting-the-fields-to-use(์ ๊ต์ฌ๋ฐฉ์๊ณผ ๊ณต์๋ฌธ์๊ฐ ๋ค๋ฅด์ง?)

https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/#selecting-the-fields-to-use



```python
# views.py


```





#### 3) HTTP requests ์ฒ๋ฆฌ

```python
# views.py


```

django shortcuts - render(), redirect(), get_object_or_404()

https://docs.djangoproject.com/en/3.2/topics/http/shortcuts/



### 4. ์ด๋ฏธ์ง๋ฃ๊ธฐ

#### 1) Static files

โ  INSTALLED_APPS ํ์ธ

โก STATIC_URL ์ ์

โข ํํ๋ฆฟ ํ๊ทธ์๋ ฅ๊ณผ STATIC_ROOT์ ์ฐ๊ฒฐ

โฃ ์ฑ์ ์ ์ฅ

```python
# settings.py

STATIC_URL = '/static/'

# STATIC_ROOT = BASE_DIR / 'staticfiles'
# ๋ช๋ น์ด python manage.py collectstatic


STATICFILES_DIRS = [
    BASE_DIR / 'static',
]


```



```django
{# base.html์ ์ ์ฉ #}
```



```django
{# ๊ฐ๋ณ.html์ ์ ์ฉ #}
```





#### 2) Media files

##### (1) Media ์ค๋น

```python
# ํ๋ก์ ํธ urls.py์ ์ถ๊ฐ

from django.conf import settings
from django.conf.urls.static import static


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```



```python
# settings.py์ ์ถ๊ฐ

STATIC_URL = '/static/'
# STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

MEDIA_ROOT = BASE_DIR / 'media'

MEDIA_URL = '/media/'

```



```python
# models.py์ ์ถ๊ฐ

def aritlces_image_path(instance, filename):
    return f'user_{instance.user.pk}/{filename}'


class Article(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)

```

models.py๊ฐ ๋ฐ๋์ด์ migrationsํด์ฃผ๊ธฐ





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
    # ์ด๋ฏธ์งํ๋ ์ฌ์ฉ๋ฒ!!
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
    <input type="submit" value="์์ฑ">
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
    <input type="submit" value="์์ฑ">
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
  <title>์ค๊ณ ๋๋ผ {% block title %}{% endblock title %} </title>
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
    <p>๊ธ ๋ฒํธ : {{ article.pk }}</p>
    <p>๊ธ ์ ๋ชฉ : {{ article.title }}</p>
    <p>๊ธ ๋ด์ฉ : {{ article.content }}</p>
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
{# if๋ฌธ์ผ๋ก ๋๋ ์ค๋ค #}

{% extends 'base.html' %}
{% load static %}

{% block content %}
  <img src="{% static 'articles/sample-img-1.png' %}" alt="sample image">

  <h2>DETAIL</h2>
  <h3>{{ article.pk }} ๋ฒ์งธ ๊ธ</h3>
  {% if article.image %}
    <img src="{{ article.image_thumbnail.url }}" alt="{{ article.image_thumbnail }}">
  {% else %}
    <img src="{% static 'images/default.jpg' %}" alt="default image">
  {% endif %}
  
  <hr>
  <p>์ ๋ชฉ : {{ article.title }}</p>
  <p>๋ด์ฉ : {{ article.content }}</p>
  <p>์์ฑ์๊ฐ : {{ article.created_at }}</p>
  <p>์์ ์๊ฐ : {{ article.updated_at }}</p>
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
    <button>์์ </button>
  </form>
  <hr>
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock content %}

```







#### 3) Image Upload

์ค์น์ฌํญ

```
$ python manage.py makemigrations
$ pip install Pillow

$ python manage.py makemigrations
$ python manage.py migrate

$ pip freeze > requirements.txt
```



#### 4) Image Resizing

์ด๋ฏธ์งํท ์ค์น

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

models์ ๋ณํ๋ก migrations



```python
# ๊ฐ๋ณ.html


```



### 5. ๋ก๊ทธ์ธ/๋ก๊ทธ์์ 

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
      <a href="{% url 'accounts:update' %}">ํ์์ ๋ณด์์ </a>
      <form action="{% url 'accounts:logout' %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="Logout">
      </form>
      <form action="{% url 'accounts:delete' %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="ํ์ํํด">
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
            # ๋ก๊ทธ์ธ !
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





### 6. ํ์๊ฐ์/ํ์์์ /๋น๋ฐ๋ฒํธ์์ 



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
{# ํ์๊ฐ์ #}

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
{# ํ์์ ๋ณด์์  #}

{% extends 'base.html' %}

{% block content %}
  <h1>ํ์์ ๋ณด์์ </h1>
  <form action="{% url 'accounts:update' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
{% endblock content %}
```







```django
{# ๋น๋ฐ๋ฒํธ๋ณ๊ฒฝ #}

{% extends 'base.html' %}

{% block content %}
  <h1>๋น๋ฐ๋ฒํธ ๋ณ๊ฒฝ</h1>
  <form action="{% url 'accounts:change_password' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
{% endblock content %}
```

