# EcodomsKotom 

## How to use

### Backend requirements:

  1. Install `pip` - [pip.pypa.io/en/stable/installing](https://pip.pypa.io/en/stable/installing/#installation)
  2. Install `virtualenv` - [virtualenv.pypa.io/en/stable/installation](https://virtualenv.pypa.io/en/stable/installation/#installation)
  3. Install `virtualenvwrapper` - [virtualenvwrapper.readthedocs.io/en/latest/install](https://virtualenvwrapper.readthedocs.io/en/latest/install.html#installation) or command `pip install virtualenvwrapper`
  4. install `gdal` - [pypi.python.org/pypi/GDAL](https://pypi.python.org/pypi/GDAL) or command `pip install gdal`
  5. Install and run `PostgreSQL`

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

For start gitlab-runner on Docker:
```
docker run -d --name gitlab-runner --restart always \
  -v /srv/gitlab-runner/config:/etc/gitlab-runner \
  -v /var/run/docker.sock:/var/run/docker.sock \
  gitlab/gitlab-runner:latest
```
_For MacOs use `/Users/Shared` instead of `srv`_ 
```
docker exec -it gitlab-runner gitlab-runner register
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
