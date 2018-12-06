import requests
from bs4 import BeautifulSoup
import sys
import logging
from pick import *
from const import tag_keys_filename, tag_values_filename, filename_for_logging
from data import work_with_db

def main():
    web_page_address = sys.argv[1]

    logging.basicConfig(filename=filename_for_logging, level=logging.INFO, format="%(asctime)s %(message)s")
    logging.info('%s', web_page_address)
    
    try:
        response = requests.get("https://" + web_page_address)
    except:
        return print("Wrong webpage address!!!")
    
    soup = BeautifulSoup(response.text, "html.parser")
    tags_dict = {}

    for tag in soup.findAll():
        if tags_dict.get(tag.name):
            tags_dict[tag.name] += 1
        else:
            tags_dict[tag.name] = 1 

    return tags_dict
    
if __name__ == '__main__':
    tags_dict = main()
    write_data_keys_to_file(tag_keys_filename, tags_dict)
    write_data_values_to_file(tag_values_filename, tags_dict)
    work_with_db()
