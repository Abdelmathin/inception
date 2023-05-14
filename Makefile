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

NAME	=	inception

re: all

$(NAME): clear
	cd srcs && docker-compose up --build

all: $(NAME)

up: clear
	cd srcs && docker-compose up

down:
	cd srcs && docker-compose down

fclean: clear
	@docker system prune --all --force || echo ""
	@docker stop $(docker ps -qa) || echo ""
	@docker rm $(docker ps -qa) || echo ""
	@docker rmi -f $(docker images -qa) || echo ""
	@docker volume rm $(docker volume ls -q) || echo ""
	@docker network rm $(docker network ls -q) 2>/dev/null || echo ""

clear:
	@clear
