FROM debian:stable

RUN apt-get -y update && apt-get -y upgrade && apt-get -y install python redis redis-server systemctl

RUN mkdir -p /etc/redis/

COPY tools/setup.py /etc/redis/setup.py

CMD ["python", "/etc/redis/setup.py"]
