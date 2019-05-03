# Python support can be specified down to the minor or micro version
# (e.g. 3.6 or 3.6.3).
# OS Support also exists for jessie & stretch (slim and full).
# See https://hub.docker.com/r/library/python/ for all supported Python
# tags from Docker Hub.
FROM python:alpine

LABEL Name=bigdatafed Version=0.0.1
EXPOSE 8080

WORKDIR /app
ADD . /app

# Using pipenv:
RUN python3 -m pip install pipenv
RUN pipenv install --ignore-pipfile
