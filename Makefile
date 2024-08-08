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

$(NAME): clear
	cd srcs && $(sudo) docker-compose up --build

all: $(NAME)

up: clear
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

fclean: clear
	@$(sudo) docker system prune --all --force || echo ""
	@$(sudo) docker stop $(docker ps -qa) || echo ""
	@$(sudo) docker rm $(docker ps -qa) || echo ""
	@$(sudo) docker rmi -f $(docker images -qa) || echo ""
	@$(sudo) docker volume rm $(docker volume ls -q) || echo ""
	@$(sudo) docker network rm $(docker network ls -q) 2>/dev/null || echo ""

ls:
	@echo ">> containers:"
	$(sudo) docker container ls
	@echo ">> images:"
	$(sudo) docker image ls
	@echo ">> networks:"
	$(sudo) docker network ls
	@echo ">> volumes:"
	$(sudo) docker volume ls

clear:
	@clear

re: fclean all