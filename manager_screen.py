from tkinter import *


class manager_screen:
        def __init__(self,window):
            self.window = window

            self.frame = Frame(self.window, bg = 'white', width=800,height=450)

            self.frame.pack()

            self.label = Label(self.frame,text='',bg='white',font=('Arial',30,'bold'))
            self.label.place(x=20,y=20,width=400,height=50)

            self.label_prroperty = Label(self.frame, text='Property',bg='white',font=('Arial',8,'bold'))
            self.label_prroperty.place(x=20,y=100,width=100,height=50)

            self.label_manager = Label(self.frame, text='Manager',bg='white',font=('Arial',8,'bold'))
            self.label_manager.place(x=20,y=150,width=100,height=30)

            self.label_area = Label(self.frame, text='Area',bg='white',font=('Arial',8,'bold'))
            self.label_area.place(x=350,y=100,width=100,height=30)

            self.label_thrroughlane = Label(self.frame, text='Throughlane',bg='white',font=('Arial',8,'bold'))
            self.label_thrroughlane.place(x=350,y=150,width=100,height=30)

            self.title_text=StringVar()
            self.entry_title = Entry(self.frame, fg='gray',textvariable=self.title_text,width=25,font=('Arial',12,'bold'))
            self.entry_title.place(x=120,y=100,width=150,height=30)

            self.year_text=StringVar()
            self.entry_year = Entry(self.frame, fg='gray',textvariable=self.year_text,width=25,font=('Arial',12,'bold'))
            self.entry_year.place(x=120,y=150,width=150,height=30)

            self.author_text=StringVar()
            self.entry_author = Entry(self.frame, fg='gray',textvariable=self.author_text,width=25,font=('Arial',12,'bold'))
            self.entry_author.place(x=470,y=100,width=150,height=30)

            self.isbn_text=StringVar()
            self.entry_isbn = Entry(self.frame, fg='gray',textvariable=self.isbn_text,width=25,font=('Arial',12,'bold'))
            self.entry_isbn.place(x=470,y=150,width=150,height=30)
            self.info = Label(self.frame, text='REsult',bg='white',font=('Arial',8,'bold'))
            self.info.place(x=100,y=180,width=500,height=100)
            self.listbox = Listbox(self.frame)
            self.listbox.place(x=100,y=200,width=500,height=100)

            self.button_view = Button(self.frame,text='View All')
            self.button_view.place(x=100,y=320,width=100,height=40)
            self.button_clear = Button(self.frame,text='Clear All')
            self.button_clear.place(x=200,y=320,width=100,height=40)
            self.button_search = Button(self.frame,text='Search ')
            self.button_search.place(x=100,y=380,width=100,height=40)

            self.button_add = Button(self.frame,text='Add entry')
            self.button_add.place(x=200,y=380,width=100,height=40)

            self.button_update = Button(self.frame, text='Update entry')
            self.button_update.place(x=300, y=380,width=100,height=40)

            self.button_delete = Button(self.frame, text='Delete entry')
            self.button_delete.place(x=400, y=380,width=100,height=40)

            


        def destroy(self):
            self.button_issuedelete.destroy()
            self.button_requestdelete.destroy()

        

       

window = Tk()
window.title('manager_screen_User')
window.geometry('900x500')
obj = manager_screen(window)
window.mainloop()
