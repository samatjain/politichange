all: heroku

local:
	python manage.py collectstatic

heroku:
	git pull heroku master
	git push heroku master
	heroku run python manage.py syncdb
#	heroku run python manage.py collectstatic

nuke:
	heroku pg:reset DATABASE_URL

serve:
	. venv/bin/activate; python manage.py runserver

venv: venv/bin/activate
venv/bin/activate: requirements.txt
	test -d venv || virtualenv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/bin/activate

clean:
	rm -rf venv
