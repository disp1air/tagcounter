import sys
from read_write import work_with_db
from gui import gui

def main():
    try:
        if len(sys.argv) == 1:
            gui()
        elif len(sys.argv) == 2:
            print('Enter command and webpage address, please')
        else:
            command = sys.argv[1]
            web_page_address = sys.argv[2]

            work_with_db(web_page_address, command)
    except Exception as error:
        print("Enter correct command, please")
        print(error)

if __name__ == '__main__':
    main()