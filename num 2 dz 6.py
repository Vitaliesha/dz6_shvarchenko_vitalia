#* (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
#Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
import requests as requests

url = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
req = (el for el in requests.get(url).text.strip().split('\n'))

list_tuples = []
spamer = {}
for el in req:
    el = el.split(' ')
    remote_addr = el[0]
    request_type = el[5][1:]
    requested_resourse = el[6]
    list_tuples.append((remote_addr, request_type, requested_resourse))
    if el[0] not in spamer:
        spamer[el[0]] = 1
    else:
        spamer[el[0]] += 1

spamer = dict([max(spamer.items(), key=lambda k_v: k_v[1])])
print(list_tuples)
print(f'Спамер: id: {list((i for i in spamer.keys()))}, количество запросов: {list((i for i in spamer.values()))}')
