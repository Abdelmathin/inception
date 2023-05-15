#encoding: UTF-8
#  **************************************************************************  #
#                                                                              #
#                                                          :::      ::::::::   #
#    setup.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ahabachi <ahabachi@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/12 14:58:50 by ahabachi          #+#    #+#              #
#    Updated: 2023/05/12 21:02:07 by ahabachi         ###   ########.fr        #
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

def setup():
	content = open('/etc/ssh/ssh_config').read()
	content+= '\nPort ' + os.environ['SSH_PORT'] + '\n'
	with open('/etc/ssh/ssh_config', 'w') as fp:
		fp.write(content)

	os.system('useradd -m -s /bin/bash ' +
		os.environ['SSH_USER'] + ' && echo "' + 
		os.environ['SSH_USER'] +':' + 
		os.environ['SSH_PASSWORD'] +'" | chpasswd')
	os.system('service ssh restart')
	os.system('python3 /etc/python-server/main.py')

setup()
