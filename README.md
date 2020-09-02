# takkand.com

Source code for Django and PostgreSQL powered website [takkand.com](https://takkand.com).


## To run locally:
### Clone repository
	git clone https://github.com/dmitrytk/takkand.com.git

### Create and activate Python 3.7 virtualenv
	python3 -m venv venv
	source venv/bin/activate

### Install dependencies:
	pip install -r requirements.txt

### Create PotsgreSQL database named 'django_db':
	sudo -u postgres psql
	CREATE DATABASE django_db;


### Create .env for django-environ
	nano project/.env

	DEBUG=1
	SECRET_KEY=<secret_key>
	POSTGRES_PASSWORD=<password>
	POSTGRES_USER=<user>


### Migrate and create superuser
	./manage.py migrate
	./manage.py createsuperuser

### Run local development server
	python manage.py runserver 0.0.0.0:8000

Site is running on 127.0.0.1:8000


## License
[MIT](LICENSE.md)
