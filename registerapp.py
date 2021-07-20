from os import close
from tkinter import *
#window 
window = Tk()
window.title("Registration Form")
window.geometry("650x600")
window.resizable(False,False)
window.config(background="#ACBAB6")
main_title = Label(window, text= "Registration Form", bg="#30A282", font="Arial", fg= "white", width="500", height="2")
main_title.pack()

#functions.

def send_data():
    lastaname_data = lastname.get()
    name_data = name.get()
    age_data =str(age.get())
    email_data = email.get()

   
    new_file= open("registration.txt", "a")
    new_file.write(lastaname_data)
    new_file.write("\t")
    new_file.write(name_data)
    new_file.write("\t")
    new_file.write(age_data)
    new_file.write("\t")
    new_file.write(email_data)
    new_file.write("\n")
    lastname_entry.delete(0, END)
    name_entry.delete(0, END)
    age_entry.delete(0, END)
    email_entry.delete(0,END)
    new_file(close)






    


#labels form.

lastname_label = Label(text="Lastname", fg="black" )
lastname_label.place(x=22, y= 70)
name_label = Label(text="Name", fg="black" )
name_label.place(x=22, y= 130)
age_label = Label(text="Age", fg="black" )
age_label.place(x=22, y= 190)
email_label = Label(text="E-mail", fg="black" )
email_label.place(x=22, y= 250)

lastname = StringVar()
name = StringVar()
age = StringVar()
email = StringVar()

lastname_entry = Entry(textvariable = lastname , width="50")
name_entry = Entry(textvariable = name, width="50")
age_entry = Entry(textvariable = age, width="50")
email_entry = Entry(textvariable = email, width="50")

lastname_entry.place(x=22, y=100)
name_entry.place(x= 22, y=160)
age_entry.place(x= 22, y=220)
email_entry.place(x= 22, y=280)

#Button.
sumbit_button = Button(window, text= "Sumbit", command= send_data, width="30", height="2", bg="#30A282")
sumbit_button.place(x=22, y= 340)







 
window.mainloop()
