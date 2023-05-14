#encoding: UTF-8
#  **************************************************************************  #
#                                                                              #
#                                                          :::      ::::::::   #
#    setup.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ahabachi <ahabachi@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/12 14:58:50 by ahabachi          #+#    #+#              #
#    Updated: 2023/05/12 18:25:44 by ahabachi         ###   ########.fr        #
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

class Redis:
	def setup(self):
		data = open("/etc/redis/redis.conf").read()
		data = data.replace('127.0.0.1', '0.0.0.0')
		data = data.replace('localhost', '0.0.0.0')
		with open("/etc/redis/redis.conf", 'w') as fp:
			fp.write(data)
	def run(self):
		os.system('systemctl enable redis-server')
		os.system('systemctl stop redis-server')
		os.system('redis-server --protected-mode no')

rd = Redis()
rd.setup()
rd.run()
