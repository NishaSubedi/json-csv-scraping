import requests
from bs4 import BeautifulSoup
import pymysql
import csv
import json

courses = []


for i in range(61):
    url = f"https://edusanjal.com/course/?page={i+1}"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

   
    for div in soup.find_all('div', class_="flex flex-col justify-between flex-grow"):
        
        h6_value = div.find('h6').text.strip() if div.find('h6') else None
        accreditation_value = div.find('li', title="Accreditation").text.strip() if div.find('li', title="Accreditation") else None
        duration_value = div.find('li', title="Duration").text.strip() if div.find('li', title="Duration") else None
        courses.append((h6_value, accreditation_value, duration_value))

    if i % 10 == 0:
        print(f"Page {i+1} reading complete")

print(f"WEB SCRAPING COMPLETE: {len(courses)} entries")


conn = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="demo"
)
x = conn.cursor()


truncate_query = "TRUNCATE TABLE courses;"
x.execute(truncate_query)
conn.commit()

alter_query = "ALTER TABLE courses AUTO_INCREMENT = 1;"
x.execute(alter_query)
conn.commit()


insert_query = """
INSERT INTO courses (level, board, duration)
VALUES (%s, %s, %s)
"""
total_length = len(courses)
print(f"Total length to insert is {total_length}")

for entry in courses:
    x.execute(insert_query, entry)

conn.commit()

print(" ")
print("First 20 data in database is:")


sql = """SELECT * FROM courses"""
x.execute(sql)
rows = x.fetchall()


output_file = 'courses_output.csv'


with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    writer.writerow(['id', 'level', 'board', 'duration'])

    i = 1
   
    for row in rows:
        if i <= 20:
            print(row)
        writer.writerow(row)
        i += 1

print(f"Total items in database is: {i-1}")
print("CSV file written successfully")


formatted_rows = []
for row in rows:
    formatted_row = {
        'id': row[0],
        'level': row[1],
        'board': row[2],
        'duration': row[3]
    }
    formatted_rows.append(formatted_row)


file_path = "output.json"


with open(file_path, 'w') as json_file:
    json.dump(formatted_rows, json_file, indent=4)

print("JSON file created successfully!")

x.close()
conn.close()
