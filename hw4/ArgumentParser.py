import argparse
import os
import time
import requests


def download_image(url_synchronous):
    """Функция, которая скачивает изображения с заданного URL-адреса(и выводит время работы в консоль)"""
    if not os.path.exists('images'):
        os.mkdir('images')
    start_time = time.time()
    name = url_synchronous.split('/')[-1]
    resp = requests.get(url_synchronous)
    if resp.status_code == 200:
        with open(f'images\\{name}', 'wb') as file:
            file.write(resp.content)
    print(f'время скачивания изображения({name}): {time.time() - start_time:.2f} сек.')


#  С помощью этого кода можно задавать список URL-адресов, через аргументы командной строки
start_time_all = time.time()

parser = argparse.ArgumentParser(description='Parser to start download_image')
parser.add_argument('-list', metavar='url', action='append', type=str, nargs='*', help='download_image sending URL')

args = parser.parse_args()

for url in args.list[0]:
    download_image(url)

print(f'Общее времени выполнения программы: {time.time() - start_time_all:.2f}')
