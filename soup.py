import urllib.request as urllib2
from bs4 import BeautifulSoup


url = 'https://admin.intra.42.fr/users?commit=Search&q%5Bc%5D%5B0%5D%5Ba%5D%5B0%5D%5Bname%5D=campus_users_campus_id&q%5Bc%5D%5B0%5D%5Bp%5D=eq&q%5Bc%5D%5B0%5D%5Bv%5D%5B0%5D%5Bvalue%5D=58&q%5Bc%5D%5B1756235597345%5D%5Ba%5D%5B0%5D%5Bname%5D=pool_year&q%5Bc%5D%5B1756235597345%5D%5Bp%5D=eq&q%5Bc%5D%5B1756235597345%5D%5Bv%5D%5B0%5D%5Bvalue%5D=2025&q%5Bc%5D%5B1756235603985%5D%5Ba%5D%5B0%5D%5Bname%5D=pool_month&q%5Bc%5D%5B1756235603985%5D%5Bp%5D=eq&q%5Bc%5D%5B1756235603985%5D%5Bv%5D%5B0%5D%5Bvalue%5D=september&utf8=%E2%9C%93'

req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
page = urllib2.urlopen( req )

soup = BeautifulSoup(page)

print(soup.prettify())
