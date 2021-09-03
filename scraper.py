#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests, json, re

URL = "https://en.wikipedia.org/wiki/AFI%27s_100_Years...100_Movie_Quotes"

def get(tag):
    if (a := tag.get("a")) is None:
        return tag.get_text()
    else:
        return a.get_text()

def get_clean(tag):
    string = get(tag).replace('\n', '').replace('"', '')
    return re.sub(r"\[[0-9]+\]", '', string)

if __name__ == "__main__":
    
    req = requests.get(URL)
    
    if req.status_code // 100 != 2 :
        raise RuntimeError("status code")
    
    soup = BeautifulSoup(req.text, "html.parser")
    table = soup.find("table", class_ = "wikitable")
    raw_quotes = table.find_all("tr")
    parsed_quotes = list()
    for quote in raw_quotes[1:]:
        tds = quote.find_all_next("td")
        parsed_quotes.append({
            "Quote": get_clean(tds[1]),
            "Character": get_clean(tds[2]),
            "Interpreter": get_clean(tds[3]),
            "Film": get_clean(tds[4]),
            "Year": get_clean(tds[5])
        })
    json.dump(parsed_quotes, open("quotes.json", "w+"))
    print("Done")