#encoding: UTF-8
#  **************************************************************************  #
#                                                                              #
#                                                          :::      ::::::::   #
#    WordPress.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ahabachi <ahabachi@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/12 14:58:50 by ahabachi          #+#    #+#              #
#    Updated: 2023/05/12 22:25:01 by ahabachi         ###   ########.fr        #
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
import time

class WordPress:
	def __init__(self, version = os.environ['INCEPTION_WP_VERSION']):
		self.logs_file = '/etc/inception/wordpress/tools/logs'
		self.version   = version
		self.link      = "https://wordpress.org/wordpress-" + version + ".tar.gz"
	def install(self):

		os.system("curl -o wordpress.tar.gz -fL " + self.link)
		os.system('tar -xzf wordpress.tar.gz')
		os.system('curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar')
		os.system('chmod +x wp-cli.phar && mv ./wp-cli.phar /bin/')

	def configure(self):

		data = open('wordpress/wp-config-sample.php').read()
		
		data = data.replace(
			"define( 'DB_NAME', 'database_name_here' );",
			"define( 'DB_NAME', '" + os.environ["INCEPTION_DB_NAME"] + "' );"
			)

		data = data.replace(
			"define( 'DB_USER', 'username_here' );",
			"define( 'DB_USER', '" + os.environ['INCEPTION_DB_USER'] + "' );"
			)

		data = data.replace(
			"define( 'DB_PASSWORD', 'password_here' );",
			"define( 'DB_PASSWORD', '" + os.environ['INCEPTION_DB_PASSWORD'] + "' );",
			)

		data = data.replace(
			"define( 'DB_HOST', 'localhost' );",
			"define( 'DB_HOST', '" + os.environ["INCEPTION_DB_BIND_HOST"] + "' );",
			)

		with open('wordpress/wp-config.php', 'w') as fp:
			fp.write(data)

		for step in range(100):
			cmd = (
				'cd /var/www/wordpress && '
				'wp-cli.phar core download --allow-root'
				' 1> "' + self.logs_file + '" 2> "' + self.logs_file + '"'
			)

			cmd += '\n' + ('wp-cli.phar core install '
				'--url="'            + os.environ['INCEPTION_DOMAIN_NAME'] + '" '
				'--title="'          + os.environ['INCEPTION_WP_TITLE']    + '" '
				'--admin_user="'     + os.environ['INCEPTION_WP_USER']     + '" '
				'--admin_password="' + os.environ['INCEPTION_WP_PASSWORD'] + '" '
				'--admin_email="'    + os.environ['INCEPTION_WP_EMAIL']    + '" '
				'--allow-root'
				' 1>> "' + self.logs_file + '" 2>> "' + self.logs_file + '"'
				)
			
			cmd += '\n' + ('wp-cli.phar core install '
				'--url="'            + os.environ['INCEPTION_DOMAIN_NAME'] + '" '
				'--title="'          + os.environ['INCEPTION_WP_TITLE']    + '" '
				'--admin_user="'     + os.environ['INCEPTION_WP_USER']     + '" '
				'--admin_password="' + os.environ['INCEPTION_WP_PASSWORD'] + '" '
				'--admin_email="'    + os.environ['INCEPTION_WP_EMAIL']    + '" '
				'--allow-root'
				' 1>> "' + self.logs_file + '" 2>> "' + self.logs_file + '"'
				)

			cmd += '\n' + ('wp user create "' + os.environ['INCEPTION_WP_AUTHOR_USER'] + '" "'
				+ os.environ['INCEPTION_WP_AUTHOR_MAIL'] + 
				'" --role=author --user_pass="'
				+ os.environ['INCEPTION_WP_AUTHOR_PASSWORD'] + '" --allow-root'
				' 1>> "' + self.logs_file + '" 2>> "' + self.logs_file + '"'
			)

			cmd += '\n' + (
				'wp-cli.phar plugin install redis-cache '
				'--activate '
				'--allow-root'
				' 1>> "' + self.logs_file + '" 2>> "' + self.logs_file + '"'
			)

			cmd += '\n' + ('wp-cli.phar redis enable --allow-root')

			cmd += ' 1>> "' + self.logs_file + '" 2>> "' + self.logs_file + '"'

			os.system(cmd)

			logs = open(self.logs_file).read()

			if ('Success:' in logs):
				break			
			time.sleep(1)
