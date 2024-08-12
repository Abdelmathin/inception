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
	# python3 -m http.server  80 --directory . --bind 0.0.0.0 &
	# python3 -m http.server 443 --directory . --bind 0.0.0.0 &
	${sudo} docker-compose -f srcs/docker-compose.yml up --build

all: $(NAME)

up: init
	${sudo} docker-compose -f srcs/docker-compose.yml up -d

down:
	${sudo} docker-compose -f srcs/docker-compose.yml down

build: init
	${sudo} docker-compose -f srcs/docker-compose.yml build

start: init
	${sudo} docker-compose -f srcs/docker-compose.yml start

restart: init
	${sudo} docker-compose -f srcs/docker-compose.yml restart

stop:
	${sudo} docker-compose -f srcs/docker-compose.yml stop

clean: down
	@${sudo} docker image rm -f $$(docker image ls nginx:ahabachi-inception -q)     1> /dev/null 2> /dev/null || true
	@${sudo} docker image rm -f $$(docker image ls wordpress:ahabachi-inception -q) 1> /dev/null 2> /dev/null || true
	@${sudo} docker image rm -f $$(docker image ls mariadb:ahabachi-inception -q)   1> /dev/null 2> /dev/null || true
	@${sudo} docker network rm ahabachi-inception-network                           1> /dev/null 2> /dev/null || true
	@${sudo} docker volume rm ahabachi-inception-wp-volume                          1> /dev/null 2> /dev/null || true
	@${sudo} docker volume rm ahabachi-inception-db-volume                          1> /dev/null 2> /dev/null || true

fclean: clean
	${sudo} rm -rf ${INCEPTION_WORDPRESS_VOLUME}
	${sudo} rm -rf ${INCEPTION_MARIADB_VOLUME}

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
	${sudo} mkdir -p ${INCEPTION_WORDPRESS_VOLUME}
	${sudo} mkdir -p ${INCEPTION_MARIADB_VOLUME}

re: fclean all

push:
	git add .
	git commit -m "auto-commit"
	git push