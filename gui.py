# Import Module
from tkinter import *

# create root window
root = Tk()

# root window title and dimension
root.title("Diabetes Predictive Diagnosis Module")
# Set geometry (widthxheight)
root.geometry('1280x720')

lblIntro = Label(root, text = "Welcome to the Diabetes Predictive Diagnosis Module!\nPlease enter the following information: ", font=('Arial', 12), justify = "left")
lblIntro.grid(padx = 10, ipady = 10)
lblIntro.pack()

usrAgeInp = Entry(root, bd =5)
usrAgeInp.pack(anchor = W)
# from https://www.tutorialspoint.com/python/tk_entry.htm
usrSmoker = 0
smokeNo = Radiobutton(root, text="Non-smoker", variable=usrSmoker, value=0)
smokeNo.pack( anchor = W )
smokeYes = Radiobutton(root, text="Smoker", variable=usrSmoker, value=1)
smokeYes.pack( anchor = W )
# from https://www.tutorialspoint.com/python/tk_radiobutton.htm
bpMedNo = Radiobutton(root, text="Not currently taking blood pressure medication", variable=usrSmoker, value=0)
bpMedNo.pack( anchor = W )
bpMedYes = Radiobutton(root, text="Currently taking blood pressure medication", variable=usrSmoker, value=1)
bpMedYes.pack( anchor = W )
# Create option for cigarettes per day, education, sex, and 10-year HD risk?

usrAgeInp.pack()
smokeNo.pack()
smokeYes.pack()
bpMedNo.pack()
bpMedYes.pack()

smokeNo.select()

# all widgets will be here
# Execute Tkinter
root.mainloop()