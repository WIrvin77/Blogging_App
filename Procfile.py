import blogging

web: gunicorn blogging.wsgi
web: gunicorn blogpost:app
