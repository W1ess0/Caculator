import tkinter as tk

class Calculator:
    """dedfined calculator"""
    def __init__(self,master):
        self.master = master
        self.master.title("Calculator")
        #create entry field
        self.display = tk.Entry(self.master,width=40,borderwidth=5,font=("Times New Roman",16))
        self.display.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
        
        #create buttons
        self.create_buttons("7",1,0)
        self.create_buttons("8",1,1)
        self.create_buttons("9",1,2)
        self.create_buttons("/",1,3)
        self.create_buttons("4",2,0)
        self.create_buttons("5",2,1)
        self.create_buttons("6",2,2)
        self.create_buttons("*",2,3)
        self.create_buttons("1",3,0)
        self.create_buttons("2",3,1)
        self.create_buttons("3",3,2)
        self.create_buttons("-",3,3)
        self.create_buttons("0",4,0)
        self.create_buttons(".",4,1)
        self.create_buttons("C",4,2)
        self.create_buttons("+",4,3)
        self.create_buttons("=",5,3)


    def create_buttons(self,text,row,column):
        """function for show the buttons"""
        button = tk.Button(self.master, text=text, width=5, height=2,command=lambda: self.button_click(text))
        button.grid(row=row,column=column,padx=5,pady=5)

    def button_click(self,text):
        """function for mouse_clicking and calculating"""
        if text == "=":
            result = eval(self.display.get())
            self.display.delete(0,tk.END)
            self.display.insert(0,str(result))
        elif text == "C":
            self.display.delete(0,tk.END)
        else:
            self.display.insert(tk.END,text)
    
if __name__ == "__main__":
    root = tk.Tk()
    cal = Calculator(root)
    root.mainloop()