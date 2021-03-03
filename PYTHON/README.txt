to run gunicorn:
gunicorn --reload --bind=10.1.83.57:5000 wsgi:app

to stop gunicorn:
pkill gunicorn
