#!/bin/bash

set -e
/wait-for-it.sh --host=db --port=5432 -t 90


cd /code
python3 manage.py migrate

# try to setup the default user and sites
email=test@example.com
username=test
password=Conestoga1
echo "from django.contrib.auth.models import User; User.objects.filter(email='$username').delete(); User.objects.create_superuser('$username', '$email', '$password');" | python3 manage.py shell
echo "from django.contrib.sites.models import Site; Site.objects.create(domain='example.org', name='test2'); Site.objects.create(domain='howtokillyourself.org', name='test');" | python3 manage.py shell

# run the server
python3 manage.py runserver --settings=suicide_site.settings 0.0.0.0:8000
