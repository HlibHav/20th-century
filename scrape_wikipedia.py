import requests
from bs4 import BeautifulSoup
import pandas as pd

# Fetch Wikipedia page content
url = 'https://en.wikipedia.org/wiki/20th_century'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract major sections
    sections = []
    for heading in soup.find_all(['h2', 'h3']):
        section = {
            'title': heading.text.strip(),
            'content': ''
        }
        next_node = heading.find_next_sibling()
        while next_node and next_node.name not in ['h2', 'h3']:
            if next_node.name == 'p':
                section['content'] += next_node.text + ' '
            next_node = next_node.find_next_sibling()
        sections.append(section)
    
    # Create DataFrame and save CSV
    df = pd.DataFrame(sections)
    df.to_csv('20th_century_data.csv', index=False)
    print('CSV created successfully!')
else:
    print(f'Failed to retrieve page. Status code: {response.status_code}')