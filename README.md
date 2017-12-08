# cirugiapp

Configuracion de entorno
------------------------

1. instalar paquetes del sistema necesarios

        sudo apt-get install python-dev
        
2. instalar pip y virtualenv

        wget https://bootstrap.pypa.io/get-pip.py
        sudo python get-pip.py
        sudo pip install virtualenv virtualenvwrapper

3. crear y activar virtualenv

        mkvirtualenv cirugiapp
        workon cirugiapp

4. si mkvirtualenv no funciona entonces

        sudo pip install virtualenv
        virtualenv env
        . env/bin/activate

5. instalar paquetes de python

        pip install -r requirements/dev.txt

6. Copiar template de settings
        
        cp cirugiapp/settings/dev.template.py cirugiapp/settings/dev.py

7. Configurar y Crear BD
        
        sudo apt-get install postgresql
        sudo -u postgres psql postgres
        \password postgres # elegir un password y poner el mismo en cirugiapp/settings/dev.py
        #salir de psql (ctrl+d)
        sudo -u postgres createdb cirugiapp
        python manage.py migrate_schemas

8. Crear un superusuario
        
        python manage.py createsuperuser
        
9. Correr el server de prueba

        python manage.py runserver
