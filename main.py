import tkinter
import userAction
import productAction
from tkinter import messagebox

def login():
    global session
    user=txt_user.get()
    pas=txt_pass.get()
    result=userAction.user_login(user, pas)
    if user=="admin" and pas=="123456789":
        messagebox.showinfo("accessed to admin panel!")
        txt_user.delete(0,"end")
        txt_pass.delete(0,"end")
        btn_login.configure(state="disabled")
        btn_admin_panel.configure(state="active")
        btn_logout.configure(state="active")
        btn_shop.configure(state="active")
        btn_cart.configure(state="active")
   
    elif result:
        lbl_msg.configure(text="welcome to your account!",fg="green")
        session=result
        txt_user.delete(0,"end")
        txt_pass.delete(0,"end")
        btn_login.configure(state="disabled")
        btn_logout.configure(state="active")
        btn_shop.configure(state="active")
        btn_cart.configure(state="active")
           
    else:
        lbl_msg.configure(text="wrong username or pass!",fg="red")
        
    
def submit():
    def register():
        user=txt_user.get()
        pas=txt_pass.get()
        addr=txt_addr.get()
        result,errorMSG=userAction.user_submit(user, pas, addr)
        if result:
            lbl_msg.configure(text="submit done",fg="green")
            txt_user.delete(0,"end")
            txt_pass.delete(0,"end")
            txt_addr.delete(0,"end")
            btn_submit.configure(state="disabled")
        else:
            lbl_msg.configure(text=errorMSG,fg="red")
        
    win_submit=tkinter.Toplevel()  
    win_submit.title("Submit panel")
    win_submit.geometry("500x400")
    
    lbl_user=tkinter.Label(win_submit,text="Username: ")
    lbl_user.pack()
    txt_user=tkinter.Entry(win_submit)
    txt_user.pack()

    lbl_pass=tkinter.Label(win_submit,text="Password: ")
    lbl_pass.pack()
    txt_pass=tkinter.Entry(win_submit)
    txt_pass.pack()
    
    lbl_addr=tkinter.Label(win_submit,text="Address: ")
    lbl_addr.pack()
    txt_addr=tkinter.Entry(win_submit)
    txt_addr.pack()
    
    lbl_msg=tkinter.Label(win_submit,text="")
    lbl_msg.pack()
    
    btn_submit=tkinter.Button(win_submit,text="Submit",command=register)
    btn_submit.pack()
    
    
    win_submit.mainloop()


def logout():
    global session
    session=False
    btn_login.configure(state="active")
    btn_logout.configure(state="disabled")
    btn_shop.configure(state="disabled")
    btn_cart.configure(state="disabled")
    btn_admin_panel.configure(state="disabled")
    lbl_msg.configure(text="you are logged out now!",fg="green")


def shop():
    def buy():
        global session
        pid=txt_id.get()
        qnt=txt_qnt.get()
        result,msg=productAction.shopValidate(pid, qnt)
        if not result:
            lbl_msg.configure(text=msg,fg="red")
            return
        productAction.savetocart(session,pid,qnt)
        productAction.updateqnt(pid,qnt)
        lstbx.delete(0,"end")
        products=productAction.getAllProducts()
        for product in products:
            text=f"id:{product[0]},   Name:{product[1]},   Price:{product[2]},   Quantity:{product[3]}"
            lstbx.insert("end", text)
        
        lbl_msg.configure(text="saved to your cart",fg="green")
        txt_id.delete(0,"end")
        txt_qnt.delete(0,"end")
        
    win_shop=tkinter.Toplevel(win)
    win_shop.title("shop panel")
    win_shop.geometry("500x400")
    
    products=productAction.getAllProducts()
    
    lstbx=tkinter.Listbox(win_shop,width=60)
    lstbx.pack()
    
    for product in products:
        text=f"id:{product[0]},   Name:{product[1]},   Price:{product[2]},   Quantity:{product[3]}"
        lstbx.insert("end", text)
    
    lbl_id=tkinter.Label(win_shop,text="Product id:")
    lbl_id.pack()
    
    txt_id=tkinter.Entry(win_shop)
    txt_id.pack()
    
    lbl_qnt=tkinter.Label(win_shop,text="quantity:")
    lbl_qnt.pack()
    
    txt_qnt=tkinter.Entry(win_shop)
    txt_qnt.pack()
    
    lbl_msg=tkinter.Label(win_shop,text="")
    lbl_msg.pack()
    
    btn_buy=tkinter.Button(win_shop,text="Buy",command=buy)
    btn_buy.pack()
    
    
    win_shop.mainloop()
    

def mycart():
    global session
    
    win_cart=tkinter.Toplevel(win)
    win_cart.title("cart panel")
    win_cart.geometry("500x400")
    
    lstbx=tkinter.Listbox(win_cart,width=60)
    lstbx.pack()
    
    result=productAction.getUserCart(session)
    for product in result:
        text=f"Name:{product[1]},   Quantity:{product[0]},   Total Price:{product[0]*product[2]}"
        lstbx.insert("end", text)
    
    
    win_cart.mainloop()
    

def admin_panel():
    
    def add_product():
        def add():
            pname=txt_pname.get()
            price=txt_price.get()
            qnt=txt_qnt.get()
            productAction.newproduct(pname,price,qnt)
            lstbx.delete(0,"end")
            products=productAction.getAllProducts()
            for product in products:
                text=f"id:{product[0]},   Name:{product[1]},   Price:{product[2]},   Quantity:{product[3]}"
                lstbx.insert("end", text)
                
            lbl_msg.configure(text="add product done",fg="green")
            txt_pname.delete(0,"end")
            txt_price.delete(0,"end")
            txt_qnt.delete(0,"end")
            
        win_add_product=tkinter.Toplevel(win)
        win_add_product.title("add product")
        win_add_product.geometry("600x500")
        
        products=productAction.getAllProducts()
        
        lstbx=tkinter.Listbox(win_add_product,width=60)
        lstbx.pack()
        
        for product in products:
            text=f"id:{product[0]},   Name:{product[1]},   Price:{product[2]},   Quantity:{product[3]}"
            lstbx.insert("end", text)
        
        lbl_pname=tkinter.Label(win_add_product,text="Product name:")
        lbl_pname.pack()
        txt_pname=tkinter.Entry(win_add_product)
        txt_pname.pack()
        
        lbl_price=tkinter.Label(win_add_product,text="product price:")
        lbl_price.pack()
        txt_price=tkinter.Entry(win_add_product)
        txt_price.pack()
        
        lbl_qnt=tkinter.Label(win_add_product,text="product quantity:")
        lbl_qnt.pack()
        txt_qnt=tkinter.Entry(win_add_product)
        txt_qnt.pack()
        
        lbl_msg=tkinter.Label(win_add_product,text="")
        lbl_msg.pack()
        
        btn_add=tkinter.Button(win_add_product,text="add",command=add)
        btn_add.pack()
        
        
        win_add_product.mainloop()
        
        
    def change_inventory():
        
        def increase():
            pid=txt_pid.get()
            qnt=txt_qnt.get()
            productAction.increasequantity(pid,qnt)
            lstbx.delete(0,"end")
            products=productAction.getAllProducts()
            for product in products:
                text=f"id:{product[0]},   Name:{product[1]},   Price:{product[2]},   Quantity:{product[3]}"
                lstbx.insert("end", text)
                
            lbl_msg.configure(text="increase product done",fg="green")
            txt_pid.delete(0,"end")
            txt_qnt.delete(0,"end")
            
        def decrease():
            pid=txt_pid.get()
            qnt=txt_qnt.get()
            productAction.decreasequantity(pid,qnt)
            lstbx.delete(0,"end")
            products=productAction.getAllProducts()
            for product in products:
                text=f"id:{product[0]},   Name:{product[1]},   Price:{product[2]},   Quantity:{product[3]}"
                lstbx.insert("end", text)
                
            lbl_msg.configure(text="decrease product done",fg="green")
            txt_pid.delete(0,"end")
            txt_qnt.delete(0,"end")
            
            
        win_change_inventory=tkinter.Toplevel(win)
        win_change_inventory.title("change inventory")
        win_change_inventory.geometry("600x500")
        
        products=productAction.getAllProducts()
        
        lstbx=tkinter.Listbox(win_change_inventory,width=60)
        lstbx.pack()
        
        for product in products:
            text=f"id:{product[0]},   Name:{product[1]},   Price:{product[2]},   Quantity:{product[3]}"
            lstbx.insert("end", text)
        
        lbl_pid=tkinter.Label(win_change_inventory,text="Product id:")
        lbl_pid.pack()
        txt_pid=tkinter.Entry(win_change_inventory)
        txt_pid.pack()
        
        
        lbl_qnt=tkinter.Label(win_change_inventory,text="product quantity:")
        lbl_qnt.pack()
        txt_qnt=tkinter.Entry(win_change_inventory)
        txt_qnt.pack()
        
        lbl_msg=tkinter.Label(win_change_inventory,text="")
        lbl_msg.pack()
        
        btn_increase=tkinter.Button(win_change_inventory,text="increase",command=increase)
        btn_increase.pack()
        
        btn_decrease=tkinter.Button(win_change_inventory,text="decrease",command=decrease)
        btn_decrease.pack()
       
        
        win_change_inventory.mainloop()
        
       
    def access_level():
        
        def determine_access():
            user=txt_user.get()
            grade=txt_grade.get()
            userAction.user_access(user,grade)
            lstbx.delete(0,"end")
            users=userAction.getallusers()
            for user in users:
                text=f"id:{user[0]},   username:{user[1]},   grade:{user[4]}"
                lstbx.insert("end", text)
                
            lbl_msg.configure(text="change done",fg="green")
            txt_user.delete(0,"end")
            txt_grade.delete(0,"end")
                
        win_access_level=tkinter.Toplevel(win)
        win_access_level.title("access level")
        win_access_level.geometry("600x500")
        
        users=userAction.getallusers()
        
        lstbx=tkinter.Listbox(win_access_level,width=60)
        lstbx.pack()
        
        for user in users:
            text=f"id:{user[0]},   username:{user[1]},   grade:{user[4]}"
            lstbx.insert("end", text)
           
        lbl_user=tkinter.Label(win_access_level,text="id: ")
        lbl_user.pack()
        txt_user=tkinter.Entry(win_access_level)
        txt_user.pack()

        
        lbl_grade=tkinter.Label(win_access_level,text="grade: ")
        lbl_grade.pack()
        txt_grade=tkinter.Entry(win_access_level)
        txt_grade.pack()
        
        
        lbl_msg=tkinter.Label(win_access_level,text="")
        lbl_msg.pack()
        
        btn_access_level=tkinter.Button(win_access_level,text="determine access",command=determine_access)
        btn_access_level.pack()
        
        
        win_access_level.mainloop()
    
    
    win_admin_panel=tkinter.Toplevel(win)
    win_admin_panel.title("admin panel")
    win_admin_panel.geometry("500x400")

    
    btn_add_product=tkinter.Button(win_admin_panel, text="add new product", command=add_product)
    btn_add_product.pack()

    btn_change_inventory=tkinter.Button(win_admin_panel, text="change in product inventory", command=change_inventory)
    btn_change_inventory.pack()

    btn_access_level=tkinter.Button(win_admin_panel, text="user access level", command=access_level)
    btn_access_level.pack()
    
    
    win_admin_panel.mainloop()

# ------------------ Main ---------------------------
session=False

win=tkinter.Tk()
win.title("SHOP PROJECT")
win.geometry("500x400")

lbl_user=tkinter.Label(win,text="Username: ")
lbl_user.pack()
txt_user=tkinter.Entry(win)
txt_user.pack()

lbl_pass=tkinter.Label(win,text="Password: ")
lbl_pass.pack()
txt_pass=tkinter.Entry(win)
txt_pass.pack()

lbl_msg=tkinter.Label(win,text="")
lbl_msg.pack()

btn_login=tkinter.Button(win,text="Login",command=login)
btn_login.pack()

btn_submit=tkinter.Button(win,text="Submit",command=submit)
btn_submit.pack()

btn_logout=tkinter.Button(win,text="Logout",state="disabled", command=logout)
btn_logout.pack()

btn_shop=tkinter.Button(win,text="Shop",state="disabled", command=shop)
btn_shop.pack()

btn_cart=tkinter.Button(win,text="my cart",state="disabled", command=mycart)
btn_cart.pack()

btn_admin_panel=tkinter.Button(win,text="admin panel",state="disabled" , command=admin_panel)
btn_admin_panel.pack()


win.mainloop()