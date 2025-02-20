"""
Author: Emanuele Bossi
DS 244
RegEx Assignment 2
Description: complete a given code that extracts data from a simple HTML file and saves it in a JSON file.
"""


"""
This script extracts data from a simple HTML file and saves it in a JSON file.
Regular expressions are used to extract the table data, and the ordered and unordered lists.
Author: Wolf Paulus (wolf@paulus.com)
"""


import re
import json

try:
    with open("simple.html", encoding="utf-8") as file:
        html = file.read()

        # extract the table data
        regex = re.compile(r"<tr>\s*<td>(.*?)</td>\s*<td>(.*?)</td>\s*</tr>", re.DOTALL)
        dict_ = {}
        for key, val in regex.findall(html):
            dict_[key] = val

        # extract 1st list - ordered list:
        list_ = re.findall(r"<ol>(.*?)</ol>", html, re.DOTALL)
        ordered_items = re.findall(r"<li>(.*?)</li>", list_[0], re.DOTALL)

        # extract 2nd list - unordered list:
        list_ = re.findall(r"<ul>(.*?)</ul>", html, re.DOTALL)
        unordered_items = re.findall(r"<li>(.*?)</li>", list_[0], re.DOTALL)

        # Save extracted data to JSON
        result = {
            "table": dict_,
            "ordered": ordered_items,
            "unordered": unordered_items
        }

        result = {
            "dict": dict_,
            "ordered": ordered_items,
            "unordered": unordered_items
        }
        with open("simple.json", "w", encoding="utf-8") as file:
            json.dump(result, file)
except OSError as e:
    print(e)


# Do the same using BeautifulSoup
from bs4 import BeautifulSoup

try:
    with open("simple.html", encoding="utf-8") as file:
        html = file.read()
        
        soup = BeautifulSoup(html, "html.parser")
        
        # extract the table data
        table_data = {}
        for row in soup.find_all("tr"):
            cells = row.find_all("td")
            if len(cells) == 2:
                table_data[cells[0].text.strip()] = cells[1].text.strip()
        
        # extract 1st list - ordered list:
        ordered_items = [li.text.strip() for li in soup.find("ol").find_all("li")]
        
        # extract 2nd list - unordered list:
        unordered_items = [li.text.strip() for li in soup.find("ul").find_all("li")]
        
        # Save extracted data to JSON
        result = {
            "table": table_data,
            "ordered": ordered_items,
            "unordered": unordered_items
        }
        
        with open("simple_BS.json", "w", encoding="utf-8") as file:
            json.dump(result, file)
except OSError as e:
    print(e)