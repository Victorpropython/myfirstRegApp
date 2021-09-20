from tkinter import *
import inec_bck as bck
from tkinter import messagebox

def get_selected_row(events):
    global selected_tuple
    index=list1.curselected()[0]
    selected_tuple=list1.get(index)

    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])
    e5.delete(0,END)
    e5.insert(END,selected_tuple[5])

"""def selected_tuple([0]):
    global selected_tuple
    selected_tuple=list1.get(index)
"""
def view_command():
    list1.delete(0,END)
    for row in bck.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in bck.search(lastname_text.get(),fname_text.get(),other_name_text.get(),dateofreg_text.get(),formNum_text.get()):
        list1.insert(END,row)

def Submit_command():

    bck.insert(lastname_text.get(),fname_text.get(),other_name_text.get(),dateofreg_text.get(),formNum_text.get())
    list1.delete(0,END)
    list1.insert(END,lastname_text.get(),fname_text.get(),other_name_text.get(),dateofreg_text.get(),formNum_text.get())
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)


def delete_command(list1):
    values=list1.curselection()
    if values:
        index=values[0]
    #selected_tuple=
        val=list1.get(index)
        messagebox.showinfo("Selection",val)
        bck.delete(val[0])
        list1.delete(0,END)

def update_command():
    #selected_tuple=l'ist1.get(index)
    values=list1.curselection()
    if values:
        index=values[0]
        val=list1.get(index)
    bck.update(val[0],lastname_text.get(),fname_text.get(),other_name_text.get(),dateofreg_text.get(),formNum_text.get())

window=Tk()

l1=Label(window,text="LastName")
l1.grid(row=0,column=0)

l2=Label(window,text="FirstName")
l2.grid(row=0,column=2)

l3=Label(window,text="OtherName")
l3.grid(row=0,column=4)

l4=Label(window,text="Date_of_Reg")
l4.grid(row=1,column=0)

l5=Label(window,text="Form_number")
l5.grid(row=1,column=2)

lastname_text=StringVar()
e1=Entry(window,textvariable=lastname_text)
e1.grid(row=0,column=1)

fname_text=StringVar()
e2=Entry(window,textvariable=fname_text)
e2.grid(row=0,column=3)

other_name_text=StringVar()
e3=Entry(window,textvariable=other_name_text)
e3.grid(row=0,column=5)

dateofreg_text=StringVar()
e4=Entry(window,textvariable=dateofreg_text)
e4.grid(row=1,column=1)

formNum_text=StringVar()
e5=Entry(window,textvariable=formNum_text)
e5.grid(row=1,column=3)

list1=Listbox(window,width=42,height=13)
list1.grid(row=4,column=0,rowspan=6,columnspan=4)

scb1=Scrollbar(window)
scb1.grid(row=4,column=2,columnspan=3)

list1.configure(yscrollcommand=scb1.set)
scb1.configure(command=list1.yview)
list1.bind('<<listboxselect>>',get_selected_row)

b1=Button(window,text="Submit",width=10,bg='grey',command=Submit_command)
b1.grid(row=3,column=2,columnspan=2,pady=10,padx=10)

b2=Button(window,text="View All",width=10,command=view_command)
b2.grid(row=4,column=4)

b3=Button(window,text="Search",width=10,command=search_command)
b3.grid(row=5,column=4)

b4=Button(window,text="Update",width=10,command=update_command)
b4.grid(row=6,column=4)

b5=Button(window,text="Delete",width=10,command=lambda: delete_command(list1))
b5.grid(row=7,column=4)

b6=Button(window,text="Close",width=10,command=window.destroy)
b6.grid(row=8,column=4)

window.mainloop()
