web: newrelic-admin run-program gunicorn -c gunicorn.py.ini wsgi:application
web: python manage.py runserver 0.0.0.0:$PORT --noreload
scheduler: python manage.py celery worker -B -E --maxtasksperchild=1000
worker: python manage.py celery worker -E --maxtasksperchild=1000
