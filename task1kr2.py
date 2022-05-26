#4 variant

import csv
import requests
import json

n = int(input())
houses = requests.get(f'https://www.anapioficeandfire.com/api/houses={str(n)}')
houses_list = houses.json()
region_list = []

for i in houses_list:
    a = i["region"], i['name'], i["currentLord"]
    region_list.append([a, i])
region_list.sort(key=lambda x: x[0], reverse=True)


with open("houses.csv", 'a', encoding='utf-8') as file:
    h = csv.writer(file, delimiter = "\t")
    for row in h:
        h.writerow(i)

