#encoding: UTF-8
#  **************************************************************************  #
#                                                                              #
#                                                          :::      ::::::::   #
#    setup.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ahabachi <ahabachi@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/04 01:43:12 by ahabachi          #+#    #+#              #
#    Updated: 2023/05/04 23:38:48 by ahabachi         ###   ########.fr        #
#                                                                              #
#  **************************************************************************  #
#                                                                              #
#   █████████            ██████████         ██████████         ██████████      #
#   ██     ██                    ██                 ██         ██      ██      #
#          ██                    ██                 ██         ██      ██      #
#          ██                    ██                 ██                 ██      #
#          ██            ██████████         ██████████                 ██      #
#          ██                    ██                 ██                 ██      #
#          ██                    ██                 ██                 ██      #
#          ██                    ██                 ██                 ██      #
#       ████████         ██████████         ██████████                 ██      #
#                                                                              #
#  **************************************************************************  #

import os

__dirname__ = __file__[:-len(__file__.split('/')[-1])]

NGINX_CONFIG = '''
server {
    listen                  ''' + os.environ['INCEPTION_PORT'] + ''' ssl;
    ssl_certificate         /etc/nginx/certificates/''' + os.environ['INCEPTION_DOMAIN_NAME'] + '''.crt;
    ssl_certificate_key     /etc/nginx/certificates/''' + os.environ['INCEPTION_DOMAIN_NAME'] + '''.key;
    server_name             ''' + os.environ['INCEPTION_DOMAIN_NAME'] + ''';

    root                /var/www/wordpress;
    index               index.php;

    location / {
        try_files       $uri $uri/ /index.php?$args;
    }

    location ~ \\.php$ {
        try_files       $uri =404;
        fastcgi_pass    wordpress:9000;
        fastcgi_param   SCRIPT_FILENAME $document_root$fastcgi_script_name;
        include         fastcgi_params;
    }
}
'''

def create_certificates():
	os.system("mkdir -p /etc/nginx/certificates/")
	os.system('''openssl req -newkey rsa:2048 -nodes '''
		'''-keyout /etc/nginx/certificates/''' + os.environ['INCEPTION_DOMAIN_NAME'] + '''.key -x509 '''
		'''-days 365 -out /etc/nginx/certificates/''' + os.environ['INCEPTION_DOMAIN_NAME'] + '''.crt '''
		'''-subj "/CN=''' + os.environ['INCEPTION_DOMAIN_NAME'] + '''"''')

def nginx_config():
	conf = NGINX_CONFIG
	with open(__dirname__ + 'sites-enabled/default', 'w') as fp:
		fp.write(conf)

def create_default_page():
	if (not os.path.exists('/var/www/html/index.html')):
		os.system("mkdir -p /var/www/html/")
		with open('/var/www/html/index.html', 'w') as fp:
			fp.write("<h1>Hello World!</h1>")
	if (not os.path.exists('/var/www/wordpress/index.php')):
		os.system("mkdir -p /var/www/wordpress/")
		with open('/var/www/wordpress/index.html', 'w') as fp:
			fp.write("<h1>Error Wordpress Not Found!</h1>")

if (__name__ == "__main__"):

    create_certificates()
    nginx_config()
    create_default_page()
    os.system("nginx -g 'daemon off;'")
