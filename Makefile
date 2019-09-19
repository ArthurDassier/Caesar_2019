##
## EPITECH PROJECT, 2019
## CAESAR
## File description:
## Makefile
##

# DIR = Challenge01/

all:
	$(MAKE) -C Challenge01
	$(MAKE) -C Challenge02

clean:
	$(MAKE) clean -C Challenge01
	$(MAKE) clean -C Challenge02

fclean:
	$(MAKE) fclean -C Challenge01
	$(MAKE) fclean -C Challenge02

.PHONY:	all clean re fclean