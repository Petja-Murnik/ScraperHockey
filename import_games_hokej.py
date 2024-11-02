import requests
from bs4 import BeautifulSoup
from functions_hokej import get_info_from_game, get_link_of_games
import pandas as pd

def main():
    links_to_rezults = [
        #"https://hokej.si/stat/?stat_c=199&stat_v=results", #mlajši dečki
        "https://hokej.si/stat/?stat_c=200&stat_v=results",
        "https://hokej.si/stat/?stat_c=201&stat_v=results",
        "https://hokej.si/stat/?stat_c=202&stat_v=results",
        "https://hokej.si/stat/?stat_c=203&stat_v=results",
        "https://hokej.si/stat/?stat_c=204&stat_v=results",
        "https://hokej.si/stat/?stat_c=205&stat_v=results",
    ]

    df = pd.DataFrame(columns=['date', 'kategorija','kraj', 'sodniki','dolzine kazni','vrste_kazni','link'])
    for url_competition in links_to_rezults:
        selector = "#competition-info div.resulttab_wrapper a.scoresheet-overlay"  
        links = get_link_of_games(url_competition, selector)
        for link in links:
            get_info_from_game(link)
            sodniki, kategorija, kraj, date, penalty_texts , type_texts =  get_info_from_game(link)
            #print(f'''Tekmo kategorije {kategorija}, v {kraj} na {date}, katero so sodili {sodniki}, je bilo {len(penalty_texts)} kazni, porocilo na {link}''')
            new_row = pd.DataFrame([{
                'date': date,
                'kategorija': kategorija,
                'kraj': kraj,
                'sodniki': sodniki,
                'dolzine kazni': penalty_texts,
                'vrste_kazni': type_texts,
                'link': link
            }])
            df = pd.concat([df, new_row], ignore_index=True)

    df.to_csv('rezultati_hokej.csv', index=False, encoding='utf-8')
