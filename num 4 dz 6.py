from itertools import zip_longest

with open('data/users.csv', 'r', encoding='utf-8') as name, \
        open('data/users.csv', 'r', encoding='utf-8') as hobby:
    names = name.read().splitlines()
    hobbys = hobby.read().splitlines()

users_hobbys_gen = ((names, hobbys) for names, hobbys in zip_longest(names, hobbys, fillvalue=None))

with open('data/users_hobby.txt', 'w', encoding='utf-8') as f:
    for user_hobby in users_hobbys_gen:
        f.write(f'{user_hobby[0]}: {user_hobby[1]}\n')