FROM debian:bullseye

RUN apt-get -y update && apt-get -y upgrade && apt-get -y install openssl && apt-get -y install nginx && apt-get -y install python

COPY tools/setup.py /etc/nginx/

CMD ["python", "/etc/nginx/setup.py"]

