# django-octicons

[![PyPI](https://img.shields.io/pypi/v/django-octicons.svg)](https://pypi.org/project/django-octicons/)
[![Build Status](https://travis-ci.org/sanketsaurav/django-octicons.svg?branch=master)](https://travis-ci.org/sanketsaurav/django-octicons)
[![Python Versions](https://img.shields.io/pypi/pyversions/django-octicons.svg)](https://pypi.org/project/django-octicons/)
[![License](https://img.shields.io/pypi/l/django-octicons.svg)](https://pypi.org/project/django-octicons/)

Django template tags for using [GitHub Octicons](https://octicons.github.com/), with no other dependencies.

## Installation

Grab it from PyPI using pipenv (or pip):

```sh
$ pipenv install django-octicons
```

Install the app in your project:

```python
# settings.py

INSTALLED_APPS = [
    # other apps
    'octicons',
]
```

## Usage

Load the tag library in your HTML template:

```html
{% load octicons %}
```

And then, you can use the icons like this:

```html
<a class="btn btn-sm" href="#url" role="button">
  {% octicon "eye" %}
  Watch
</a>
```

You can also pass any required attributes:

```html
<a class="btn btn-sm" href="#url" role="button">
  {% octicon "thumbsup" height="60" class="large" %}
  Confirm Purchase
</a>
```

All attributes passed will be added as HTML attributes to the SVG element
of the icon.

### Styling

You should add the following in your styles:

```css
.octicon {
  display: inline-block;
  vertical-align: text-top;
  fill: currentColor;
}
```

The class `octicon` will be present in all icons. You are free to style it however you want.
