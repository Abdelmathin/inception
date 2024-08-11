FROM debian:bullseye

RUN apt-get -y update && apt-get -y upgrade && apt-get -y install python redis redis-server systemctl && mkdir -p /etc/redis/

COPY tools/setup.py /etc/redis/setup.py

CMD ["python", "/etc/redis/setup.py"]
