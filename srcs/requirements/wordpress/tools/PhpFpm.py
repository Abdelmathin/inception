#encoding: UTF-8
#  **************************************************************************  #
#                                                                              #
#                                                          :::      ::::::::   #
#    PhpFpm.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ahabachi <ahabachi@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/12 14:58:50 by ahabachi          #+#    #+#              #
#    Updated: 2023/05/12 20:57:00 by ahabachi         ###   ########.fr        #
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

class PhpFpm:
	def __init__(self, version = os.environ['INCEPTION_PHP_VERSION']):
		self.version = version
	def install(self):
		os.system("apt-get -y install php" + self.version + "-fpm")
		os.system("apt-get -y install php-mysql")
		os.system("service php" + self.version + "-fpm start")
	def configure(self):
		content = ''
		for line in open("/etc/php/" + self.version + "/fpm/pool.d/www.conf", 'r'):
			line2 = line.replace('\t','').replace(' ', '')
			if (line2.startswith('listen=')):
				content += 'listen = 0.0.0.0:9000\n'
				continue
			content += line + '\n'
		with open("/etc/php/" + self.version + "/fpm/pool.d/www.conf", 'w') as fp:
			fp.write(content)

	def run(self):
		os.system("service php" + self.version + "-fpm stop")
		os.system("/usr/sbin/php-fpm" + self.version + " -F")
