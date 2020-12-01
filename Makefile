install:
	pip install -r requirements.txt

start:
	python manage.py runserver

test:
	python manage.py test

test_coverage:
	coverage run --source='.' manage.py test
	coverage report
	coverage html