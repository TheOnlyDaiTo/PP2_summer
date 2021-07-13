import re
for i in range(int(input())):
    print(bool(re.match('^[-+]?\d*\.\d+$', input())))