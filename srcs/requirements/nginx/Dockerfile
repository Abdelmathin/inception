FROM debian:bullseye

RUN apt-get -y update && apt-get -y upgrade && apt-get -y install openssl
RUN apt-get -y install nginx && apt-get -y install python

COPY tools/setup.py /etc/nginx/

COPY conf/nginx-ahabachi.conf /etc/nginx/

RUN python /etc/nginx/setup.py

CMD ["nginx", "-g", "daemon off;"]
