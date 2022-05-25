import sys


with open ('data/bakery.csv', 'a', encoding='utf-8') as f:
    f.write(f'{sys.argv[0]}\n')
exit()