# EcodomsKotom 

## How to use

### Backend requirements:

  1. Install `pip` - [pip.pypa.io/en/stable/installing](https://pip.pypa.io/en/stable/installing/#installation)
  2. Install `virtualenv` - [virtualenv.pypa.io/en/stable/installation](https://virtualenv.pypa.io/en/stable/installation/#installation)
  3. Install `virtualenvwrapper` - [virtualenvwrapper.readthedocs.io/en/latest/install](https://virtualenvwrapper.readthedocs.io/en/latest/install.html#installation) or command `pip install virtualenvwrapper`
  4. Install `gdal` - [pypi.python.org/pypi/GDAL](https://pypi.python.org/pypi/GDAL) or command `pip install gdal`
  5. Install and run `PostgreSQL`
  6. Install and run`Docker`

### General run:
```commandline
docker build -t ecodomskotom .
```
```commandline
docker-compose up -d
```
Go to - http://localhost:8000

### For run dev server:
Create file `.env.dev`
```dockerfile
POSTGRES_HOST=dev_db_ecodomskotom
POSTGRES_PORT=5432
POSTGRES_USER=pguser
POSTGRES_PASSWORD=pgpass
POSTGRES_DB=pgdb
POSTGRES_ENGINE=django.db.backends.postgresql_psycopg2

DJANGO_SETTINGS_MODULE=_project_.settings

DJANGO_ALLOWED_HOSTS='127.0.0.1 [::1] 0.0.0.0 localhost'
SECRET_KEY=very_secret
DEBUG=1

```
Create file `docker-compose-dev.yml` in source dir
```yaml
version: "3.0"
services:
  db:
    container_name: dev_db_ecodomskotom
    image: postgres:15-alpine
    volumes:
      - ~/.pg/pg_data/ecodomskotom_dev:/var/lib/postgresql/data
    restart: always
    env_file:
      - .env.dev
    networks:
      - custom_dev

  web:
    container_name: dev_web_ecodomskotom
    build: .
    depends_on:
      - db
    env_file:
      - .env.dev
    ports:
      - "7777:8000"
    command: >
      bash -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
    volumes:
      - ./:/ecodomskotom
    networks:
      - custom_dev
networks:
  custom_dev:
    driver: bridge
```

and run
```commandline
docker-compose -p ecodomskotom_dev -f docker-compose-dev.yml up web
```
To check logs in real time:

```commandline
docker logs -f <container_name>  
```

To go in container terminal use:
```commandline
docker exec -it <container_name> /bin/bash  
```

To go psql terminal:
```commandline
psql -U pguser -d pgdb
```
Go to - http://localhost:7777

### Create new project, virtualenv and install requirements: ###
```
git clone https://gitlab.com/homedev6/ecodomskotom.git
```
```
cd <project-name> 
```
```
mkvirtualenv --python=$(which python3.9) <project-name>
```
```pip
pip install -r requirements.txt  # install python requirements
```

### Choose git branch
Our git flow has a simple structure:
- there is **main** and **stage** branch
- create new branch according to the task/case from **stage**
- and every task will be accepted thought **merge request**

Switch to stage branch
```
git checkout stage #or git switch stage
```
Create branch for your case
```
git checkout -b <branchname>
```

### Create file `settings_local.py` in \_project_ and setup `DATABASE` and some local settings: ###
```python
DEBUG = True
SECRET_KEY = '0n-w7wsf^3-ehi^!@m2fayppf55ecodomskotom55^l7k'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',  # for you can Windows 127.0.0.1
        'PORT': '5436'
    }
}
ALLOWED_HOSTS = ['*']
```    
* and change setting for your dev DB 

### If your default(5432) port already use:
Create file `docker-compose-dev.yml` and set up:
```yaml
version: "3.0"
services:
  db:
    container_name: "db"
    image: postgres:14.1-alpine
    restart: always
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
      - POSTGRES_DB=postgres
    ports:
      - "5436:5432"
    networks:
      - custom

networks:
    custom:
      driver: bridge
```


Or create/init new instance by `pg_ctl`
```
initdb -D path/to/initial_db
```
```
pg_ctl -D path/to/initial_db -o "-p 5433" start
```


### Create and migrate database:

    createdb <project-name>  # create postgres database
    (OR sudo su postgres -c "createdb <project-name>")
    python manage.py migrate

### Run dev server:

    python manage.py runserver 8000

### Set up your local gitlab-runner for CI/CD

If you want to start gitlab-runner on your local system - follow [official Docs](https://docs.gitlab.com/runner/install/)

Create the Docker volume:

```
docker volume create gitlab-runner-config
```
Start the GitLab Runner container using the volume we just created:

```
docker run -d --name <proj_name>-gitlab-runner --restart always \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v gitlab-runner-config:/etc/gitlab-runner \
    gitlab/gitlab-runner:latest
```
_For MacOs use `/Users/Shared` instead of `srv`_ 

Register your runner:
```
docker exec -it <proj_name>-gitlab-runner gitlab-runner register
```
Then:

> Enter the GitLab instance URL:
>        
>     https://gitlab.com/ 
>Enter the registration token:
>
>     GR134894178BYr39yzppfjsasL-Mh
> Enter a description for the runner:
> 
>     <Your_name>-Docker.local
> 
> Enter tags for the runner or optional maintenance note for the runner:
> 
>     just enter

You should to see info like: `Registering runner... succeeded                     runner=GR1569417865r39y`

> Enter an executor:  
> 
>      docker
> Enter the default Docker image:
> 
>      alpine:latest  # or ubuntu:20.04


You should to see: 

`Runner registered successfully. Feel free to start it, but if it's running already the config should be automatically reloaded!`

`Configuration (with the authentication token) was saved in "/etc/gitlab-runner/config.toml" `

### For local machine validate project
_Recommended to do this before every creating every commit_

For **lint, pep** and etc use:
```commandline
prospector
```
For **run tests**:
```commandline
pytest 
```
To see how much the **code is covered by tests**, run the command:
```commandline
coverage report
```

### to be continuous...
