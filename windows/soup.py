from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from getpass import getpass
import time
import os

user = []
file_size = 0
i = 0

if not os.path.exists('output.csv'):
    print("No output file from C Program")
    exit(255)

user_input = input("Are you part of the staff? (yes/no): ")
intra_user = input("Please enter your intra username:")
intra_pass = getpass("Please enter your intra password:")

with open('output.csv') as my_file:
    user = [line.rstrip() for line in my_file]



file_size = len(user)

browser = webdriver.Chrome()
if user_input.lower() == "yes":
    login_url = 'https://auth.42.fr/auth/realms/staff-42/protocol/openid-connect/auth?client_id=intra&redirect_uri=https%3A%2F%2Fadmin.intra.42.fr%2Fusers%2Fauth%2Fkeycloak_admin%2Fcallback&response_type=code&state=f364a3f4e86f95e94aa91638e029b38376247200a79a50d7'
elif user_input.lower() == "no":
    login_url = 'https://auth.42.fr/auth/realms/students-42/protocol/openid-connect/auth?client_id=intra&redirect_uri=https%3A%2F%2Fprofile.intra.42.fr%2Fusers%2Fauth%2Fkeycloak_student%2Fcallback&response_type=code&state=b4de7e4354eab555ba76e75639ff2920334ec95c9e38817e'
else:
    print("Wrong input")
    exit(1)
browser.get(login_url)
time.sleep(2)
user_name = browser.find_element(By.ID, "username")
user_name.send_keys(intra_user)
user_pass = browser.find_element(By.ID, "password")
user_pass.send_keys(intra_pass)
user_pass.send_keys(Keys.RETURN)
time.sleep(2)

f = open("final.csv", "w")
img_url = []

while i < file_size:
    url = "https://profile.intra.42.fr/users/" + str(user[i])
    browser.get(url)
    soup = BeautifulSoup(browser.page_source, 'lxml')
    for img in soup.find_all('img', alt=True):
        img_url.append(img['src'])
    f.write(img_url[1])
    f.write('\n')
    img_url = []
    i += 1
browser.close()
