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
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': '<project-name>',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
ALLOWED_HOSTS = ['*']
```    
* and change setting for your dev DB 

### If your default(5432) port already use:
Create/init new instance by `pg_ctl`

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


### to be continuous...
