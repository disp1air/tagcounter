import requests
from bs4 import BeautifulSoup
import sys
import logging
from pick import write_data_to_file
from const import filename_for_logging, tag_info_filename
from data import work_with_db
from gui import gui

def main(web_page_address):
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
    try:
        if len(sys.argv) == 1:
            gui()
        elif len(sys.argv) == 2:
            print('Enter command and webpage address, please')
        else:
            command = sys.argv[1]
            web_page_address = sys.argv[2]

            tags_dict = main(web_page_address)
            write_data_to_file(tag_info_filename, tags_dict)
            work_with_db(web_page_address, command)
    except Exception as error:
        print("Enter correct command, please")
        print(error)
