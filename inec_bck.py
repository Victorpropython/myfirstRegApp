import sqlite3

def connect():
    con=sqlite3.connect("register.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS regista(id INTEGER PRIMARY KEY,lastname text,fname text,other_name text,dateofreg TEXT,formNum TEXT)")
    con.commit()
    con.close()

def insert(lastname,fname,other_name,dateofreg,formNum):
    con=sqlite3.connect("register.db")
    cur=con.cursor()
    cur.execute("INSERT INTO regista VALUES(NULL,?,?,?,?,?)",(lastname,fname,other_name,dateofreg,formNum))
    con.commit()
    con.close()

def view():
    con=sqlite3.connect("register.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM regista")
    rows=cur.fetchall()
    con.close()
    return rows

def search(lastname="",fname="",other_name="",dateofreg="",formNum=""):
    con=sqlite3.connect("register.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM regista WHERE lastname=? OR fname=? OR other_name=? OR dateofreg=? OR formNum=?",(lastname,fname,other_name,dateofreg,formNum))
    rows=cur.fetchall()
    con.close()
    return rows

def update(id,lastname,fname,other_name,dateofreg,formNum):
    con=sqlite3.connect("register.db")
    cur=con.cursor()
    cur.execute("UPDATE regista SET lastname=?,fname=?,other_name=?,dateofreg=?,formNum=?,id=?",(lastname,fname,other_name,dateofreg,formNum,id))
    con.commit()
    con.close()

def delete(id):
    con=sqlite3.connect("register.db")
    cur=con.cursor()
    cur.execute("DELETE FROM regista WHERE id=?",(id,))
    con.commit()
    con.close()


connect()
