#!/usr/bin/env bash

IRed='\033[0;91m'
NC='\033[0m'
IGreen='\033[0;92m'

python3 --version > /dev/null 

if	[ $? -eq 127 ]; then
	printf "${IRed}Python's not installed\nPlease install the latest version of python3 with your package manager\n${NC}"
	exit 1
else
	printf "${IGreen}Python is installed\n${NC}"
fi

python3 test.py

if [ $? -eq 0 ]; then
	printf "${IGreen}Every package necessary is installed\n${NC}"
elif [ $? -eq 30 ]; then
	printf "${IRed}Both packages are missing\n${NC}"
	pip3 install selenium
	pip3 install beautifulsoup4
elif [ $? -eq 10 ]; then
	printf "${IRed}Selenium is missing\n${NC}"
	pip3 install selenium
elif [ $? -eq 20 ]; then
	printf "${IRed}BeautifulSoup is missing\n${NC}"
	pip3 install beautifulsoup4
fi

first_file=./users.csv

if [ -e "$first_file" ]; then
	printf "${IGreen}Found users.csv, compiling C program\n${NC}"
else
	printf "${IRed}No users.csv found\n${NC}"
	exit 1
fi

cc main.c && ./a.out

python3 soup.py

rm -rf ./users.csv a.out ./output.csv

printf "${IGreen}Done\n${NC}"
