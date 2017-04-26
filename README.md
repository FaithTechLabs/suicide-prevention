# suicide-prevention
Suicide Prevention website - Waterloo Hackathon

http://howtokillyourself.org

An SEO focused website that aims to be the top result when people search "how to kill yourself". We provide useful resources and let them know they're not alone.

Write in Django 1.10, Foundation

## INSTALL

To install the requirements
`pip3 install -r requirements.txt`

To run database migrations
`python3 manage.py migrate`

To run the suicide site:
`python3 manage.py runserver --settings=suicide_site.settings`

Create a test user
`python3 manage.py createsuperuser --username=test --email=test@example.com`

## Docker Development environment

If you are new to this project the fastest way to get a development environment running is to download docker for ([mac](https://docs.docker.com/docker-for-mac/)/[windows](https://docs.docker.com/docker-for-windows/)/[linux](https://docs.docker.com/engine/installation/linux/)).

Use the following commands from the project root folder.
The site will be available at `http://0.0.0.0:8000`.

    $ docker-compose up
    Starts the app

When you're done working you can kill the containers using `ctrl-c`.

If you run into issues you might have to:

    $ docker-compose build --no-cache --pull
    rebuilds the python dependencies
    $ docker-compose rm -vf
    removes containers and volumes
    $ docker-compose up
    Starts the app with fresh everything

Any issues with docker contact IanEdington (IanEdington@gmail.com, 514.318.3053).
