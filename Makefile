installdeps:
	pip install -r requirements.txt

createmigrations:
	python manage.py makemigrations

install: installdeps createmigrations

migrate:
	python manage.py migrate

run:
	python manage.py runserver
