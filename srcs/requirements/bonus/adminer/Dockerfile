FROM debian:bullseye

RUN apt-get -y update && apt-get -y upgrade && apt-get -y install python wget php php-mysql

RUN mkdir -p /etc/adminer

COPY tools/tools.py /etc/adminer/
COPY conf/configure.py /etc/adminer/

CMD ["python", "/etc/adminer/configure.py"]
