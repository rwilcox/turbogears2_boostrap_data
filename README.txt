This Turbogears app shows how to use websetup/bootstrap.py to
add bootstrap data to your application, and presents a better way than
the built-in Turbogears way to do this.

If you browse this repository by looking at the diffs, or by following along, time traveling to
each commit, you'll see the evolutions from the out-of-the-box TG way to a more complicated (but more robust) way

Suggested commands to time travel to view the state of the repo in each commit:

    $ git checkout SHA-1  # <-- time travel to this commit
    
    $ git show --pretty="format:" --name-only SHA-1   #< -- will show you all files changed in this commit, so you can investigate yourself
      OR
    $ git whatchanged -p SHA-1 # <-- easy acess to the diff for this commit


This example uses sqlalchemy-migrate to migrate the database too.

Meant to be ran inside a virtualenv. Set it up like:

$ virtualenv --no-site-packages -p python2.6 tg2env
$ cd tg2env/
$ source bin/activate
$ easy_install -i http://www.turbogears.org/2.1/downloads/current/index tg.devtools
$ git clone git://github.com/rwilcox/turbogears2_boostrap_data.git
$ cd turbogears2_boostrap_data
$ python setup.py develop
$ paster setup-app development.ini


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
