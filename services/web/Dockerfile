# services/web/Dockerfile
FROM python:3.10.7-slim-buster

# set work directory
# https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service
ENV APP_HOME /app
WORKDIR $APP_HOME

# allow statements and log message to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED 1


# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
# copy project
COPY . .

EXPOSE 5000

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 run:app