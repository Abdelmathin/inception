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
    listen                  127.0.0.1:''' + os.environ['INCEPTION_PORT'] + ''' ssl;
    listen                  0.0.0.0:''' + os.environ['INCEPTION_PORT'] + '''   ssl;
    ssl_certificate         /etc/nginx/certificates/inception.crt;
    ssl_certificate_key     /etc/nginx/certificates/inception.key;
    ssl_protocols           TLSv1.2;
    server_name             ''' + os.environ['INCEPTION_SERVER_NAMES'] + ''';

    root                /var/www/wordpress;
    index               index.php;

    location / {
        try_files       $uri $uri/ /index.php?$args;
    }

    location ~ \\.php$ {
        try_files       $uri =404;
        fastcgi_pass    wordpress:''' + os.environ['INCEPTION_WP_BIND_PORT'] + ''';
        fastcgi_param   SCRIPT_FILENAME $document_root$fastcgi_script_name;
        include         fastcgi_params;
    }
}
'''

def create_certificates():
	os.system("mkdir -p /etc/nginx/certificates/")
	os.system('''openssl req -newkey rsa:2048 -nodes '''
		'''-keyout /etc/nginx/certificates/inception.key -x509 '''
		'''-days 365 -out /etc/nginx/certificates/inception.crt '''
		'''-subj "/CN=''' + os.environ['INCEPTION_DOMAIN_NAME'] + '''"''')

def nginx_config():
	with open(__dirname__ + 'sites-enabled/default', 'w') as fp:
		fp.write(NGINX_CONFIG)

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
