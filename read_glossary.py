"""
Fills an SQL database from a text file: glossary.txt

sqlite> SELECT gl_term FROM glossary ORDER by gl_term COLLATE NOCASE;
.NET
Agile
AJAX
Apache
Apache Foundation
...

sqlite> select gl_definition from glossary where gl_term = "Tk";
a GUI tool kit, written in tcl.
"""

import sqlite3 as sql
import time
import os

FILE = "glossary.txt"  # adjust as needed

class DB:

    backend  = 'sqlite3'
    user_initials  = 'CWK'
    timezone = int(time.strftime("%z", time.localtime()))
    target_path = os.getcwd()  # current directory
    # is this the filepath you need?  Double check.
    db_name = os.path.join(target_path, 'data', 'glossary.db')

    @staticmethod
    def mod_date():
        return int(time.mktime(time.gmtime()))  # GMT time

    @classmethod
    def connect(cls):
        if cls.backend == 'sqlite3':
            DB.conn = sql.connect(DB.db_name)
            DB.c = DB.conn.cursor()
        elif cls.backend == 'mysql':
            DB.conn = sql.connect(host='localhost',
                                  user='root', port='8889')
            DB.c = DB.conn.cursor()

    @classmethod
    def disconnect(cls):
        DB.conn.close()

    @classmethod
    def save_term(cls, *the_data):
        print(the_data)
        query = ("INSERT INTO Glossary "
        "(gl_term, gl_definition, updated_at, updated_by) "
        "VALUES ('{}', '{}', {}, '{}')".format(*the_data))
        # print(query)
        DB.c.execute(query)
        DB.conn.commit()

class DBcontext:

    def __enter__(self):
        DB.connect()
        return DB

    def __exit__(self, *oops):
        DB.disconnect()
        if oops[0]:
            return False
        return True

def create_table():

    # https://www.sqlite.org/lang_droptable.html
    DB.c.execute("""DROP TABLE IF EXISTS Glossary""")
    DB.c.execute("""CREATE TABLE Glossary
        (gl_term text PRIMARY KEY,
         gl_definition text,
         updated_at int,
         updated_by text)""")

with DBcontext() as dbx:

    create_table()

    with open(FILE, 'r', encoding='UTF-8') as gloss:
        lines = gloss.readlines()

    for line in lines:
        if len(line.strip()) == 0:  # skip blank lines
            continue
        term, definition = line.split(":", 1)
        right_now = DB.mod_date()
        DB.save_term(term[2:].strip(), definition.strip(), 
                     right_now, DB.user_initials)

print("Done!")