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

up: init
	cd srcs && $(sudo) docker-compose up

down:
	cd srcs && $(sudo) docker-compose down

build: init
	cd srcs && $(sudo) docker-compose build

start: init
	cd srcs && $(sudo) docker-compose start

restart: init
	cd srcs && $(sudo) docker-compose restart

stop:
	cd srcs && $(sudo) docker-compose stop

clean: down
	@${sudo} docker image rm -f $$(docker image ls nginx:ahabachi-inception -q)     1> /dev/null 2> /dev/null || true
	@${sudo} docker image rm -f $$(docker image ls wordpress:ahabachi-inception -q) 1> /dev/null 2> /dev/null || true
	@${sudo} docker image rm -f $$(docker image ls mariadb:ahabachi-inception -q)   1> /dev/null 2> /dev/null || true
	@${sudo} docker network rm ahabachi-inception-network                           1> /dev/null 2> /dev/null || true
	@${sudo} docker volume rm ahabachi-inception-wp-volume                          1> /dev/null 2> /dev/null || true
	@${sudo} docker volume rm ahabachi-inception-db-volume                          1> /dev/null 2> /dev/null || true

fclean: clean
	rm -rf ${WORDPRESS_VOLUME}
	rm -rf ${MARIADB_VOLUME}

ls:
	@echo "# # # # # # # # # # # # # # # containers # # # # # # # # # # # # # # #"
	@${sudo} docker container ls | grep "ahabachi-inception" || true
	@echo "# # # # # # # # # # # # # # # images     # # # # # # # # # # # # # # #"
	@${sudo} docker image     ls | grep "ahabachi-inception" || true
	@echo "# # # # # # # # # # # # # # # networks   # # # # # # # # # # # # # # #"
	@${sudo} docker network   ls | grep "ahabachi-inception" || true
	@echo "# # # # # # # # # # # # # # # volumes    # # # # # # # # # # # # # # #"
	@${sudo} docker volume    ls | grep "ahabachi-inception" || true

init:
	mkdir -p ${WORDPRESS_VOLUME}
	mkdir -p ${MARIADB_VOLUME}

re: fclean all

push:
	git add .
	git commit -m "auto-commit"
	git push