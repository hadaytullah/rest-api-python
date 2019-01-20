FROM python:3.4.5-slim

## make a local directory
RUN mkdir /app

# set "app" as the working directory from which CMD, RUN, ADD references
WORKDIR /app

# now copy all the files in this directory to /code
ADD . .

# pip install the local requirements.txt
RUN pip install -r requirements.txt

# Listen to port 5000 at runtime
EXPOSE 8080

# Define our command to be run when launching the container
CMD gunicorn wsgi:app --workers 4 --timeout 120 --bind 0.0.0.0:$PORT --reload