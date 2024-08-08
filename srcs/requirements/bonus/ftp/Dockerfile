FROM debian:bullseye

RUN apt-get -y update && apt-get -y upgrade && apt-get -y install python && mkdir /etc/ftp

COPY tools/FTP.py /etc/ftp
COPY tools/setup.py /etc/ftp
COPY conf/vsftpd.json /etc/ftp

CMD ["python", "/etc/ftp/setup.py"]
