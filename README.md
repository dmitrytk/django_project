# takkand.pw

This is the source code for my sandbox Django powered website at 
[takkand.pw](https://takkand.pw).


## To run locally:
### Clone repository
	git clone https://github.com/dmitrytk/takkand.pw.git

### Create and activate Python 3.7 virtualenv
	python3 -m venv venv
	source venv/bin/activate

### Install dependencies::
	pip install -r requirements.txt

### Create PotsgreSQL database named 'django_db':
	sudo -u postgres psql
	CREATE DATABASE django_db;

### Set env variables:
	nano ~/.profile

	export DEBUG=1
	export SECRET_KEY=<secret_key>
	export POSTGRES_PASSWORD=<password>
	export POSTGRES_USER=<user>

	source ~/.profile

### Migrate and create superuser
	python manage.py migrate
	python manage.py createsuperuser

### Run local development server
	python managepy runserver 0.0.0.0:8000

Site is running on 127.0.0.1:8000


## License
[MIT](LICENSE.md)
