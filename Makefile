all: heroku

local:
	python manage.py collectstatic

heroku:
	git push heroku master
	heroku run python manage.py syncdb
#	heroku run python manage.py collectstatic

nuke: heroku
	heroku pg:reset DATABASE_URL
