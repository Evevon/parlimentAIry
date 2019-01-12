# Using django for webpages -Guide
Web pages for the question answering website are generated with django.
This happens through the use of the following resources and tools:
* templates
* static files
* views.py
* urls.py

## Templates: creating a web page
To create a web page in django, we will use django **templates**. These
templates can be created in the following directory:

```
website/q_answering/templates/q_answering/
```

These templates are just the html files you would use in a similar way
outside of the django framework.


## Static files: creating css, javascript, and media for the web page
Css files, javascript, and media such as images are stored in the static folder
of the project:

```
website/q_answering/static/q_answering/
```

Loading in the static files is necessary to use any of the files in this folder
in your webpage. Put this in the head of your document at the top of your file:
```
{% load static %}
```

### Add css
To add css, just add the css to the currently existing **style.css** file, and
include it as a stylesheet by pasting the following link in the head of the
html file:

```
<link rel="stylesheet" href="{% static 'q_answering/style.css' %}">
```

### Add javascript
Similar fashion as css, include this at the bottom of your file:
```
<script src="{% static 'q_answering/my_js_file.js' %}"></script>
```

### Add media
Also similar, for example an image will become:
```
<img src="{% static 'q_answering/image.png' %}"/>
```

## views.py: make Django recognize your webpage
Django works with **views** and can be found in the following directory:
```
website/q_answering/views.py
```

These views are functions that Django calls, which return a HttpResponse.
An HttpResponse can be things like the rendering of a template, or a redirect
to another view function. The advantage of views are that before the
HttpResponse, one can use python to generate or edit/calculate data, which
can then be passed through to the webpage to be rendered, as context.

### context
A context is simply a python dictionary that can be used to pass variables
which can be used within an html template directly (so this kind of takes
over some of the functionality of PHP)
```
context = {
    'variable_name_for_html': value_of_variable,
}
return render(request, 'q_answering/page.html', context)
```

Then accessing the context variable in html can be done like this:

```
<!-- variable in code -->
{% variable_name_for_html %}

<!-- echo variable -->
{{ variable_name_for_html}}
```

### accessing post values
We can also use the post functionality like in php. Let's say the user
submits a form on the webpage and the action is calling a view. Then in this
view function, we can access the post value the following way:
```
elementvalue = request.POST['elementname']
```

## urls.py: make Django display your webpage on a specified url path
An advantage of Django is that we can specify the name of the url path that will
lead to a certain view. This must be done through the urls.py file.
```
website/q_answering/urls.py
```

### adding a new view to the url path
Assigning a new view to a specified url path is easy. In the urls.py file we
just add a new path to the urlpatterns list, giving up a relative url we want
the user to type in order to visit our webpage, a views function that returns
our webpage in a HttpResponse, and a reference name we can use to reference
our view in the code in a human readable way.
```
path('relative/url/for/display', views.viewFunction, name='referencename')
```

### linking to page
With our newly defined path, we can now use the reference name in our code
to trigger the views function we want to link to. Let's say we want to create
a hyperlink to our viewFunction view as defined previously. We can do this
with this code:

```
<a href="{% url 'referencename' %}"> link </a>
```

### submit action and post
If we want to post values from a form, there are two special things we
need to do:

* action link to specified url
* add csrf token

As an action for the form we link to our view that does the form processing
like explained in the linking to page subsection. We also need to add a
csrf token in Django. This is just one line of code which allows Django to do
some security stuff. The code will look like this:

```
<form action={% url 'formprocessview' %} method="post">
    <!-- add csrf token -->
    {% csrf_token %}
    ...
    <!-- form stuff -->
    ...
</form>
```
