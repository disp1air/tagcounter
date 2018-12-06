import pickle
import sqlite3
from const import db_name
from pick import read_data_from_file
from const import tag_keys_filename, tag_values_filename

def work_with_db():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    tag_keys = read_data_from_file(tag_keys_filename)
    tag_values = read_data_from_file(tag_values_filename)

    c.execute("CREATE TABLE IF NOT EXISTS tagcounter {nf}".format(nf=tag_keys))
    c.execute("INSERT INTO tagcounter VALUES {tag_values}".format(tag_values=tag_values))

    conn.commit()
    conn.close()
