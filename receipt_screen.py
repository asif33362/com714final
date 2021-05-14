from tkinter import *


class receipt:
        def __init__(self,window):
            self.window = window

            self.frame = Frame(self.window, bg = 'white', width=800,height=450)

            self.frame.pack()

            self.label = Label(self.frame,text='Property Receipt ',bg='white',font=('Arial',30,'bold'))
            self.label.place(x=200,y=20,width=400,height=50)

            self.label_property = Label(self.frame, text='Property :',bg='white',font=('Arial',8,'bold'))
            self.label_property.place(x=120,y=100,width=100,height=50)

            self.label_Manager = Label(self.frame, text='Manager :',bg='white',font=('Arial',8,'bold'))
            self.label_Manager.place(x=120,y=150,width=100,height=30)

            self.label_locality = Label(self.frame, text='Locality :',bg='white',font=('Arial',8,'bold'))
            self.label_locality.place(x=120,y=200,width=100,height=30)

            self.label_Throughlane = Label(self.frame, text='Throughlane :',bg='white',font=('Arial',8,'bold'))
            self.label_Throughlane.place(x=120,y=250,width=100,height=30)
            self.label_amount = Label(self.frame, text='Amount',bg='white',font=('Arial',8,'bold'))
            self.label_amount.place(x=120,y=300,width=100,height=30)

            self.property_text=StringVar()
            self.entry_property = Label(self.frame, text='Star Estate',bg='white',font=('Arial',8,'bold'))
            self.entry_property.place(x=220,y=100,width=150,height=30)

            self.manager_text=StringVar()
            self.entry_manager = Label(self.frame, text='Jhon Cooper',bg='white',font=('Arial',8,'bold'))
            self.entry_manager.place(x=220,y=150,width=150,height=30)

            self.locality_text=StringVar()
            self.entry_locality = Label(self.frame, text='Square tile road',bg='white',font=('Arial',8,'bold'))
            self.entry_locality.place(x=220,y=200,width=150,height=30)

            self.throughlane_text=StringVar()
            self.entry_throughlane = Label(self.frame, text='Garden walkway',bg='white',font=('Arial',8,'bold'))
            self.entry_throughlane.place(x=220,y=250,width=150,height=30)
            self.entry_throughlane = Label(self.frame, text='$ 60000',bg='white',font=('Arial',8,'bold'))
            self.entry_throughlane.place(x=220,y=300,width=150,height=30)

            

            self.button_view = Button(self.frame,text='Print', command=self.view_command)
            self.button_view.place(x=250,y=380,width=100,height=40)

            


        

        def view_command(self):
        
            print("paid")

        

window = Tk()
window.title('receipt_User')
window.geometry('700x450')
obj = receipt(window)
window.mainloop()
