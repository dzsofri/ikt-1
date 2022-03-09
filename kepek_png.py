from tkinter import *
def klikk():
    print("Klikkeltem")
ablak1 =  Tk()
gyoker = "C:\\Users\\beretizsofia\\Desktop\\python\\"

ablak1.geometry("450x450")
ablak1.title("IKT Tkinter")
icon = PhotoImage(file=gyoker+'cica.png')
ablak1.iconphoto(True, icon)
ablak1.config(background='black')
elsokep = PhotoImage(file=gyoker+"among-us-sus.gif")
gombkep = PhotoImage(file=gyoker+"among-us-sus.gif")

cimke= Label(ablak1,
             text="Üdvözlet",      
             fg='#553388',
             bg="#c3cee0",
             font=("Arial", 45, "bold"),
             bd=10,
             relief=RAISED,
             padx=25,
             pady=30,
             image=elsokep,
             compound="bottom").pack()

gomb = Button(ablak1,
              text= "kattints",
              font= ("Comic Sans", 35, "bold"),
              bg="yellow",
              relief=SUNKEN,
              bd=10,
              command=klikk,
              padx=12,
              pady=12,
              #image=gombkep,
              compound="bottom",
              activebackground="blue",
              activeforeground="yellow",
              state=ACTIVE).pack()

ablak1.mainloop()