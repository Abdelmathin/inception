FROM debian:bullseye

RUN apt-get -y update && apt-get -y upgrade

RUN apt-get -y install python3 pip openssh-server
RUN mkdir -p /etc/python-server/ && pip install flask

COPY conf/main.py /etc/python-server/
COPY tools/setup.py /etc/python-server/

CMD ["python3", "/etc/python-server/setup.py"]
