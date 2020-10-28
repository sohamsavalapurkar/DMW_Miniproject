import tkinter
from tkinter import filedialog
from backend import dmw_mini
from tkinter import *
window = tkinter.Tk()
window.geometry("1024x720")

backend_class = dmw_mini()

def clear_frame():
    for w in window.winfo_children()[6:]:
        w.destroy()

def getTestInput():
    text.delete(0,tkinter.END)
    if v.get() == 1:
    
        filename =filedialog.askopenfilename(filetypes=(("csv files","*.csv"),("All files","*.*")))
        
        text.insert(tkinter.END, filename)

print_output = {1:'positive', 0: 'negative'}
def returnTestInput():
    clear_frame()
    if v.get() == 1:
        accuracy, confusion_matrix = backend_class.read_test_data_and_predict(text.get())
        Label(window, text='Naive Bayes').grid(row=3,column=1)
        Label(window, text=f'Accuracy : {accuracy[0]}%').grid(row=4,column=1 )
        Label(window, text=f'Confusion Matrix : ').grid(row=5,column=1 )
        Label(window, text=f'{confusion_matrix[0][0]}').grid(row=6,column=1 )
        Label(window, text=f'{confusion_matrix[0][1]}').grid(row=7,column=1 )
        

        Label(window, text='').grid(column=2)

        Label(window, text='KNN').grid(row=3,column=3)
        Label(window, text=f'Accuracy : {accuracy[1]}%').grid(row=4,column=3)
        Label(window, text=f'Confusion Matrix : ').grid(row=5,column=3)
        Label(window, text=f'{confusion_matrix[1][0]}').grid(row=6,column=3 )
        Label(window, text=f'{confusion_matrix[1][1]}').grid(row=7,column=3 )
    
        Label(window, text='').grid(column=4)

        Label(window, text='Random Forest').grid(row=3,column=5)
        Label(window, text=f'Accuracy : {accuracy[2]}%').grid(row=4,column=5)
        Label(window, text=f'Confusion Matrix : ').grid(row=5,column=5)
        Label(window, text=f'{confusion_matrix[2][0]}').grid(row=6,column=5 )
        Label(window, text=f'{confusion_matrix[2][1]}').grid(row=7,column=5 )

    else:
        output = backend_class.read_test_text_and_predict(text.get())
        Label(window, text='Naive Bayes').grid(row=3,column=1)
        print(output)
        Label(window, text=f'Prediction : {print_output[output[0][0]]} review').grid(row=4,column=1 )
        Label(window, text='KNN').grid(row=3,column=5)
        Label(window, text=f'Prediction : {print_output[output[1][0]]} review').grid(row=4,column=5)
        Label(window, text='Random Forest').grid(row=3,column=9)
        Label(window, text=f'Prediction : {print_output[output[2][0]]} review').grid(row=4,column=9 )
    return (v.get(), text.get())

if __name__ == '__main__':
    v = IntVar() 
    Radiobutton(window, text='File', variable=v, value=1, command=getTestInput).grid(row=1)
    Radiobutton(window, text='Text', variable=v, value=2, command=getTestInput).grid(row=1,column=1)
    text = Entry(window) 
    text.grid(row=1, column=9)
    Label(window, text='').grid(row=2)
    Label(window, text='Filepath/Text').grid(row=1,column=8 )
    load_data = Button(window, text = 'Load Data',command=returnTestInput).grid(row=1,column=11) 
    col_count, row_count = window.grid_size()
    print(col_count)
    print(row_count)
    for col in range(col_count):
        window.grid_columnconfigure(col, minsize=20)

    for row in range(row_count):
        window.grid_rowconfigure(row, minsize=20)

    window.mainloop()