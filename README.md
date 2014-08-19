Scheduling app
-----------------

An app to help friends find when they're available.

Running the app
------

Uses Python 2.7.8.
For dependencies, I use pip to install dependencies, and virtualenv to manage them.  Setup for pip can be found
[here](https://pip.pypa.io/en/latest/installing.html).  

Virtualenv is really only nice if you use a command line interface to interact with your code.  You don't need
to worry about it otherwise, though it will help system-wide library versioning conflicts.
To install virtualenv and virtualenvwrapper (simplifies use of virtualenv), just do: 

  pip install virtualenv virtualenvwrapper

On certain platforms virtualenvwrapper may break -- let me know if that's the case for you.
To setup virtualenv for this project, run this command:

  mkvirtualenv scheduling

Then, whenever you want to work on the app, just run:
  
  workon scheduling

and it will load all dependencies that have been installed in that environment.

For installing the dependencies, just run:

  pip install -r requirements.txt

If you need to generate a new requirements file (because you've installed a new dependency), you can do:

  pip freeze > requirements.txt

For running the actual server we'll just use the flask development server for now, which I'm fairly sure
you're familiar with, but can be run by doing:

  python runserver.py

Design of the app
------

Here I'm just going to lay out the basics of what I think this needs for a prototype version.

Data-
  -Users - needed for the basic premise, obviously
  -Schedules - associated with users.  For a prototype we can do one per user, but ultimately it might
    make sense for a user to be able to maintain and share different schedules with different people.
    (for example, a work-related events only calender vs. a complete one)

Server/Views-

Honestly we could do this very straightforwardly with some sort of forms and POST-requests, in sort of
an oldschool style.  I've decided to do this in a more seperated fashion between backend and frontend,
especially so you can see a more modern approach that's a lot more useful nowadays.

routes:
/       - index for the site; for now let's just keep a login form on it.
/login  - possibly POST only, if we don't want it as a seperate view.  Just someplace to send login credentials.
/logout - invalidate the session
/app    - main view of the app, you can edit your schedule and try to synch with other users.  Unsure if this should
            be structured as a single page regardless of how much we add, or if it should be broken into more views.
            For now I'd like to keep it as a single page.
/api/   - api routes.  See the next section for exactly what will be here.  They'll just be data endpoints.

For the actual production server I'm planning to go with Nginx and mod_usgi, but we'll discuss this more when
we get around to hosting/deployment.

API-

I'm unsure how familiar you are with RESTful API design, so please feel free to ask any questions at all.
Definitely feel free to discuss if you think this design doesn't fulfill needs for features you wanted,
etc.

routes:
/users/                  - list of all users.  For now we'll exclude filtering or pagination.
/users/:id               - a specific user
/users/:id/schedules     - a specific user's list of schedules.
/users/:id/schedules/:id - a specific schedule.

I've excluded a base-level schedules endpoint simply because I don't see any case in the app where we
would want to find a schedule outside the context of a user.
