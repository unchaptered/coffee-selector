# jinja2

<hr>

## 문법

참고 링크 : https://hackersandslackers.com/flask-jinja-templates/

### 레이아웃 기능

```javascript
// home.html

{% extends 'layout.html' %}

{% block content %}
    <div class="container">
        <h1>{{title}}</h1>
        <p>{{description}}</p>
    </div>
{% endblock %}
```

```javascript
// layout.html

<!doctype html>
<html>

  <head>
    <title>{{title}}</title>
    <meta charset="utf-8">
    <meta name="description" content={{description}}>
    <link rel="shortcut icon" href="/favicon.ico">
  </head>

  <body>
    {% include 'navigation.html' %}
    {% block content %}{% endblock %}
  </body>

</html>
layout
```