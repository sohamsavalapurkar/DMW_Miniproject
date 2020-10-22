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
    
        filename =filedialog.askopenfilename(filetypes=(("csv files","*.csv"),("All files","*.*")))
        
        text.insert(tkinter.END, filename)

print_output = {1:'positive', 2: 'negative'}        
        
def returnTestInput():
    if v.get() == 1:
        accuracy, confusion_matrix = backend_class.read_test_data_and_predict(text.get())
        Label(window, text='Naive Bayes').grid(row=3,column=1)
        Label(window, text=f'Accuracy : {accuracy[0]}%').grid(row=4,column=1 )
        Label(window, text=f'Confusion Matrix : ').grid(row=5,column=1 )
        Label(window, text=f'{confusion_matrix[0][0]}').grid(row=6,column=1 )
        Label(window, text=f'{confusion_matrix[0][1]}').grid(row=7,column=1 )

        Label(window, text='KNN').grid(row=3,column=7)
        Label(window, text=f'Accuracy : {accuracy[1]}%').grid(row=4,column=7)
        Label(window, text=f'Confusion Matrix : ').grid(row=5,column=7 )
        Label(window, text=f'{confusion_matrix[1][0]}').grid(row=6,column=7 )
        Label(window, text=f'{confusion_matrix[1][1]}').grid(row=7,column=7 )
    
        Label(window, text='Random Forest').grid(row=3,column=10)
        Label(window, text=f'Accuracy : {accuracy[2]}%').grid(row=4,column=10)
        Label(window, text=f'Confusion Matrix : ').grid(row=5,column=10)
        Label(window, text=f'{confusion_matrix[2][0]}').grid(row=6,column=10 )
        Label(window, text=f'{confusion_matrix[2][1]}').grid(row=7,column=10 )

    else:
        output = backend_class.read_test_text_and_predict(text.get())
        Label(window, text='Naive Bayes').grid(row=3,column=1)
        Label(window, text=f'Prediction : {print_output[output[0][0]]} review').grid(row=4,column=1 )
        Label(window, text='KNN').grid(row=3,column=5)
        Label(window, text=f'Prediction : {print_output[output[1][0]]} review').grid(row=4,column=5)
        Label(window, text='Random Forest').grid(row=3,column=9)
        Label(window, text=f'Prediction : {print_output[output[2][0]]} review').grid(row=4,column=9 )
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