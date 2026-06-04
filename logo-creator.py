from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageFont
class logo_creator:
   def kiss_formula_(self):
       ttkx = Tk()
       xx = ttkx.winfo_screenwidth()
       yy = ttkx.winfo_screenheight()
       ttkx.geometry(("600x300+%d+%d")%((xx-600)/2, (yy-300)/2))
       ttkx.configure(bg="#660000")
       ttkx.overrideredirect(1)
       cnx = Canvas(ttkx, bg="#330000", width="600", height="29", highlightthickness=0)
       cnx.place(x=0, y=0)
       main_lab = Label(cnx, text="Logo Creator", bg="#330000", fg="#ffffff", font=("Gill Sans", 10))
       main_lab.place(x=10, y=2)
       cl = Label(cnx, text="×", bg="#330000", fg="#ffffff", font=("Arial", 10))
       cl.place(x=570, y=2)
       def ce(e):
             cl.config(fg="#ff8000")
       def cll(e):
             cl.config(fg="#ffffff")
       def cb(e):
           ttkx.destroy()
       cl.bind('<Enter>', ce)
       cl.bind('<Leave>',cll)
       cl.bind('<Button-1>', cb)
       l1 = Label(ttkx, text="Text (Not Use Big Text):", bg="#660000", fg="#ffffff", font=("Arial", 8))
       l1.place(x=10, y=40)
       l2 = Label(ttkx, text="Width:", bg="#660000", fg="#ffffff", font=("Arial", 8))
       l2.place(x=360, y=40)
       l3 = Label(ttkx, text="Height:", bg="#660000", fg="#ffffff", font=("Arial", 8))
       l3.place(x=10, y=80)
       l4 = Label(ttkx, text="Font (Exist In Your System):", bg="#660000", fg="#ffffff", font=("Arial", 8))
       l4.place(x=310, y=80)
       l5 = Label(ttkx, text="Background Color (HEX):", bg="#660000", fg="#ffffff", font=("Arial", 8))
       l5.place(x=10, y=120)
       l6 = Label(ttkx, text="Text Color (HEX):", bg="#660000", fg="#ffffff", font=("Arial", 8))
       l6.place(x=360, y=120)
       l7 = Label(ttkx, text="Destination:", bg="#660000", fg="#ffffff", font=("Arial", 8))
       l7.place(x=10, y=170)
       l8 = Label(ttkx, text="Text - X:", bg="#660000", fg="#ffffff", font=("Arial", 8))
       l8.place(x=10, y=209)
       l9 = Label(ttkx, text="Text - Y:", bg="#660000", fg="#ffffff", font=("Arial", 8))
       l9.place(x=120, y=209)
       _x1 = StringVar()
       _x2 = StringVar()
       _x3 = StringVar()
       _x4 = StringVar()
       _x5 = StringVar()
       _x6 = StringVar()
       _x7 = StringVar()
       _x8 = StringVar()
       _x9 = StringVar()
       et1 = Entry(ttkx, textvariable=_x1, width="30")
       et1.place(x=140, y=40)
       et2 = Entry(ttkx, textvariable=_x2, width="10")
       et2.place(x=460, y=40)
       et3 = Entry(ttkx, textvariable=_x3, width="10")
       et3.place(x=110, y=80)
       et4 = Entry(ttkx, textvariable=_x4, width="20")
       et4.place(x=460, y=80)
       et5 = Entry(ttkx, textvariable=_x5, width="20")
       et5.place(x=140, y=120)
       et6 = Entry(ttkx, textvariable=_x6, width="20")
       et6.place(x=460, y=120)
       et7 = Entry(ttkx, textvariable=_x7, state="disabled", width="60")
       et7.place(x=100, y=170)
       et8 = Entry(ttkx, textvariable=_x8, width="7")
       et8.place(x=60, y=209)
       et9 = Entry(ttkx, textvariable=_x9, width="7")
       et9.place(x=170, y=209)
       cr = Label(ttkx, text="Pranav", bg="#660000", fg="#ff9933", font=("Arial", 7))
       cr.place(x=239, y=269)
       browse = Label(ttkx, text="Browse", bg="#003366", fg="#ffffff", font=("Calibri", 8))
       browse.place(x=499, y=170)
       def be(e):
               browse.config(bg="#ff8000")
       def bl(e):
               browse.config(bg="#003366")
       def bb(e):
         fd =  filedialog.askdirectory(title="Select Destination")
         _x7.set(fd)
       browse.bind('<Enter>', be)
       browse.bind('<Leave>', bl)
       browse.bind('<Button-1>', bb)
       logo = Label(ttkx, text="Generate Logo", bg="#003366", fg="#ffffff", font=("Calibri", 8), height="2")
       logo.place(x=269, y=209)
       def le(e):
               logo.config(bg="#ff8000")
       def ll(e):
               logo.config(bg="#003366")
       def lb(e):
          if _x1.get()!="" and _x2.get()!="" and _x3.get()!="" and _x4!="" and _x5!="" and _x6!="" and _x7!="":
              if _x2.get().isnumeric()==True and _x3.get().isnumeric()==True:
                if len(_x5.get())==7 and len(_x6.get())==7:
                   if _x8.get().isnumeric()==True and _x9.get().isnumeric()==True:
                     img = Image.new("RGB", (int(_x2.get()), int(_x3.get())), _x5.get())
                     img_draw = ImageDraw.Draw(img)
                     fnt = ImageFont.truetype("C:\\Windows\\Fonts\\"+_x4.get()+".ttf", 18)
                     img_draw.text((int(_x8.get()), int(_x9.get())), _x1.get(), font=fnt, align="left")
                     xpath = _x7.get()+"\\"+_x1.get()+".png"
                     img.save(xpath)
                   else:
                       messagebox.showwarning("Error", "There is problem with x y cordinates of text.")
                else:
                   messagebox.showwarning("Error", "There is problem with colors.")
              else:
                   messagebox.showwarning("Error", "There is problem with width and height.")
          else:
               messagebox.showwarning("Error", "There is problem with putting data.")

       logo.bind('<Enter>', le)
       logo.bind('<Leave>', ll)
       logo.bind('<Button-1>', lb)
       return ttkx

if __name__=="__main__":
    lg = logo_creator()
    lg.kiss_formula_().mainloop()
  