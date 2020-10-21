import tkinter
from tkinter import filedialog
from backend import dmw_mini
from tkinter import *
window = tkinter.Tk()
window.geometry("1024x720")

backend_class = dmw_mini()

def getTestInput():
    text.delete(0,tkinter.END)    
    if v.get() == 1:
    
        filename =filedialog.askopenfilename(filetypes=(("text files","*.txt"),("All files","*.*")))
        
        text.insert(tkinter.END, filename)
        
        
def returnTestInput():
    if v.get() == 1:
        backend_class.read_test_data_and_predict(text)
    else:
        output = backend_class.read_test_text_and_predict(text.get())
    accuracy = '98.4'
    Label(window, text='Naive Bayes').grid(row=3,column=1)
    Label(window, text=f'Accuracy : {output[0]}').grid(row=4,column=1 )
    return (v.get(), text.get())


v = IntVar() 
Radiobutton(window, text='File', variable=v, value=1, command=getTestInput).grid(row=1)
Radiobutton(window, text='Text', variable=v, value=2, command=getTestInput).grid(row=1,column=1)
text = Entry(window) 
text.grid(row=1, column=9)
Label(window, text='').grid(row=2)
Label(window, text='Filepath/Text').grid(row=1,column=8 )
load_data = Button(window, text = 'Load Data',command=returnTestInput).grid(row=1,column=11) 
naive_bayes = Text(window, height=10, width=20)


window.mainloop()