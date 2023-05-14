#encoding: UTF-8
#  **************************************************************************  #
#                                                                              #
#                                                          :::      ::::::::   #
#    setup.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ahabachi <ahabachi@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/12 14:58:50 by ahabachi          #+#    #+#              #
#    Updated: 2023/05/12 15:30:55 by ahabachi         ###   ########.fr        #
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

class mariaDB:
	def __init__(self, username, password, host = '0.0.0.0', port = 3306,
		configfile = "/etc/mysql/mariadb.conf.d/50-server.cnf"
		):
		self.username = username
		self.password = password
		self.host = host
		self.port = port
		self.configfile = configfile
		self.cmd = 'mariadb << EOF\n'
	def install(self):
		os.system("apt-get install -y mariadb-server");
	def start(self):
		os.system("service mariadb start");
	def stop(self):
		os.system("service mariadb stop")
	def create(self, name):
		self.name = name
		self.cmd += ("CREATE DATABASE IF NOT EXISTS " + name + ";\n")
	def flush(self):
		self.cmd += ("\nFLUSH PRIVILEGES;")
		self.cmd += '\nEOF\n'
		print (self.cmd)
		os.system (self.cmd)
	def show(self):
		self.cmd += ("\nshow databases;")
	def grant(self):
		self.cmd += "CREATE USER '" + self.username + "'@'%' IDENTIFIED BY '" + self.password+ "';\n"
		self.cmd += "CREATE USER 'root'@'%' IDENTIFIED BY '" + os.environ['DB_ROOT_PASSWORD'] + "';\n"
		self.cmd += "GRANT ALL PRIVILEGES ON " + self.name + ".* TO '" + self.username +"'@'%';\n"
		self.cmd += "GRANT ALL PRIVILEGES ON " + self.name + ".* TO 'root'@'%';"
	def configure(self):
		text = ''
		for line in open(self.configfile):
			l = line.strip()
			if (l):
				if (l.replace('\t', ' ').split(' ')[0] == 'bind-address'):
					continue
				if (l.replace('\t', ' ').split(' ')[0] == 'port'):
					continue
			text += line + '\n'
		text += 'bind-address            = 0.0.0.0\n'
		text += 'port                    = ' + str(self.port) + '\n'
		text = text.replace('localhost', '0.0.0.0')
		text = text.replace('127.0.0.1', '0.0.0.0')
		with open(self.configfile, 'w') as fp:
			fp.write(text)

db = mariaDB(os.environ.get('DB_USER', None), os.environ.get('DB_PASSWORD', None))
db.install()
db.configure()
db.start()
db.create(os.environ.get('DB_NAME', None))
db.grant()
db.flush()
db.show()
db.stop()
os.system("mysqld_safe")
