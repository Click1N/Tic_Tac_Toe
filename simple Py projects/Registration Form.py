from tkinter import *
from tkinter.ttk import Label

# creat a class of the window. The root window has a title that defaults to tk
root = Tk()
# geometry() gives size of root window
root.geometry("500x300")
# to chage the titlr of the root window
root.title("Registration form")

# label(0 to show elenets on the widows,
#pack()- to show up label, instead of it we can do grid.(row=0, column =3)
Label(root, text = "Registration data", font="ar 15 bold").grid(row=0, column =3)


name = Label(root, text="Name").grid(row =1, column=0)
surname = Label(root, text="Surname").grid(row =2, column=0)
age = Label(root, text="Age").grid(row =3, column=0)
country = Label(root, text="Country").grid(row =4, column=0)
course = Label(root, text="Course").grid(row =5, column=0)
payment_mood = Label(root, text="Payment mood").grid(row =6, column=0)

# will creat string value for the name and then it will storage in name_val
name_val = StringVar()
surname_val = StringVar()
age_val = StringVar()
country_val = StringVar()
#course_val = StringVar()
course_val = IntVar
payment_mood_val = StringVar()
check_val= IntVar

#Second, create the name Entry widget and associate it with the name_val variable:
name_entry = Entry(root, textvariable=name_val).grid(row =1, column=1)
surname_entry = Entry(root, textvariable=surname_val).grid(row =2, column=1)
age_entry = Entry(root, textvariable=age_val).grid(row =3, column=1)
country_entry = Entry(root, textvariable=country_val).grid(row =4, column=1)
#course_entry = Entry(root, textvariable=course_val).grid(row =5, column=1)
payment_mood_entry = Entry(root, textvariable=payment_mood_val).grid(row =6, column=1)

check_btm = Checkbutton(text="remember me?", variable=check_val).grid(row =7, column=3)
course_btm1 = Checkbutton(text="English", variable=course_val).grid(row =5, column=1)
course_btm2 = Checkbutton(text="Italian", variable=course_val).grid(row =5, column=2)
course_btm3 = Checkbutton(text="French", variable=course_val).grid(row =5, column=3)

Button(text="Submit").grid(row =9, column=1)
Button(text="Exit").grid(row =9, column=2)



# mainloop() help to desplay all the time root window
root.mainloop()


# pip install tk - to install tkinter