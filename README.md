MyDjangoAngularSeed (Single Domain App: Angular, Django, uWSGI, nginx)
======================================================================

A single domain Django SPA (using Angular JS) with a Django REST API backend.

This is a rough guide on how to set up a basic Django Web application which will work as a SPA service one index.html, Django REST API as a backend webservice within the same domain.  It will also serve up static content including javascript (your app & angular), css etc…We will also use django’s admin facility to control the model within the REST API.  

So the components are:
* Django Web App (index.html + static content: css, Angular JS etc…)
* Django REST API (has model, admin pages, returning data as JSON)

**For Development**
During development use “python manage.py runserver” which should work service everything.  

**For Deployment (Live)**
We’ll use uWSGI & nginxl:
* uWSGI will serve up the django app
* nginx will prxy requests to uWSGI & also serve up static content directly  







