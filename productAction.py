import sqlite3
cnt=sqlite3.connect('store.db')

def getAllProducts():
    sql='''SELECT * FROM products'''
    result=cnt.execute(sql)
    rows=result.fetchall()
    return rows

def shopValidate(pid,qnt):
    if pid=="" or qnt=="":
        return False,"Fill the inputs"
    
    sql='''SELECT * FROM PRODUCTS WHERE id=?'''
    result=cnt.execute(sql,(pid,))
    rows=result.fetchone()
    if not rows:
        return False,"Wrong product id"
    
    sql='''SELECT * FROM PRODUCTS WHERE id=? AND qnt>=?'''
    result=cnt.execute(sql,(pid,qnt))
    rows=result.fetchone()
    if not rows:
        return False,"not enough quantity"
    
    return True,""

def savetocart(uid,pid,qnt):
    sql=''' INSERT INTO cart(uid,pid,qnt) VALUES(?,?,?)'''
    cnt.execute(sql,(uid,pid,qnt))
    cnt.commit()

def updateqnt(pid,qnt):
    sql=''' UPDATE products SET qnt=qnt-? WHERE id=?'''
    cnt.execute(sql,(qnt,pid))
    cnt.commit()

def getUserCart(uid):
    sql=''' SELECT cart.qnt,products.pname,products.price
            FROM cart INNER JOIN products ON
            cart.pid=products.id
            WHERE cart.uid=?'''
    result=cnt.execute(sql,(uid,))
    rows=result.fetchall()
    return rows

def newproduct(pname,price,qnt):
    sql='''INSERT INTO products(pname,price,qnt) VALUES(?,?,?)'''
    cnt.execute(sql,(pname, price, qnt))
    cnt.commit()
    
def increasequantity(pid,qnt):
    sql=''' UPDATE products SET qnt=qnt+? WHERE id=?'''
    cnt.execute(sql,(qnt,pid))
    cnt.commit()
    
def decreasequantity(pid,qnt):
    sql=''' UPDATE products SET qnt=qnt-? WHERE id=?'''
    cnt.execute(sql,(qnt,pid))
    cnt.commit()