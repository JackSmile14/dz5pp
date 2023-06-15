# Task N1
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

# russia_only = []
index = 0
key = None

while index < len(geo_logs):
    key = list(geo_logs[index].keys())
    if 'Россия' not in geo_logs[index][key[0]]:
        geo_logs.pop(index)
    else:
        index += 1

print('Visits in Russia:')
print(geo_logs)
print('\n')

###########

# Task N2

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

unique_id = set()
for geo_list in ids.values():
    unique_id.update(geo_list)
unique_id_list = list(unique_id)
print('Unique values:', unique_id_list)
print('\n')


###########

# Task N3

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
sales = [sale for sale in stats.values()]
# print(sales)
best_sites = []
for site, sale in stats.items():
    if sale == max(sales):
        print(f'Maximum-statistic site is {site} with {sale} sales')
        best_sites.append(site)

print('\n')




