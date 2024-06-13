import requests
from bs4 import BeautifulSoup

url = f"https://edusanjal.com/course"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')


level_divs = soup.find('div', class_='my-6').find_all('div', class_='flex')


levels = [div.find('span', class_='text-sm').text.strip() for div in level_divs]

print(levels)
    
