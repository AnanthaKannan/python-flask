# python-flask

## Ubuntu
### Create Viritual env
    python3.6 -m venv env
    virtualenv env --python=python3.6
### To activate venu
    source bin/activate
    source env/bin/activate
### You can confirm you’re in the virtual environment
    which python .../env/bin/python
### Leaving the virtual environment
    deactivate
### To list down the dependencies of your application
    pip freeze > requirements.txt
### Installing packages
    pip install requests
### set the file
    export FLASK_APP=app.py
### run the file
    flask run


## Windows
### Check pip version
    py -m pip --version
### Create Viritual env
    py -m venv env
### To activate venu
    .\env\Scripts\activate
### You can confirm you’re in the virtual environment
   where python .../env/bin/python.exe
### set the file
    set FLASK_APP=app.py
### run the file
    flask run
### Leaving the virtual environment
    deactivate




### How to deploy in heroky


### Error status
 404 not found
 401 Unauthorized Authentication failure
 403 Forbidden: Authorization failure or invalid Application ID.
 200 ok
 201 created
 204 no content