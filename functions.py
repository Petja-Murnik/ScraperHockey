import requests
from bs4 import BeautifulSoup
import os
import urllib.parse

class HockeyGameScraper:
    def __init__(self, base_url, output_file='game_reports.txt'):
        self.base_url = base_url
        self.output_file = output_file

    def get_game_report_links(self):
        response = requests.get(self.base_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all links to game reports
        game_links = []
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            # Identify game report links based on a unique pattern in the URL
            if 'game-report' in href:  # Replace 'game-report' with the actual identifier in URLs
                full_url = urllib.parse.urljoin(self.base_url, href)
                game_links.append(full_url)
        return game_links

    def acquire_game_info(self, game_url):
        response = requests.get(game_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract game information
        game_info = {}
        game_info['date'] = soup.find('div', class_='game-date').get_text(strip=True)
        game_info['teams'] = soup.find('div', class_='teams').get_text(strip=True)
        game_info['score'] = soup.find('div', class_='score').get_text(strip=True)
        # Add more fields as necessary

        return game_info

    def write_game_info(self, game_info):
        with open(self.output_file, 'a', encoding='utf-8') as file:
            file.write(f"Date: {game_info.get('date', 'N/A')}\n")
            file.write(f"Teams: {game_info.get('teams', 'N/A')}\n")
            file.write(f"Score: {game_info.get('score', 'N/A')}\n")
            file.write("-" * 40 + "\n")

    def scrape_games(self):
        game_links = self.get_game_report_links()
        print(f"Found {len(game_links)} game reports.")
        for idx, link in enumerate(game_links, 1):
            print(f"Scraping game {idx}/{len(game_links)}: {link}")
            try:
                game_info = self.acquire_game_info(link)
                self.write_game_info(game_info)
            except Exception as e:
                print(f"Failed to scrape {link}: {e}")


# Usage
if __name__ == "__main__":
    base_url = "https://hokej.si/stat/?stat_c=199&stat_v=results"  # Replace with the actual URL
    scraper = HockeyGameScraper(base_url)
    scraper.scrape_games()
    print(f"Game information has been written to {scraper.output_file}")                