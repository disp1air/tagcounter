import pickle
import sqlite3
from const import db_name, tag_info_filename
from pick import read_data_from_file
from const import tag_keys_filename, tag_values_filename
from datetime import datetime

def work_with_db(web_page_address, command):
    tag_info = read_data_from_file(tag_info_filename)
    
    if command == "--get":
        write_data_to_db(web_page_address, tag_info)
    elif command == "--view":
        read_data_from_db(web_page_address)

def write_data_to_db(web_page_address, data):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    url = "https://" + web_page_address

    c.execute("""CREATE TABLE IF NOT EXISTS tagcounter
        (site_name text, url text, date text, taginfo text)""")
    c.execute("INSERT INTO tagcounter VALUES (?,?,?,?)",
        (web_page_address, url, str(datetime.now()), data))

    conn.commit()
    conn.close()

def read_data_from_db(web_page_address):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    c.execute("SELECT taginfo FROM tagcounter WHERE site_name=?", (web_page_address,))
    print(c.fetchone())

    conn.commit()
    conn.close()
