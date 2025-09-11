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

intra_user = input("Please enter your intra username:")
intra_pass = getpass("Please enter your intra password:")

with open('output.csv') as my_file:
    user = [line.rstrip() for line in my_file]

f = open("final.csv", "w")

file_size = len(user)

op = webdriver.ChromeOptions()
op.add_argument('headless')
browser = webdriver.Chrome(options=op)
login_url = 'https://auth.42.fr/auth/realms/students-42/protocol/openid-connect/auth?client_id=intra&redirect_uri=https%3A%2F%2Fprofile.intra.42.fr%2Fusers%2Fauth%2Fkeycloak_student%2Fcallback&response_type=code&state=b4de7e4354eab555ba76e75639ff2920334ec95c9e38817e'
browser.get(login_url)
time.sleep(2)
user_name = browser.find_element(By.ID, "username")
user_name.send_keys(intra_user)
user_pass = browser.find_element(By.ID, "password")
user_pass.send_keys(intra_pass)
user_pass.send_keys(Keys.RETURN)
time.sleep(2)


while i < file_size:
    f.write(user[i])
    f.write(';')
    url = "https://profile.intra.42.fr/users/" + str(user[i])
    browser.get(url)
    soup = BeautifulSoup(browser.page_source, 'lxml')
    eval_points = soup.find('span', class_="user-correction-point-value")
    for eval_child in eval_points.descendants:
        f.write(eval_child)
    f.write(';')
    user_coalition = soup.find('span', class_="coalition-span")
    for coalition_child in user_coalition.descendants:
        cleaned_coalition = coalition_child.replace("\n", "")
        f.write(cleaned_coalition)
    f.write('\n')
    i += 1
browser.close()
print("!Done!")
