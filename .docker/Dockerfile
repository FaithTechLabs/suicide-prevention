FROM python:3.6
ENV PYTHONUNBUFFERED 1

# script to wait for db to spin up
ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /
RUN chmod +x /wait-for-it.sh

# install project requirements
ADD requirements.txt /
RUN pip3 install -r requirements.txt

# create code as a directory and volume
RUN mkdir /code
VOLUME /code
WORKDIR /code

# expose the work port
EXPOSE 8000
