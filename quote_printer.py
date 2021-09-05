#!/usr/bin/python3

import json, random, os

if __name__ == "__main__":
    lst = json.load(open(os.environ["HOME"] + "/.local/bin/" + "quotes.json"))
    quote : dict = lst[random.randint(0, len(lst) - 1)]
    print(f"{quote['Quote']} -- {quote['Character']} ({quote['Interpreter']}) in \"{quote['Film']}\", {quote['Year']}")
