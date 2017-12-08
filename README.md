# cirugiapp

Environment configuration
------------------------

1. install necessary system packages

        sudo apt-get install python-dev
        
2. install pip and virtualenv

        wget https://bootstrap.pypa.io/get-pip.py
        sudo python get-pip.py
        sudo pip install virtualenv virtualenvwrapper

3. create and activate virtualenv

        mkvirtualenv cirugiapp
        workon cirugiapp

4. instal python packages

        pip install -r requirements/dev.txt

5. Copy settings template
        
        cp cirugiapp/settings/dev.template.py cirugiapp/settings/dev.py

6. Configure and create DB
        
        sudo apt-get install postgresql
        sudo -u postgres psql postgres
        \password postgres # elegir un password y poner el mismo en cirugiapp/settings/dev.py
        #salir de psql (ctrl+d)
        sudo -u postgres createdb cirugiapp
        python manage.py migrate_schemas

7. Create a superuser
        
        python manage.py createsuperuser
        
9. Run server

        python manage.py runserver
