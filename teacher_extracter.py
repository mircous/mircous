from bs4 import BeautifulSoup
import requests
import csv

def get_urls():

    venu_list = []
    source = requests.get("https://edu.ge.ch/moodle/course/index.php?fbclid=IwAR2EcCIKG8Iho3r9V39Bf1L4zofZxvOYUy9Nsx4nALcriqye5C2iRAgnH5E")
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')
    sup = soup.find('div', class_ = 'subcategories')
    links = sup.find_all('a', href = True)
    for link in links:
        href = link.get('href')
        venu_list.append(href)
    return venu_list

print(get_urls())
