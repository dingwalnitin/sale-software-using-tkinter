from tkinter import *
from PIL import Image,ImageTk


Gvar1=""
Gvar2=""
Gvar3=[]


from tkinter import *
from PIL import Image,ImageTk

Mdict={}


def thank():

    root3 = Tk()
    root3.title("Store")
    root3.geometry("700x700")
    label1 = Label(root3, text="VIT Store", font=("Arial", 25)).place(x=350, y=0)
    img1 = (Image.open("1.png"))
    resized_image = img1.resize((80, 80), Image.ANTIALIAS)
    image1 = ImageTk.PhotoImage(resized_image)
    label2 = Label(root3, image=image1).place(x=270, y=0)
    xc = "Thanks for Shopping With Us"
    Label(root3, text=xc, font=("Arial", 25)).place(x=100, y=100)
def buy_now(item,price):
    def thanks():
        root2.destroy()
        thank()


    root2= Tk()
    root2.title("Store")
    root2.geometry("700x700")
    label1= Label(root2,text="VIT Store",font=("Arial", 25)).place(x=350,y=0)
    img1=(Image.open("1.png"))
    resized_image= img1.resize((80,80), Image.ANTIALIAS)
    image1= ImageTk.PhotoImage(resized_image)
    label2= Label(root2,image=image1).place(x=270,y=0)
    xc=f"You Bought {item} worth: {price}"
    Label(root2, text=xc, font=("Arial", 15)).place(x=100,y=100)
    Button(root2,text="Complete Purchase", command=thanks).place(x=100,y=150)


    root2.mainloop()

def Cartc(a):
    def thanks():
        root3.destroy()
        thank()
    root3 = Tk()
    root3.title("Cart")

    root3.geometry("960x1080")



    Label(root3, text="VIT Store", font=("Arial", 25)).place(x=350, y=0)
    img55 = (Image.open("1.png"))
    resized_image = img55.resize((80, 80), Image.ANTIALIAS)
    image55 = ImageTk.PhotoImage(resized_image)
    Label(root3, image=image55).place(x=270, y=0)
    Label(root3,text="The Items in Your Cart are",font=("Arial", 20)).place(x=320, y=100)
    tot=0
    for i in range(len(a)):
        res = list(Mdict.keys())[i]
        red=list(Mdict.values())[i]
        if res==1:
            res="Basmati chawal,बासमती चावल"
            rem = 900 * int(red)
            if (int(red))>4:
                Label(root3,text="You have been given a 5% discount",font=("Arial", 13)).place(x=100,y=250*(i+1))
                rem=rem-(rem/20)

            tot=tot+rem
        elif res==2:
            res="Kissan फ्रेश टोमेटो केचप"
            rem=120*int(red)
            if (int(red))>4:
                Label(root3,text="You have been given a 5% discount",font=("Arial", 13)).place(x=100,y=250*(i+1))
                rem=rem-(rem/20)
            tot=tot+rem
        ma=F"{res}      {red}pcs   {rem}"
        Label(root3,text=ma,font=("Arial", 13)).place(x=100,y=200*(i+1))
    Label(root3,text=f" Total:{tot}",font=("Arial", 23)).place(x=100,y=700)
    Button(root3,text="Complete Purchase",font=("Arial", 13),command=thanks).place(x=500,y=700)
    root3.mainloop()
def getfn1():

    def add1():
        z=Label(root1, text="added!",font=("Arial", 15)).place(x=700,y=380)
        a=cartval1.get()
        Mdict[1]=a

    def add2():


        z=Label(root1, text="added!", font=("Arial", 15)).place(x=700, y=700)
        a = cartval1.get()
        Mdict[2] = a

    def G2C():
        root1.destroy()
        Cartc(Mdict)
    def bu2():
        root1.destroy()
        buy_now("Kisan Tomato Sauce", "₹120")

    def bu1():
        root1.destroy()
        buy_now("DAAWAT brown rice", "₹900")




    root1 = Tk()
    root1.title("Store")

    root1.geometry("960x1080")
    scroll = Scrollbar(root1, orient=VERTICAL)
    cartval1 = StringVar()
    cartval2 = StringVar()
    scroll.pack(side=RIGHT, fill=Y)
    Button(root1, text="Go to Cart",font=("Arial bold", 13),command=G2C).place(x=850,y=0)
    Label(root1, text="VIT Store", font=("Arial", 25)).place(x=350, y=0)
    img1 = (Image.open("1.png"))
    resized_image = img1.resize((80, 80), Image.ANTIALIAS)
    image1 = ImageTk.PhotoImage(resized_image)
    Label(root1, image=image1).place(x=270, y=0)

    img2 = (Image.open("2.jpg"))
    resized_image = img2.resize((200, 300), Image.ANTIALIAS)
    image2 = ImageTk.PhotoImage(resized_image)
    Label(root1, text="1)", font=("Arial", 13)).place(x=0, y=130)
    Label(root1, image=image2).place(x=20, y=130)
    Label(root1, text="Daawat Brown, Cooks in 15-minute, Full Bran Intact,\n Fibre-Rich Basmati Rice, 5 Kg",
          font=("Arial", 17)).place(x=230, y=120)
    Label(root1,
          text="-Zero cholesterol: Good for your heart and cardio vascular functioning\n Whole grain (Lower carbohydrates): Helps in overall health",
          font=("Arial", 13)).place(x=230, y=180)
    Label(root1, text="-Country of Origin: India", font=("Arial", 13)).place(x=230, y=230)
    Label(root1, text="-Lower GI: Diabetic friendly", font=("Arial", 13)).place(x=230, y=280)
    Label(root1, text="-HET processed and enriched with vitamins and minerals: For stronger immunity",
          font=("Arial", 13)).place(x=230, y=330)
    Button(root1, text="Buy Now", font=("Arial bold", 13), command=bu1).place(x=280, y=380)
    Button(root1, text="Add To Cart", font=("Arial bold", 13),command=add1).place(x=380, y=380)
    Spinbox(root1,from_= 0, to = 20, textvariable=cartval1).place(x=530,y=390)


    img3 = (Image.open("3.jpg"))
    resized_image = img3.resize((200, 300), Image.ANTIALIAS)
    image3 = ImageTk.PhotoImage(resized_image)
    Label(root1, text="1)", font=("Arial", 13)).place(x=0, y=450)
    Label(root1, image=image3).place(x=20, y=450)
    Label(root1, text="Kissan Fresh Tomato Ketchup 950 g Pouch, \nSweet & Tangy Sauce made from 100% Real Tomatoes",
          font=("Arial", 17)).place(x=230, y=440)
    Label(root1,text="-Is easy to pour and use and can be enjoyed with every snack",font=("Arial", 13)).place(x=230, y=500)
    Label(root1, text="-Enjoy it best with samosas, pakodas, noodles or Roti roll for an interesting tiffin meal", font=("Arial", 13)).place(x=230, y=560)
    Label(root1, text="-Lower GI: Diabetic friendly", font=("Arial", 13)).place(x=230, y=600)
    Label(root1, text="-Carefully sealed in impermeable glass packaging to retain the best flavour and taste of product",
          font=("Arial", 13)).place(x=230, y=650)
    Button(root1, text="Buy Now", font=("Arial bold", 13), command=bu2).place(x=280, y=700)
    Button(root1, text="Add To Cart", font=("Arial bold", 13),command=add2).place(x=380, y=700)
    Spinbox(root1, from_=0, to=20, textvariable=cartval2).place(x=530, y=710)


    img4 = (Image.open("2.jpg"))
    resized_image = img4.resize((200, 300), Image.ANTIALIAS)
    image4 = ImageTk.PhotoImage(resized_image)
    Label(root1, text="1)", font=("Arial", 13)).place(x=0, y=770)
    Label(root1, image=image2).place(x=20, y=770)
    Label(root1, text="Daawat Brown, Cooks in 15-minute, Full Bran Intact,\n Fibre-Rich Basmati Rice, 5 Kg",
          font=("Arial", 17)).place(x=230, y=760)
    Label(root1,
          text="-Zero cholesterol: Good for your heart and cardio vascular functioning\n Whole grain (Lower carbohydrates): Helps in overall health",
          font=("Arial", 13)).place(x=230, y=820)
    Label(root1, text="-Country of Origin: India", font=("Arial", 13)).place(x=230, y=880)
    Label(root1, text="-Lower GI: Diabetic friendly", font=("Arial", 13)).place(x=230, y=920)
    Label(root1, text="-HET processed and enriched with vitamins and minerals: For stronger immunity",
          font=("Arial", 13)).place(x=230, y=970)
    Button(root1, text="Buy Now", font=("Arial bold", 13)).place(x=280, y=1020)
    Button(root1, text="Add To Cart", font=("Arial bold", 13)).place(x=380, y=1020)

    img5 = (Image.open("2.jpg"))
    resized_image = img5.resize((200, 300), Image.ANTIALIAS)
    image5 = ImageTk.PhotoImage(resized_image)
    Label(root1, text="1)", font=("Arial", 13)).place(x=0, y=1090)
    Label(root1, image=image2).place(x=20, y=1090)
    Label(root1, text="Daawat Brown, Cooks in 15-minute, Full Bran Intact,\n Fibre-Rich Basmati Rice, 5 Kg",
          font=("Arial", 17)).place(x=230, y=1080)
    Label(root1,
          text="-Zero cholesterol: Good for your heart and cardio vascular functioning\n Whole grain (Lower carbohydrates): Helps in overall health",
          font=("Arial", 13)).place(x=230, y=1140)
    Label(root1, text="-Country of Origin: India", font=("Arial", 13)).place(x=230, y=1200)
    Label(root1, text="-Lower GI: Diabetic friendly", font=("Arial", 13)).place(x=230, y=1240)
    Label(root1, text="-HET processed and enriched with vitamins and minerals: For stronger immunity",
          font=("Arial", 13)).place(x=230, y=1290)
    Button(root1, text="Buy Now", font=("Arial bold", 13)).place(x=280, y=1340)
    Button(root1, text="Add To Cart", font=("Arial bold", 13)).place(x=380, y=1340)

    img6 = (Image.open("2.jpg"))
    resized_image = img6.resize((200, 300), Image.ANTIALIAS)
    image6 = ImageTk.PhotoImage(resized_image)
    Label(root1, text="1)", font=("Arial", 13)).place(x=0, y=1410)
    Label(root1, image=image2).place(x=20, y=1410)
    Label(root1, text="Daawat Brown, Cooks in 15-minute, Full Bran Intact,\n Fibre-Rich Basmati Rice, 5 Kg",
          font=("Arial", 17)).place(x=230, y=1400)
    Label(root1,
          text="-Zero cholesterol: Good for your heart and cardio vascular functioning\n Whole grain (Lower carbohydrates): Helps in overall health",
          font=("Arial", 13)).place(x=230, y=1460)
    Label(root1, text="-Country of Origin: India", font=("Arial", 13)).place(x=230, y=1520)
    Label(root1, text="-Lower GI: Diabetic friendly", font=("Arial", 13)).place(x=230, y=1560)
    Label(root1, text="-HET processed and enriched with vitamins and minerals: For stronger immunity",
          font=("Arial", 13)).place(x=230, y=1610)
    Button(root1, text="Buy Now", font=("Arial bold", 13)).place(x=280, y=1660)
    Button(root1, text="Add To Cart", font=("Arial bold", 13)).place(x=380, y=1660)

    img7 = (Image.open("2.jpg"))
    resized_image = img7.resize((200, 300), Image.ANTIALIAS)
    image7 = ImageTk.PhotoImage(resized_image)
    Label(root1, text="1)", font=("Arial", 13)).place(x=0, y=1730)
    Label(root1, image=image2).place(x=20, y=1730)
    Label(root1, text="Daawat Brown, Cooks in 15-minute, Full Bran Intact,\n Fibre-Rich Basmati Rice, 5 Kg",
          font=("Arial", 17)).place(x=230, y=1720)
    Label(root1,
          text="-Zero cholesterol: Good for your heart and cardio vascular functioning\n Whole grain (Lower carbohydrates): Helps in overall health",
          font=("Arial", 13)).place(x=230, y=1780)
    Label(root1, text="-Country of Origin: India", font=("Arial", 13)).place(x=230, y=1840)
    Label(root1, text="-Lower GI: Diabetic friendly", font=("Arial", 13)).place(x=230, y=1880)
    Label(root1, text="-HET processed and enriched with vitamins and minerals: For stronger immunity",
          font=("Arial", 13)).place(x=230, y=1930)
    Button(root1, text="Buy Now", font=("Arial bold", 13)).place(x=280, y=1980)
    Button(root1, text="Add To Cart", font=("Arial bold", 13)).place(x=380, y=1980)

    img8 = (Image.open("2.jpg"))
    resized_image = img8.resize((200, 300), Image.ANTIALIAS)
    image8 = ImageTk.PhotoImage(resized_image)
    Label(root1, text="1)", font=("Arial", 13)).place(x=0, y=2050)
    Label(root1, image=image2).place(x=20, y=2050)
    Label(root1, text="Daawat Brown, Cooks in 15-minute, Full Bran Intact,\n Fibre-Rich Basmati Rice, 5 Kg",
          font=("Arial", 17)).place(x=230, y=2040)
    Label(root1,
          text="-Zero cholesterol: Good for your heart and cardio vascular functioning\n Whole grain (Lower carbohydrates): Helps in overall health",
          font=("Arial", 13)).place(x=230, y=2100)
    Label(root1, text="-Country of Origin: India", font=("Arial", 13)).place(x=230, y=2160)
    Label(root1, text="-Lower GI: Diabetic friendly", font=("Arial", 13)).place(x=230, y=2200)
    Label(root1, text="-HET processed and enriched with vitamins and minerals: For stronger immunity",
          font=("Arial", 13)).place(x=230, y=2250)
    Button(root1, text="Buy Now", font=("Arial bold", 13)).place(x=280, y=2300)
    Button(root1, text="Add To Cart", font=("Arial bold", 13)).place(x=380, y=2300)

    img9 = (Image.open("2.jpg"))
    resized_image = img9.resize((200, 300), Image.ANTIALIAS)
    image9 = ImageTk.PhotoImage(resized_image)
    Label(root1, text="1)", font=("Arial", 13)).place(x=0, y=2370)
    Label(root1, image=image2).place(x=20, y=2370)
    Label(root1, text="Daawat Brown, Cooks in 15-minute, Full Bran Intact,\n Fibre-Rich Basmati Rice, 5 Kg",
          font=("Arial", 17)).place(x=230, y=2360)
    Label(root1,
          text="-Zero cholesterol: Good for your heart and cardio vascular functioning\n Whole grain (Lower carbohydrates): Helps in overall health",
          font=("Arial", 13)).place(x=230, y=2420)
    Label(root1, text="-Country of Origin: India", font=("Arial", 13)).place(x=230, y=2480)
    Label(root1, text="-Lower GI: Diabetic friendly", font=("Arial", 13)).place(x=230, y=2520)
    Label(root1, text="-HET processed and enriched with vitamins and minerals: For stronger immunity",
          font=("Arial", 13)).place(x=230, y=2570)
    Button(root1, text="Buy Now", font=("Arial bold", 13)).place(x=280, y=2620)
    Button(root1, text="Add To Cart", font=("Arial bold", 13)).place(x=380, y=2620)

    img10 = (Image.open("2.jpg"))
    resized_image = img10.resize((200, 300), Image.ANTIALIAS)
    image10 = ImageTk.PhotoImage(resized_image)
    Label(root1, text="1)", font=("Arial", 13)).place(x=0, y=2690)
    Label(root1, image=image2).place(x=20, y=2690)
    Label(root1, text="Daawat Brown, Cooks in 15-minute, Full Bran Intact,\n Fibre-Rich Basmati Rice, 5 Kg",
          font=("Arial", 17)).place(x=230, y=2680)
    Label(root1,
          text="-Zero cholesterol: Good for your heart and cardio vascular functioning\n Whole grain (Lower carbohydrates): Helps in overall health",
          font=("Arial", 13)).place(x=230, y=2740)
    Label(root1, text="-Country of Origin: India", font=("Arial", 13)).place(x=230, y=2800)
    Label(root1, text="-Lower GI: Diabetic friendly", font=("Arial", 13)).place(x=230, y=2840)
    Label(root1, text="-HET processed and enriched with vitamins and minerals: For stronger immunity",
          font=("Arial", 13)).place(x=230, y=2890)
    Button(root1, text="Buy Now", font=("Arial bold", 13)).place(x=280, y=2940)
    Button(root1, text="Add To Cart", font=("Arial bold", 13)).place(x=380, y=2940)

    img11 = (Image.open("2.jpg"))
    resized_image = img11.resize((200, 300), Image.ANTIALIAS)
    image11 = ImageTk.PhotoImage(resized_image)
    Label(root1, text="1)", font=("Arial", 13)).place(x=0, y=3010)
    Label(root1, image=image2).place(x=20, y=3010)
    Label(root1, text="Daawat Brown, Cooks in 15-minute, Full Bran Intact,\n Fibre-Rich Basmati Rice, 5 Kg",
          font=("Arial", 17)).place(x=230, y=3000)
    Label(root1,
          text="-Zero cholesterol: Good for your heart and cardio vascular functioning\n Whole grain (Lower carbohydrates): Helps in overall health",
          font=("Arial", 13)).place(x=230, y=3060)
    Label(root1, text="-Country of Origin: India", font=("Arial", 13)).place(x=230, y=3120)
    Label(root1, text="-Lower GI: Diabetic friendly", font=("Arial", 13)).place(x=230, y=3460)
    Label(root1, text="-HET processed and enriched with vitamins and minerals: For stronger immunity",
          font=("Arial", 13)).place(x=230, y=3210)
    Button(root1, text="Buy Now", font=("Arial bold", 13)).place(x=280, y=3260)
    Button(root1, text="Add To Cart", font=("Arial bold", 13)).place(x=380, y=3260)

    img12 = (Image.open("2.jpg"))
    resized_image = img12.resize((200, 300), Image.ANTIALIAS)
    image12 = ImageTk.PhotoImage(resized_image)
    Label(root1, text="1)", font=("Arial", 13)).place(x=0, y=3330)
    Label(root1, image=image2).place(x=20, y=3330)
    Label(root1, text="Daawat Brown, Cooks in 15-minute, Full Bran Intact,\n Fibre-Rich Basmati Rice, 5 Kg",
          font=("Arial", 17)).place(x=230, y=3320)
    Label(root1,
          text="-Zero cholesterol: Good for your heart and cardio vascular functioning\n Whole grain (Lower carbohydrates): Helps in overall health",
          font=("Arial", 13)).place(x=230, y=3380)
    Label(root1, text="-Country of Origin: India", font=("Arial", 13)).place(x=230, y=3440)
    Label(root1, text="-Lower GI: Diabetic friendly", font=("Arial", 13)).place(x=230, y=3780)
    Label(root1, text="-HET processed and enriched with vitamins and minerals: For stronger immunity",
          font=("Arial", 13)).place(x=230, y=3530)
    Button(root1, text="Buy Now", font=("Arial bold", 13)).place(x=280, y=3580)
    Button(root1, text="Add To Cart", font=("Arial bold", 13)).place(x=380, y=3580)
    root1.mainloop()



def getfn():
    Gvar1=usrname.get()
    Gvar2=password.get()
    if Gvar1=="user":
        if Gvar2=="admin":
            root.destroy()
            getfn1()

        else:
            return Label(root, text="wrong passowrd",font=("Arial",12)).place(x=330,y=290)
    else:
        return Label(root, text="Wrong username", font=("Arial", 12)).place(x=330, y=290)


root= Tk()
root.title("Store")
root.geometry("700x700")
label1= Label(root,text="VIT Store",font=("Arial", 25)).place(x=350,y=0)
img1=(Image.open("1.png"))
resized_image= img1.resize((80,80), Image.ANTIALIAS)
image1= ImageTk.PhotoImage(resized_image)
label2= Label(root,image=image1).place(x=270,y=0)
usrname=StringVar()
password=StringVar()

Label(root, text="Username:",font=("Arial",10)).place(x=220,y=200)
Entry(root, width=30,textvariable = usrname).place(x=300,y=200)
Label(root, text="Password:",font=("Arial",10)).place(x=220,y=230)
Entry(root, width=30, textvariable=password).place(x=300,y=230)
Button(root, text="Login", command=getfn).place(x=330,y=260)
root.mainloop()

