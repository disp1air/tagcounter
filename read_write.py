from data import read_data_from_db, write_data_to_db

def work_with_db(web_page_address, command):
    if command == "--get":
        write_data_to_db(web_page_address)
    elif command == "--view":
        read_data_from_db(web_page_address)
    else:
        print('Use "--get" or "--view" command, please')
