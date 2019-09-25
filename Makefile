##
## EPITECH PROJECT, 2019
## CAESAR
## File description:
## Makefile
##

DIRECTORIES	= 	Challenge01	\
				Challenge02	\
				Challenge03	\
				Challenge04	\
				Challenge05	\
				Challenge06	\
				Challenge07

all:
	@for i in $(DIRECTORIES); do $(MAKE) -C $$i all || exit 1; done

clean:
	@for i in $(DIRECTORIES); do $(MAKE) -C $$i clean || exit 1; done

fclean:
	@for i in $(DIRECTORIES); do $(MAKE) -C $$i fclean || exit 1; done

.PHONY:	all clean re fclean