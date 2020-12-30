# Lo-fi Station
A music player for playing/discovering lo-fi songs. It uses the Django Framework.


# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone https://github.com/alyssagao1120/lofi-station.git
    $ cd lofi-station

Activate the virtualenv for your project.

Install project dependencies:

    $ pip install -r requirements/local.txt


Then, apply the migrations:

    $ python manage.py migrate


You can now run the development server:

    $ python manage.py runserver