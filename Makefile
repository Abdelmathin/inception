 #  **************************************************************************  #
#                                                                              #
#                                                          :::      ::::::::   #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ahabachi <ahabachi@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/12 14:58:50 by ahabachi          #+#    #+#              #
#    Updated: 2023/05/13 00:08:42 by ahabachi         ###   ########.fr        #
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

include srcs/.env

# make <rule> sudo=sudo

NAME=inception

$(NAME): init
	cd srcs && $(sudo) docker-compose up --build

all: $(NAME)

up:
	cd srcs && $(sudo) docker-compose up

down:
	cd srcs && $(sudo) docker-compose down

build:
	cd srcs && $(sudo) docker-compose build

start:
	cd srcs && $(sudo) docker-compose start

restart:
	cd srcs && $(sudo) docker-compose restart

stop:
	cd srcs && $(sudo) docker-compose stop

clean: down
	@${sudo} docker image rm -f $$(docker image ls nginx:inception-2023.04.13 -q)     1> /dev/null 2> /dev/null || true
	@${sudo} docker image rm -f $$(docker image ls wordpress:inception-2023.04.22 -q) 1> /dev/null 2> /dev/null || true
	@${sudo} docker image rm -f $$(docker image ls mariadb:inception-2023.04.29 -q)   1> /dev/null 2> /dev/null || true
	@${sudo}  docker network rm inception-network                                     1> /dev/null 2> /dev/null || true

fclean: clean

ls:
	@echo "# # # # # # # # # # # # # # # containers # # # # # # # # # # # # # # #"
	@${sudo} docker container ls
	@echo "# # # # # # # # # # # # # # # images # # # # # # # # # # # # # # # # #"
	@${sudo} docker image ls
	@echo "# # # # # # # # # # # # # # # networks # # # # # # # # # # # # # # # #"
	@${sudo} docker network ls
	@echo "# # # # # # # # # # # # # # # volumes # # # # # # # # # # # # # # # # #"
	@${sudo} docker volume ls

init:
	mkdir -p ${WORDPRESS_VOLUME}
	mkdir -p ${MARIADB_VOLUME}

re: fclean all