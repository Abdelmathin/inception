FROM debian:bullseye

RUN apt-get -y update && apt-get -y upgrade && apt-get -y install curl && apt-get -y install python && mkdir -p /etc/inception/wordpress/tools && mkdir -p /var/www/html/ && mkdir -p /var/www/wordpress/

COPY tools/PhpFpm.py		/etc/inception/wordpress/tools/
COPY tools/run.py			/etc/inception/wordpress/tools/
COPY tools/WordPress.py		/etc/inception/wordpress/tools/

CMD ["python", "/etc/inception/wordpress/tools/run.py"]
