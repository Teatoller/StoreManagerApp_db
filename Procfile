web: gunicorn run:app
release: python db_manage.py migrate
heroku ps:scale web=1