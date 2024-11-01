import requests
from bs4 import BeautifulSoup


def get_link_of_games(url_competition, selector): 
    response = requests.get(url_competition)
    soup = BeautifulSoup(response.content, 'html.parser')
    elements = soup.select(selector)
    links = ['https://hokej.si/stat/' + str(element['href']) for element in elements if element.has_attr('href')]
    return links

def get_info_from_game(link):
    link_penalties = link + '#penalties'
    response = requests.get(link)
    soup = BeautifulSoup(response.content, 'html.parser')

    #get kategorija , kraj, date from the game
    kategorija = soup.select_one("#match-info > div.row.meta.meta1 > div:nth-child(1) > b").text.strip()
    kraj = soup.select_one("#match-info > div.row.meta.meta1 > div:nth-child(2) > b").text.strip()
    date = soup.select_one("#match-info > div.row.meta.meta1 > div:nth-child(4) > b").text.strip()
    #print(f'Kategorija: {kategorija} , kraj: {kraj}, datum: {date}.')

    #get the sodniki from the game 
    selector_personal = "#match-info > div.row.meta.meta2 >div"
    list = soup.select(selector_personal)
    sodniki = []
    for stvar in list:
        if any(keyword in stvar.text.lower() for keyword in ['linijski sodnik', 'sodnik', 'glavni sodnik']):
            name_tag = stvar.select_one("b")
            if name_tag: 
                name = name_tag.text.strip() 
                sodniki.append(name)

    #get the penalties from the game
    response = requests.get(link_penalties)
    soup = BeautifulSoup(response.content, 'html.parser')
    length_pen = soup.select("#penalties  div.col-3.col-sm-1.pbp-info")
    type_pen = soup.select("#penalties  div.col-9.col-sm-9.pbp-detail > div.penalty-info")
    penalty_texts = [element.text.strip() for element in length_pen]
    type_texts = [element.text.strip().replace('\t', '') for element in type_pen]

    return sodniki, kategorija, kraj, date, penalty_texts , type_texts

