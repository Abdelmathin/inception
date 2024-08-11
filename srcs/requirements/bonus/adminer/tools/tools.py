#encoding: UTF-8
#  **************************************************************************  #
#                                                                              #
#                                                          :::      ::::::::   #
#    tools.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ahabachi <ahabachi@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/10 08:00:09 by ahabachi          #+#    #+#              #
#    Updated: 2023/05/10 10:30:25 by ahabachi         ###   ########.fr        #
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

class Adminer:
	def __init__(self, dirname, host, port):
		self.host = host
		self.port = port
		self.dirname = dirname
	def install(self):
		os.system ('mkdir -p "' + self.dirname + '" && wget "http://www.adminer.org/latest.php" -O "' + self.dirname + '/index.php"')
	def run(self):
		os.system ('php -S ' + str(self.host) + ':' + str(self.port) + ' -t "' + self.dirname + '"')
