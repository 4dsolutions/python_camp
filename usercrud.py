#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 11:39:27 2017
Modified May 31, 2018
Modified Apr 18, 2019
Modified Apr  2, 2020
Modified Apr  3, 2020

@author: Kirby Urner

usercrud.py is about doing basic... 

Creating
Retrieving
Updating
Deleting

plus...

Authenticating

w/r to a Users table.  Good review of DB API.

Designed for interactive use from the REPL.

We'll use connector.py for our db connection.
"""

from connector import DB
import hashlib
import os

# modify this to suit, like settings.py
PATH = "./data"
filepath = os.path.join(PATH, "users.db")

def check_tables():
    with DB(filepath) as db:
        db.curs.execute("SELECT * FROM sqlite_master where type='table'")
        results = db.curs.fetchall()
        if results and "Users" in results[0]:
            return True
        else:
            print("No Users table")
            return False
    
def fetch_all():
    with DB(filepath) as db:
        if check_tables():
            db.curs.execute("SELECT * FROM Users")
            results = db.curs.fetchall()
            if results:
                return tuple(results)
            else:
                print("Users table empty")
    
def fetch_one(user_name):
    with DB(filepath) as db:
        if check_tables():
            db.curs.execute("SELECT * FROM Users "
                            "WHERE username = ?", 
                            (user_name,))
            try:
                results = db.curs.fetchone()
                if results:
                    return tuple(results)
                else:
                    print("Not found")
            except TypeError:
                return None
        
def zap_table():
    with DB(filepath) as db:
        db.curs.execute("DROP TABLE IF EXISTS Users")
        
def create_table():
    if check_tables():
        return "Table already exists"
    else:
        with DB(filepath) as db:
            db.curs.execute("CREATE TABLE Users "
                                  "(username text, "
                                  "password text)") 
        print("Table created")
    
def add_one(user_name, pw):
    with DB(filepath) as db:
        if check_tables():
            if fetch_one(user_name):
                print("User already exists")
                return
            hashpw = hashlib.sha256(bytes(pw, encoding='utf-8')).hexdigest()
            db.curs.execute("INSERT INTO Users "
                            "(username, password) "
                            "VALUES (?, ?)", 
                            (user_name, hashpw))
            db.conn.commit()
            print("User added")
                        
def delete_one(user_name):
    with DB(filepath) as db:
        
        if not check_tables():
            return
        
        if not fetch_one(user_name):
            print("User does not exists")
            return
        db.curs.execute("DELETE FROM Users "
                        "WHERE username = ? ",
                        (user_name,))
        db.conn.commit()
        print("User deleted")
        
def change_one(user_name, newpw):
    # http://www.sqlitetutorial.net/sqlite-update/
    with DB(filepath) as db:
        if not check_tables():
            return
        if not fetch_one(user_name):
            print("User does not exists")
            return
        # pass to placeholders in right order!
        hashpw = hashlib.sha256(bytes(newpw, encoding='utf-8')).hexdigest()
        db.curs.execute("UPDATE Users "
                        "SET password = ? "
                        "WHERE username = ? ",
                        (hashpw, user_name))
        db.conn.commit()
        print("Info changed")

def auth(user_name, pw=None):
    if not pw:
        pw = input("What is the password? : ")
        if not pw:
            return
    hashpw = hashlib.sha256(bytes(pw, encoding='utf-8')).hexdigest()
    got_one = fetch_one(user_name)
    if got_one:
        if got_one[1] == hashpw:
            print("Access Allowed!")
        else:
            print("Access Denied")

# used when input prompts are needed
def fetch():
    who = input("User? > ")
    result = fetch_one(who) 
    print("{}: {}".format(*result))

def fetchall():
    for rec in fetch_all():
        print("{}: {}".format(*rec))
    
def authenticate():
    who = input("User? > ")
    pw  = input("Password? > ")
    auth(who, pw)        

def addone():
    who = input("User? > ")
    pw  = input("Password? > ")
    add_one(who, pw) 

def remone():
    who = input("User? > ")
    delete_one(who)
    
def the_help():
    print("$ python usercrud.py name\n"
          "where name is:\n",
          " ".join(menu_options.keys()) + "\n")
 
menu_options = {
        "fetchone": fetch,
        "fetchall": fetchall,
        "addone": addone,
        "remove": remone,
        "auth": authenticate,
        "build": create_table, 
        "zap": zap_table,
        "--help": the_help,
        "-h": the_help}
    
if __name__ == "__main__":
    import sys
    if len(sys.argv)>1:
        requested_op = sys.argv[1]
        # print sys.argv
        if requested_op in menu_options:
            # don't just eval() whatever is passed in!
            print("Selected: ", requested_op)
            menu_options[requested_op]()
    else:       
        the_help()   