FROM debian:bullseye

RUN apt-get -y update && apt-get -y upgrade && apt-get -y install python3

RUN mkdir -p /etc/static-website

COPY conf/index.html		/etc/static-website
COPY tools/ahabachi.jpeg	/etc/static-website

WORKDIR /etc/static-website

CMD ["python3", "-m", "http.server", "8080"]
