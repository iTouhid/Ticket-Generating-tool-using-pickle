from Tkinter import *
root = Tk()
import pickle

data = 'C\\Users\\Touhid\\Desktop\\details.pkl'

def submit():
    global root
    global nameE
    global emailE
    global ttypeE
    global messageE

    intruction = Label(root, text= "Please Enter Ticket Details\n")
    intruction.grid(row=0, column = 0, sticky=E)

    nameL = Label(root, text= 'Name : ')
    emailL = Label(root, text= "Email Id : ")
    ttypeL = Label(root, text='Ticket Type : ')
    messageL = Label(root, text='Message')
    nameL.grid(row=1, column= 0, sticky= W)
    emailL.grid(row=2, column=0, sticky=W)
    ttypeL.grid(row = 3, column=0, sticky = W)
    messageL.grid(row = 4, column=0, sticky=W)

    nameE=Entry(root)
    emailE=Entry(root)
    ttypeE=Entry(root)
    messageE= Entry(root)
    nameE.grid(row = 1, column= 1)
    emailE.grid(row = 2, column=1)
    ttypeE.grid(row=3, column = 1)
    messageE.grid(row=4, column = 1)

    submitButton = Button(root, text='Submit', command=FssSubmit)
    viewButton = Button(root, text='View Ticket', command=Fssview)
    submitButton.grid(columnspan=2, sticky=W)
    viewButton.grid(columnspan=2, sticky=W)
def FssSubmit():
    dataStore = open(data,'wb')
    pickle.dump(nameE.get(), dataStore)
    pickle.dump(emailE.get(), dataStore)
    pickle.dump(ttypeE.get(), dataStore)
    pickle.dump(messageE.get(), dataStore)
    dataStore.close()

    root.destroy()
def Fssview():
    nameL = Label(root, text='Name : ')
    emailL = Label(root, text="Email Id : ")
    ttypeL = Label(root, text='Ticket Type : ')
    messageL = Label(root, text='Message')
    nameL.grid(row=1, column=0, sticky=W)
    emailL.grid(row=2, column=0, sticky=W)
    ttypeL.grid(row=3, column=0, sticky=W)
    messageL.grid(row=4, column=0, sticky=W)
    pklFile = open(data, 'rb')
    nameL = pickle.load(pklFile)
    emailL = pickle.load(pklFile)
    ttypeL = pickle.load(pklFile)
    messageL = pickle.load(pklFile)
    pklFile.close()


submit()
root.mainloop()