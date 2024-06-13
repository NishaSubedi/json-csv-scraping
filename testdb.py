import requests
from bs4 import BeautifulSoup
import pymysql
import csv
import json

courses =[]

to_scrape = 'Degree'

url = f"https://edusanjal.com/course/?page=1"
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

degree_dict = {}
level_dict = {}

divs = soup.find_all('div', class_='border-b last:border-none border-gray-300 mt-4 px-4')
for div in divs:
    h5_elements = div.find_all('h5', class_='text-sm font-bold')

    
    for h5 in h5_elements:
        span_text = h5.find('span').get_text(strip=True)
        
        if span_text == 'Degree':
            div_content = div.find('div', class_='my-6 max-h-64 overflow-auto-imp overflow-y-auto scrollbar-thin scrollbar-thumb-gray-300 scrollbar-track-gray-100 scrolling-touch')


            
            labels = div_content.find_all('label')

            
            for label in labels:
                spans = label.find_all('span')
                if len(spans) == 2:
                    degree_name = spans[0].get_text(strip=True)
                    count = spans[1].get_text(strip=True)
                    print(f"Degree Name: {degree_name}, Count: {count}")
                    degree_dict[degree_name] = count

        if span_text == 'Level':
            div_content = div.find('div', class_='my-6 max-h-64 overflow-auto-imp overflow-y-auto scrollbar-thin scrollbar-thumb-gray-300 scrollbar-track-gray-100 scrolling-touch')
            
            labels = div_content.find_all('label')

            
            for label in labels:
                spans = label.find_all('span')
                if len(spans) == 2:
                    level_name = spans[0].get_text(strip=True)
                    count = spans[1].get_text(strip=True)
                    print(f"Level Name: {level_name}, Count: {count}")
                    level_dict[level_name] = count
            print(f"Levels SCRAPING COMPLETE: {len(labels)} entries")
    
print(level_dict)        

formatted_rows = [{
    'Level': level_dict, 
    'Degree' : degree_dict
}
]


file_path = "output_sidebar.json"

with open(file_path, 'w') as json_file:
    json.dump(formatted_rows, json_file, indent=4)

print("JSON file created successfully!")
