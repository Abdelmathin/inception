#encoding: UTF-8
#  **************************************************************************  #
#                                                                              #
#                                                          :::      ::::::::   #
#    run.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ahabachi <ahabachi@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/12 14:58:50 by ahabachi          #+#    #+#              #
#    Updated: 2023/05/12 18:01:39 by ahabachi         ###   ########.fr        #
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
from PhpFpm import PhpFpm
from WordPress import WordPress

def run():

	print ('# ' * 100)

	os.chdir('/var/www/')

	# Php-Fpm
	phpfpm = PhpFpm()
	print ("Installing Php-Fpm...")
	phpfpm.install()
	print ("Configure Php-Fpm...")
	phpfpm.configure()

	# WordPress
	wb = WordPress()
	print ("Installing WordPress...")
	wb.install()
	print ("Configure WordPress...")
	wb.configure()

	print ("Run Php-Fpm...")
	phpfpm.run()

run()
