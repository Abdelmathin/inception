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
	def __init__(self, username, password, host, port, configfile):
		self.username   = username
		self.password   = password
		self.host       = host
		self.port       = port
		self.configfile = configfile
		self.cmd        = 'mariadb << EOF\n'
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
		self.cmd += "CREATE USER 'root'@'%' IDENTIFIED BY '" + os.environ["INCEPTION_DB_ROOT_PASSWORD"] + "';\n"
		self.cmd += "GRANT ALL PRIVILEGES ON " + self.name + ".* TO '" + self.username +"'@'%';\n"
		self.cmd += "GRANT ALL PRIVILEGES ON " + self.name + ".* TO 'root'@'%';"
	
	def trimall(self, s):
		for k in "\r\t\n\v\f ":
			s = s.replace(k, "")
		return (s.strip())

	def configure(self):
		text = ""
		for line in open(self.configfile):
			if (self.trimall(line).startswith("bind-address=")):
				continue
			if (self.trimall(line).startswith("port=")):
				continue
			text += line + "\n"
		text += "bind-address            = " + str(self.host) + "\n"
		text += "port                    = " + str(self.port) + "\n"
		for host in ["0.0.0.0", "localhost", "127.0.0.1"]:
			text = text.replace(host, self.host)
		with open(self.configfile, 'w') as fp:
			fp.write(text)

db = mariaDB(
	username   = str(os.environ["INCEPTION_DB_USER"]),
	password   = str(os.environ["INCEPTION_DB_PASSWORD"]),
	host       = str(os.environ["INCEPTION_DB_BIND_HOST"]),
	port       = int(os.environ["INCEPTION_DB_BIND_PORT"]),
	configfile = "/etc/mysql/mariadb.conf.d/50-server.cnf"
)
db.install()
db.configure()
db.start()
db.create(os.environ["INCEPTION_DB_NAME"])
db.grant()
db.flush()
db.show()
db.stop()
os.system("mysqld_safe")
