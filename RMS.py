from tkinter import *
import random
import time
import tkinter.messagebox
from tkinter import Menu

root = Tk()
#===========================Menu========================
def about():
    tkinter.messagebox.showinfo("About","This Program is made By Sajjan Karn. This Software is designed For Restaurant Management!")
def how_to_use():
    tkinter.messagebox.showinfo("How To Use?", "Just Fill the items that customer has eaten and click on Total Button and there you GO!")

menubar = Menu(root)
file = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=file)
file.add_command(label="About",command=about)
file.add_command(label="How to use?",command=how_to_use)
file.add_command(label="Exit",command=root.destroy)





txt_Input = StringVar()
operator = ""
#====================== TIME    ===============================
time = time.asctime(time.localtime(time.time()))
#===================== Frames =================================
Tops = Frame(root,width=1600,height=50,bg="powder blue")
Tops.pack(side=TOP)

frame1 = Frame(root,width=800,height=800)
frame1.pack(side=LEFT)

frame2 = Frame(root, width=300,height=800,padx=10)
frame2.pack(side=RIGHT)
#==================== Information Labels =======================

label_title = Label(Tops,bd=10,text="RESTAURANT MANAGEMENT SYSTEM",fg="red",font=('arial',50,'bold'),anchor='w')
label_title.grid(row=0,column=0)

label_time = Label(Tops,bd=5,text=time,font=('arial',50,'bold'),fg="red",anchor='w')
label_time.grid(row=1,column=0)
#============================= Calculatot ==========================

def txtClick(number):
    global operator
    operator = operator + str(number)
    txt_Input.set(operator)

def txtClear():
    global operator
    operator = ""
    txt_Input.set("")

def txtEqual():
    global operator
    calc = str(eval(operator))
    operator = ""
    txt_Input.set(calc)

def set_total():
    billno = random.randint(1280, 50892)
    reference.set(billno)

    COfries = float(fries.get())
    COburger = float(burger.get())
    COpizza = float(pizza.get())
    COroast = float(roast.get())
    COdosa = float(dosa.get())
    CODrinks = float(Drinks.get())
    
    CostOfFries = COfries * 500
    CostOfBurger = COburger * 80
    CostOfpizza = COpizza * 499
    CostOfRoast = COroast * 150
    CostOfDosa = COdosa * 280
    CostOfDrink = CODrinks * 40

    CostOfMeal = "रू",str("%.2f" % (CostOfFries + CostOfBurger + CostOfpizza + CostOfRoast + CostOfDosa + CostOfDrink))
    CostTax = (CostOfFries + CostOfBurger + CostOfpizza + CostOfRoast + CostOfDosa + CostOfDrink) * 0.13
    TotalCost = (CostOfFries + CostOfBurger + CostOfpizza + CostOfRoast + CostOfDosa + CostOfDrink)
    Service_Charge_Cost = (CostOfFries + CostOfBurger + CostOfpizza + CostOfRoast + CostOfDosa + CostOfDrink) / 99
    service = "रू",str("%.2f" % Service_Charge_Cost)
    OverAllCost = "रू",str("%.2f" % (CostTax + TotalCost + Service_Charge_Cost))
    PaidTax = "रू",str("%.2f" % CostTax)

    Cost_Of_Meal.set(CostOfMeal)
    Service_Charge.set(service)
    Tax.set(PaidTax)
    Sub_Total.set(CostOfMeal)
    Total_Charge.set(OverAllCost)
def rootExit():
    root.destroy()

def reset_items():
    reference.set("")
    fries.set("")
    burger.set("")
    pizza.set("")
    roast.set("")
    dosa.set("")

    Drinks.set("")
    Cost_Of_Meal.set("")
    Service_Charge.set("")
    Tax.set("")
    Sub_Total.set("")
    Total_Charge.set("")

txtDisplay = Entry(frame2,textvariable=txt_Input,bd=30,insertwidth=4,font=('sans-serif',20,'bold'),bg="powder blue",justify="right").grid(columnspan=4)

btn7 = Button(frame2,bd=8,font=('sans-serif',20,'bold'),text="7",bg="powder blue",fg="black",width=4,height=2,command=lambda:txtClick("7")).grid(row=2,column=0)
btn8 = Button(frame2,bd=8,font=('sans-serif',20,'bold'),text="8",bg="powder blue",fg="black",width=4,height=2,command=lambda:txtClick("8")).grid(row=2,column=1)
btn9 = Button(frame2,bd=8,font=('sans-serif',20,'bold'),text="9",bg="powder blue",fg="black",width=4,height=2,command=lambda:txtClick("9")).grid(row=2,column=2)
btnadd = Button(frame2,bd=8,font=('sans-serif',20,'bold'),text="+",bg="powder blue",fg="black",width=4,height=2,command=lambda:txtClick("+")).grid(row=2,column=3)

btn6 = Button(frame2,bd=8,font=('sans-serif',20,'bold'),text="6",bg="powder blue",fg="black",width=4,height=2,command=lambda:txtClick("6")).grid(row=3,column=0)
btn5 = Button(frame2,bd=8,font=('sans-serif',20,'bold'),text="5",bg="powder blue",fg="black",width=4,height=2,command=lambda:txtClick("5")).grid(row=3,column=1)
btn4 = Button(frame2,bd=8,font=('sans-serif',20,'bold'),text="4",bg="powder blue",fg="black",width=4,height=2,command=lambda:txtClick("4")).grid(row=3,column=2)
btnsub = Button(frame2,bd=8,font=('sans-serif',20,'bold'),text="-",bg="powder blue",fg="black",width=4,height=2,command=lambda:txtClick("-")).grid(row=3,column=3)

btn3 = Button(frame2,bd=8,font=('sans-serif',20,'bold'),text="3",bg="powder blue",fg="black",width=4,height=2,command=lambda:txtClick("3")).grid(row=4,column=0)
btn2 = Button(frame2,bd=8,font=('sans-serif',20,'bold'),text="2",bg="powder blue",fg="black",width=4,height=2,command=lambda:txtClick("2")).grid(row=4,column=1)
btn1 = Button(frame2,bd=8,font=('sans-serif',20,'bold'),text="1",bg="powder blue",fg="black",width=4,height=2,command=lambda:txtClick("1")).grid(row=4,column=2)
btnmul = Button(frame2,bd=8,font=('sans-serif',20,'bold'),text="*",bg="powder blue",fg="black",width=4,height=2,command=lambda:txtClick("*")).grid(row=4,column=3)

btnC = Button(frame2,bd=8,font=('sans-serif',20,'bold'),text="C",bg="powder blue",fg="black",width=4,height=2,command=txtClear).grid(row=5,column=0)
btn0 = Button(frame2,bd=8,font=('sans-serif',20,'bold'),text="0",bg="powder blue",fg="black",width=4,height=2,command=lambda:txtClick("0")).grid(row=5,column=1)
btndiv = Button(frame2,bd=8,font=('sans-serif',20,'bold'),text="/",bg="powder blue",fg="black",width=4,height=2,command=lambda:txtClick("/")).grid(row=5,column=2)
btnequal = Button(frame2,bd=8,font=('sans-serif',20,'bold'),text="=",bg="powder blue",fg="black",width=4,height=2,command=txtEqual).grid(row=5,column=3)


#======================================== Dish Items 111111 ===========================================
#===========variables========
reference = StringVar()
fries = StringVar()
burger = StringVar()
pizza = StringVar()
roast = StringVar()
dosa = StringVar()


#==================reference====================
lblref = Label(frame1,text="Reference",
                font=('sans-serif',16,'bold'),bd=16,fg="Steel Blue",anchor='w')
lblref.grid(row=0,column=0)

txtref = Entry(frame1,insertwidth=4,textvariable=reference,
                font=('sans-seif',16,'bold'),bd=10,bg="powder blue",justify='right')
txtref.grid(row=0,column=1)

#========================fries====================
lblfries = Label(frame1,text="  French Fries   ",
                font=('sans-serif',16,'bold'),bd=16,fg="Steel Blue",anchor='w')
lblfries.grid(row=1,column=0)

txtfries = Entry(frame1,insertwidth=4,textvariable=fries,
                font=('sans-seif',16,'bold'),bd=10,bg="powder blue",justify='right')
txtfries.grid(row=1,column=1)
#======================burger============================
lblburg = Label(frame1,text="Veg Burger",
                font=('sans-serif',16,'bold'),bd=16,fg="Steel Blue",anchor='w')
lblburg.grid(row=2,column=0)

txtburg = Entry(frame1,insertwidth=4,textvariable=burger,
                font=('sans-seif',16,'bold'),bd=10,bg="powder blue",justify='right')
txtburg.grid(row=2,column=1)
#====================pizza==========================
lblpiz = Label(frame1,text="Chicken Pizza",
                font=('sans-serif',16,'bold'),bd=16,fg="Steel Blue",anchor='w')
lblpiz.grid(row=3,column=0)
txtpiz = Entry(frame1,insertwidth=4,textvariable=pizza,
                font=('sans-seif',16,'bold'),bd=10,bg="powder blue",justify='right')
txtpiz.grid(row=3,column=1)
#========================= Roast =====================
lblroast = Label(frame1,text="Roast",
                font=('sans-serif',16,'bold'),bd=16,fg="Steel Blue",anchor='w')
lblroast.grid(row=4,column=0)

txtroast = Entry(frame1,insertwidth=4,textvariable=roast,
                font=('sans-seif',16,'bold'),bd=10,bg="powder blue",justify='right')
txtroast.grid(row=4,column=1)
#==================== Dosa ============================
lbldosa = Label(frame1,text="Dosa",
                font=('sans-serif',16,'bold'),bd=16,fg="Steel Blue",anchor='w')
lbldosa.grid(row=5,column=0)

txtdosa = Entry(frame1,insertwidth=4,textvariable=dosa,
                font=('sans-seif',16,'bold'),bd=10,bg="powder blue",justify='right')
txtdosa.grid(row=5,column=1)









#======================================== Dish Items 22222222222222222222 ===========================================
#===========variables========
Drinks = StringVar()
Cost_Of_Meal = StringVar()
Service_Charge = StringVar()
Tax = StringVar()
Sub_Total = StringVar()
Total_Charge= StringVar()


#==================drinks====================
lbldrinks = Label(frame1,text="Drinks",
                font=('sans-serif',16,'bold'),bd=16,fg="Steel Blue",anchor='w')
lbldrinks.grid(row=0,column=2)

txtdrinks = Entry(frame1,insertwidth=4,textvariable=Drinks,
                font=('sans-seif',16,'bold'),bd=10,justify='right')
txtdrinks.grid(row=0,column=3)

#========================Cost of MEal====================
lblCostOfMeal = Label(frame1,text="Cost Of Meal",
                font=('sans-serif',16,'bold'),bd=16,fg="Steel Blue",anchor='w')
lblCostOfMeal.grid(row=1,column=2)

txtCostOfMeal = Entry(frame1,insertwidth=4,textvariable=Cost_Of_Meal,
                font=('sans-seif',16,'bold'),bd=10,justify='right')
txtCostOfMeal.grid(row=1,column=3)
#======================Service Charge============================
lblServiceCharge = Label(frame1,text="Service Charge",
                font=('sans-serif',16,'bold'),bd=16,fg="Steel Blue",anchor='w')
lblServiceCharge.grid(row=2,column=2)

txtServiceCharge = Entry(frame1,insertwidth=4,textvariable=Service_Charge,
                font=('sans-seif',16,'bold'),bd=10,justify='right')
txtServiceCharge.grid(row=2,column=3)
#====================tax==========================
lblTax = Label(frame1,text="Tax",
                font=('sans-serif',16,'bold'),bd=16,fg="Steel Blue",anchor='w')
lblTax.grid(row=3,column=2)
txtTax = Entry(frame1,insertwidth=4,textvariable=Tax,
                font=('sans-seif',16,'bold'),bd=10,justify='right')
txtTax.grid(row=3,column=3)
#========================= Sub total =====================
lblSubTotal = Label(frame1,text="Sub Total",
                font=('sans-serif',16,'bold'),bd=16,fg="Steel Blue",anchor='w')
lblSubTotal.grid(row=4,column=2)

txtSubTotal = Entry(frame1,insertwidth=4,textvariable=Sub_Total,
                font=('sans-seif',16,'bold'),bd=10,justify='right')
txtSubTotal.grid(row=4,column=3)
#==================== total Charge ============================
lblTotalCharge = Label(frame1,text="Total",
                font=('sans-serif',16,'bold'),bd=16,fg="Steel Blue",anchor='w')
lblTotalCharge.grid(row=5,column=2)

txtTotalCharge = Entry(frame1,insertwidth=4,textvariable=Total_Charge,
                font=('sans-seif',16,'bold'),bd=10,justify='right')
txtTotalCharge.grid(row=5,column=3)


#============================= Buttons ==========================================
btnTotal = Button(frame1,text="Total",font=('arial',16,'bold'),bd=16,fg="black",bg="powder blue",padx=16,pady=8,width=8,command=set_total)
btnTotal.grid(row=7,column=1)

btnrst = Button(frame1,text="Reset",font=('arial',16,'bold'),bd=16,fg="black",bg="powder blue",padx=16,pady=8,width=8,command=reset_items)
btnrst.grid(row=7,column=2)

btnExit = Button(frame1,text="Exit",font=('arial',16,'bold'),bd=16,fg="black",bg="powder blue",padx=16,pady=8,width=8,command=rootExit)
btnExit.grid(row=7,column=3)



#======================rooooooootttttttttt==========================
root.title("Restaurant Management System")
root.config(menu=menubar)
root.geometry("1600x800+0+0")
root.mainloop()