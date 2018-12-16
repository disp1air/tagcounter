import requests
from bs4 import BeautifulSoup
from const import filename_for_logging
import logging

def tag_count(web_page_address):
    logging.basicConfig(filename=filename_for_logging, level=logging.INFO, format="%(asctime)s %(message)s")
    logging.info('%s', web_page_address)
    
    try:
        response = requests.get("https://" + web_page_address)
    except:
        print("Wrong webpage address!!!")

    soup = BeautifulSoup(response.text, "html.parser")
    tags_dict = {}
    
    for tag in soup.findAll():
        if tags_dict.get(tag.name):
            tags_dict[tag.name] += 1
        else:
            tags_dict[tag.name] = 1 

    return tags_dict