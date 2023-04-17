import requests
from bs4 import BeautifulSoup
import csv

# Make a request
url = 'https://www.olx.ro/locuri-de-munca/oradea/'
response = requests.get(url)

# Parse HTML and extract data
soup = BeautifulSoup(response.text, 'html.parser')
p_elements = soup.find_all('p')

# Save data to CSV file
with open('olx_oradea.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Text'])
    for p in p_elements:
        writer.writerow([p.text])
