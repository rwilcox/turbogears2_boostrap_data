This file is for you to describe the tg21-sample-data application. 

This Turbogears app shows how to use websetup/bootstrap.py to
add bootstrap data to your application.

It uses sqlalchemy-migrate to migrate the database too.

Meant to be ran inside a virtualenv.

Standard Information Below
======================

Installation and Setup
======================

Install ``tg21-sample-data`` using the setup.py script::

    $ cd tg21-sample-data
    $ python setup.py install

Create the project database for any model classes defined::

    $ paster setup-app development.ini

Start the paste http server::

    $ paster serve development.ini

While developing you may want the server to reload after changes in package files (or its dependencies) are saved. This can be achieved easily by adding the --reload option::

    $ paster serve --reload development.ini

Then you are ready to go.
