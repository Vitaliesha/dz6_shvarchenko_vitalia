import sys
from itertools import zip_longest

users, hobby, combined = sys.argv[1:]
if __name__ == '__main__':
    with open(users, 'r', encoding='utf-8') as name, \
            open(hobby, 'r', encoding='utf-8') as hobby:
        names = name.read().splitlines()
        hobbys = hobby.read().splitlines()

    users_hobbys_gen = ((names, hobbys) for names, hobbys in zip_longest(names, hobbys, fillvalue=None))

    with open(combined, 'w') as f:
        for user_hobby in users_hobbys_gen:
            f.write(f'{user_hobby[0]}: {user_hobby[1]}\n')
    exit()