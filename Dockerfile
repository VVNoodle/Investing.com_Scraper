# Python support can be specified down to the minor or micro version
# (e.g. 3.6 or 3.6.3).
# OS Support also exists for jessie & stretch (slim and full).
# See https://hub.docker.com/r/library/python/ for all supported Python
# tags from Docker Hub.
FROM python:slim

# If you prefer miniconda:
#FROM continuumio/miniconda3

LABEL Name=investing.com_scraper Version=0.0.1
EXPOSE 8080

WORKDIR /app
ADD . /app

# Using pip:
RUN python3 -m pip install -r requirements.txt
RUN pip install --upgrade setuptools
RUN pip install requests beautifulsoup4 pandas
RUN pip freeze > requirements.txt

CMD ["python3", "-m", "investing.com_scraper"]
