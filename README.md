AdminLTE Templates, Template Tags, and Admin Theme for Django
=============================================================

[![pypi_badge](https://badge.fury.io/py/django-adminlte4.png)](https://pypi.python.org/pypi/django-adminlte4)
[![Published on Django Packages](https://img.shields.io/badge/Published%20on-Django%20Packages-0c3c26)](https://djangopackages.org/packages/p/django-adminlte4/)

Django AdminLTE4 provides the functionality of the AdminLTE4 theme
to developers in the form of standard base templates. Optional styling for
Django's built-in admin interface is also provided.

Installation
------------

- Installation using pip:

   `pip install django-adminlte4`

- Add to installed apps:
  ```python
    INSTALLED_APPS = [
         # General use templates & template tags (should appear first)
        'adminlte4',
         # Optional: Django admin theme (must be before django.contrib.admin)
        'adminlte4_theme',
        ...
    ]
  ```
- Don't forget to collect static
    
   `python manage.py collectstatic`

Usage
-----

The [base template] is designed to be highly customisable. Template blocks are provided to
allow you to hook in customisations as you wish

### Admin Theme Usage

Install as per the above installation instructions. The django admin UI should then change as expected.

Documentation
-------------
Since, this package was created by  [Nischal Lamichhane](https://github.com/hehenischal/) as the package maintainer wasnt accepting PR fixing a critical issue in django 5.1, That error has been fixed and nothing else was added, you can refer to old docs which can be found at: http://django-adminlte3.readthedocs.io

Credits
-------

This project a based heavily on work by the following:

* dnaextrim for [django_adminlte_x]
* beastbikes for [django-adminlte]
* adamcharnock for [django-adminlte2]
* d-demirci for [django-adminlte3]
* hehenischal for [django-adminlte4]


  [django_adminlte_x]: https://github.com/dnaextrim/django_adminlte_x
  [django-adminlte]: https://github.com/beastbikes/django-adminlte/
  [django-adminlte2]: https://github.com/adamcharnock/
  [django-adminlte3]: https://github.com/d-demirci/django-adminlte3
  [django-adminlte4]: https://github.com/hehenischal/django-adminlte4
  [base template]: https://github.com/hehenischal/django-adminlte4/blob/master/adminlte3/templates/adminlte/base.html

Screenshots
-----------
Admin Area:
    
* Home :![admin screenshot](https://user-images.githubusercontent.com/24219129/68544333-214e8c00-03d3-11ea-91a1-4cfb94d2b136.png)

* Model :![model screenshot](https://user-images.githubusercontent.com/24219129/68544364-77233400-03d3-11ea-97b3-350884c68f6a.png)

* Editing Model: ![model edit](https://user-images.githubusercontent.com/24219129/68544387-b6518500-03d3-11ea-9f28-27df1d996b06.png)


Site Area:

* Landing: ![site area](https://user-images.githubusercontent.com/24219129/68544298-cd43a780-03d2-11ea-8506-3abfa341a914.png)
