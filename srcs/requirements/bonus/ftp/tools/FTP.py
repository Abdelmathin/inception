#encoding: UTF-8
#  **************************************************************************  #
#                                                                              #
#                                                          :::      ::::::::   #
#    FTP.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ahabachi <ahabachi@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/12 14:58:50 by ahabachi          #+#    #+#              #
#    Updated: 2023/05/12 22:25:31 by ahabachi         ###   ########.fr        #
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

class FTP:
	def __init__(self, username, password, root_dir):
		self.dirname = __file__[:-len(__file__.split('/')[-1])]
		self.username = username
		self.password = password
		self.root_dir = root_dir
		os.system('mkdir -p "' + self.root_dir + '"' )
	def install(self):
		os.system('apt-get -y install vsftpd')
	def start(self):
		os.system('service vsftpd stop')
		os.system('/usr/sbin/vsftpd /etc/vsftpd.conf')
		raise "RuntimeError"
	def configure(self):
		cmd  = ('useradd --home /home/' + self.username + '/ --create-home ' + self.username)
		cmd += (' && echo "' + self.username + ':' + self.password + '" | chpasswd')
		cmd += (' && chown -R "' + self.username + ':' + self.username + '" /home/' + self.username + '/')
		os.system(cmd)
		content = open(self.dirname + '/vsftpd.json', 'r').read()
		config = (eval(content.strip()))
		config['local_root'] = self.root_dir
		config['secure_chroot_dir'] = self.root_dir
		for key, value in config.items():
			with open('/etc/vsftpd.conf', 'a') as fp:
				fp.write(key + '=' + value + '\n')
