i = 0

try:
    import selenium
except ImportError as e:
    i += 10
try:
    import bs4
except ImportError as a:
    i += 20

if i == 10:
    exit(10)
elif i == 20:
    exit (20)
elif i == 30:
    exit(30)
else:
    exit(0)
