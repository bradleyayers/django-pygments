django-pygments is a Django app that provides a template tag and 2 filters for
doing syntax highlighting with Pygments ( http://pygments.org/ ).

Dependencies
============
- pygments


Installation
============
- add ``"django_pygments"`` to your project directory and to ``INSTALLED_APPS``
  in your ``settings.py``
- if you want to see the integrated demo page, add a URL pattern for
  ``django_pygments.views.demo`` and make sure you're using
  ``django.contrib.staticfiles`` if you want the stylesheet to work


Usage
=====
- enclose your code snippet in a pre tag with the non-standard "lang" attribute
  set to a supported language like this: <pre lang="python">....</pre>
- see the view and demo template for examples on how to use the ``pygmentify``
  filter and tag


Notes
=====
- the custom HTML formatter class displays each line as an ordered list
  element, thus implementing line numbering without interfering with
  copy/pasting


The project's site is here: http://od-eon.com/labs/django-pygments/
For technical support use the github issue tracker or contact us at
developers@od-eon.com
