This file is for you to describe the tg21-sample-data application. Typically
you would include information such as the information below:

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
