import requests
import csv
from bs4 import BeautifulSoup


def scrape_datalatam():
    url_base = 'https://www.datalatam.com'
    response = requests.get(url_base)
    soup = BeautifulSoup(response.text, 'html.parser')

    enlaces = []
    for a in soup.select('div.col-md-6 p strong a'):
        enlace = url_base + '/' + a['href']
        enlaces.append(enlace)

    data = []
    for enlace in enlaces:
        response = requests.get(enlace)
        soup = BeautifulSoup(response.content, 'html.parser')

        podcast = soup.find('h1').text.strip()
        episodios = []
        for a in soup.select('div ul li a'):
            enlace_episodio = a['href']
            episodios.append(enlace_episodio)

        data.append([podcast, episodios])

    with open('datalatam.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Podcast', 'Episodios'])
        for d in data:
            writer.writerow(d)

    print('Datos guardados en datalatam.csv')


if __name__ == '__main__':
    scrape_datalatam()

        
