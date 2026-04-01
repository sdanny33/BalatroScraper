from bs4 import BeautifulSoup
import requests
import csv

def fetch_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all wikitable tables
    tables = soup.find_all('table', class_='wikitable')
    
    if len(tables) >= 2:
        # Get the second wikitable (index 1)
        table = tables[1]
        # Get the second wikitable (index 1)
        table = tables[1]
        
        # Find all rows in the table
        rows = table.find_all('tr')
        
        with open('wiki_links.txt', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for row in rows:
                # Find all cells (both th and td)
                cells = row.find_all(['th', 'td'])
                # Check if there's a second column (index 1)
                if len(cells) >= 2:
                    joker_cell = cells[1]
                    # Find all links in the joker column
                    links = joker_cell.find_all('a')
                    for link in links:
                        href = link.get('href')
                        if href:
                            writer.writerow([href])
    else:
        print(f"Found {len(tables)} wikitable(s), need at least 2")

if __name__ == "__main__":
    url = "https://balatrowiki.org/w/Jokers#List_of_Jokers"
    fetch_page(url)
