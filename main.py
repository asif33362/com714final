from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox, ttk


class main:
     def __init__(self,screen):

        self.screen = screen
        self.flg = 0
        self.frm = Frame(self.screen,bg='White',width=900,height=500)  

     def main_fn(self):
        self.lbl = Label(self.frm,text='Sign IN',bg='White',font=('Arial',36,'bold'))
        self.nme = Label(self.frm,text='EMAIL: ',bg='White',font=('Arial',18,'bold'))
        self.nmee_text=StringVar()
        self.nmee = Entry(self.frm,textvariable=self.nmee_text,width=25,font=('Arial',16,'bold'))
        self.pass_ = Label(self.frm,text='Password : ',bg='White',font=('Arial',18,'bold'))
        self.pass_e_text=StringVar()
        self.pass_e = Entry(self.frm,textvariable=self.pass_e_text,bg='White',width=25,font=('Arial',16,'bold'),show='*')
        self.btn_main = Button(self.frm,text='LOG IN',bg='gray',font=('Arial',18,'bold'),cursor='hand2', command=self.main_admin)
        if self.flg !=0:
            self.btn_Admin = Button(self.frm,text='Admin',bg='Green',font=('Arial',18,'bold'),cursor='hand2', command=self.adminbtn_2)
        else:
            self.btn_Admin = Button(self.frm,text='Admin',bg='Green',font=('Arial',18,'bold'),cursor='hand2', command=self.adminbutton)
        self.buttonmember = Button(self.frm,text='Member',bg='Green',font=('Arial',18,'bold'),cursor='hand2', command=self.userbutton)
        self.btn_User = Button(self.frm,text='User',bg='Green',font=('Arial',18,'bold'),cursor='hand2', command=self.userbutton)
        self.lbl.place(x=40,y=40,width=200,height=80)
        self.nme.place(x=100,y=140,width=240,height=60)
        self.nmee.place(x=380,y=150,width=200,height=30)
        self.pass_.place(x=85,y=220,width=240,height=30)
        self.pass_e.place(x=380,y=215,width=200,height=30)
        self.btn_Admin.place(x=220,y=400,width=140,height=50)
        self.btn_User.place(x=380,y=400,width=140,height=50)
        self.buttonmember.place(x=550,y=400,width=140,height=50)
        self.btn_main.place(x=180,y=300,width=140,height=50)
        self.frm.pack()
     
    

     def adminbtn_2(self):
       
        self.btn_2.destroy()
        
        self.nme = Label(self.frm,text='Email: ',bg='White',font=('Arial',18,'bold'))
        self.nme.place(x=100,y=140,width=240,height=60)

     def register(self):
         self.btn_Admin.destroy()
         self.btn_User.destroy()
         self.buttonmember.destroy()
         self.lbl.destroy()
         self.nme.destroy()
         self.nmee.destroy()
         self.pass_.destroy()
         self.pass_e.destroy()
         self.btn_main.destroy()
         self.btn_2.destroy()
         self.lblr = Label(self.frm,text='Register',bg='White',font=('Arial',32,'bold'))
         self.nmer = Label(self.frm,text='Name : ',bg='White',font=('Arial',14,'bold'))
         self.nmere_text=StringVar()
         self.nmere = Entry(self.frm,textvariable=self.nmere_text)
         self.pass_wrd1 = Label(self.frm,text='Create Password : ',bg='White', font=('Arial',14,'bold'))
         self.pass_wrd1e_text=StringVar()
         self.pass_wrd1e = Entry(self.frm,textvariable=self.pass_wrd1e_text,bg='White',width=25,font=('Arial',12,'bold'),show='*')
         self.pass_wrd2e_text=StringVar()
         self.pass_wrd2 = Label(self.frm,text='Re-enter Password : ',bg='White', font=('Arial',14,'bold'))
         self.pass_wrd2e = Entry(self.frm,bg='White',width=25,font=('Arial',12,'bold'),show='*')
         self.btn_r = Button(self.frm,text='Register',bg='gray',font=('Arial',14,'bold'),cursor='hand2')
         self.btn_r2 = Button(self.frm,text='Back',bg='gray',font=('Arial',14,'bold'),cursor='hand2',  command= self.destroy)
         self.lblr.place(x=40,y=10,width=200,height=80)
         self.nmer.place(x=80,y=100,width=240,height=60)
         self.nmere.place(x=300,y=115,width=200,height=30)
         self.pass_wrd1.place(x=28,y=210,width=240,height=30)
         self.pass_wrd1e.place(x=300,y=210,width=200,height=30)
         self.pass_wrd2.place(x=23,y=253,width=240,height=30)
         self.pass_wrd2e.place(x=300,y=253,width=200,height=30)
         self.btn_r.place(x=160,y=330,width=140,height=50)
         self.btn_r2.place(x=320,y=330,width=140,height=50)

     def adminbutton(self):
        self.nme = Label(self.frm,text='Email: ',bg='White',font=('Arial',18,'bold'))
        self.nme.place(x=100,y=140,width=240,height=60)


     def userbutton(self):
        self.flg =1
        self.btn_main.destroy()
        self.btn_main = Button(self.frm,text='LOG IN',bg='gray',font=('Arial',18,'bold'),cursor='hand2', command=self.main_user)
        self.btn_main.place(x=180,y=300,width=140,height=50)

        self.nme = Label(self.frm,text='Name: ',bg='White',font=('Arial',18,'bold'))
        self.nme.place(x=100,y=140,width=240,height=60)
        self.btn_2 = Button(self.frm,text='SIGN UP',bg='gray',font=('Arial',18,'bold'),cursor='hand2', command=self.register)
        self.btn_2.place(x=340,y=300,width=140,height=50)

     def main_admin(self):
         if len(self.nmee.get()) ==0:
                    messagebox.showinfo("ERROR", "Mendatory empty")
         elif  len(self.pass_e.get()) == 0:
                 messagebox.showinfo("ERROR", "Mendatory empty")
         else:
             main_backend.check(self.nmee_text.get(),self.pass_e_text.get())

     def main_user(self):
          if len(self.nmee.get()) ==0:
                     messagebox.showinfo("ERROR", "Mendatory empty")
          elif  len(self.pass_e.get()) == 0:
                  messagebox.showinfo("ERROR", "Mendatory empty")
          else:
              main_backend.checks(self.nmee_text.get(),self.pass_e_text.get())

     def destroy(self):
         self.lblr.destroy()
         self.nmer.destroy()
         self.nmere.destroy()
         self.nme.destroy()
         self.btn_2.destroy()
         self.pass_wrd1.destroy()
         self.pass_wrd1e.destroy()
         self.pass_wrd2.destroy()
         self.pass_wrd2e.destroy()
         self.btn_r.destroy()
         self.btn_r2.destroy()
         self.btn_main.destroy()

         self.main_fn()



screen = Tk()
screen.title('main')
screen.geometry('900x500')

obj = main(screen)
obj.main_fn()
screen.mainloop()
