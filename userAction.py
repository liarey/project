import sqlite3

cnt=sqlite3.connect("store.db")

def user_login(user,pas):
    global cnt
    sql=''' SELECT * FROM users WHERE username=? AND pass=?'''
    result=cnt.execute(sql,(user,pas))
    row=result.fetchone()
    
    if row:
        return row[0]
    else:
        return False

def validation(user,pas,addr):
    global cnt
    if user=="" or pas=="" or addr=="":
        return False,"fill empty fields"
    if len(pas)<8:
        return False,"password length error"
    
    sql=''' SELECT * FROM users WHERE username=?'''
    result=cnt.execute(sql,(user,))
    row=result.fetchone()
    if row:
        return False,"username already exist!"
    
    return True,""
    
    
def user_submit(user,pas,addr):
    global cnt
    result,errorMSG=validation(user,pas,addr)
    if result:
        sql='''INSERT INTO users (username,pass,addr,grade)
                VALUES(?,?,?,?)'''
        cnt.execute(sql,(user,pas,addr,15))
        cnt.commit()
        return True,""
    else:
        return False,errorMSG
    

def getallusers():
    sql='''SELECT * FROM users'''
    result=cnt.execute(sql)
    rows=result.fetchall()
    return rows    


def user_access(user,grade):
    sql='''UPDATE users SET grade=? WHERE id=?'''    
    cnt.execute(sql,(grade,user))
    cnt.commit()