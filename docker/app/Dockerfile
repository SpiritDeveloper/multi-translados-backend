FROM python:3.10-slim-bullseye
ADD . /app
WORKDIR /app 


RUN apt-get -y update
# You will need 
RUN apt install -y postgresql postgresql-contrib

RUN echo "jenkins ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

COPY requirements.txt /app/
RUN pip install -r requirements.txt
