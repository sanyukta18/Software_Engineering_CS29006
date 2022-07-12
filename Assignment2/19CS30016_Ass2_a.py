from tkinter import *
from ast import literal_eval
import numpy as np
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk) 

class RightFrame(Frame):
    def __init__(self, master=None,rframe=None):
        Frame.__init__(self, master,bg="lightPink1")
        self.master = master
        self.rframe = rframe
        self.grid(row=0, column=1,sticky=S+N+E+W)
        #self.textbox = Text(self,width=2,height=2,padx=10,pady=10,bd=5)
        #self.textbox.insert(END,"enter your expression and value of variable")
        #self.textbox.grid(row=0,column=0,sticky=S+N+E+W)

    def insert(self, ins_string):
        textbox.insert(END,ins_string)



class LeftFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master,bg="light sky blue")
        self.master = master
        master.grid_columnconfigure(1,weight=1)
        self.grid(row=0, column=0,sticky=S+N+E+W)
        master.grid_columnconfigure(0,weight=1)
        master.grid_rowconfigure(0,weight=1)

        self.lab1 = Label(self,text="Expression (variable x): ")
        self.lab1.grid(row=0,column=0)
        self.lab1.configure(bg="light sky blue")
        self.exprtext = Text(self,width=40,height=2,padx=10,pady=20)
        self.exprtext.insert(END, "expr")
        self.exprtext.grid(row=0,column=1,columnspan=2)

        self.lab2 = Label(self, text="Variable Range (a,b): ")
        self.lab2.grid(row=1, column=0)
        self.lab2.configure(bg="light sky blue")

        self.variablevalue = Text(self,width=10,height=2,padx=2,pady=20)
        self.variablevalue.insert(END, "value")
        self.variablevalue.grid(row=1,column=1)


        self.evaluatebutton = Button(self,text="Plot",command=self.evaluate,width=10,height=2,padx=2,pady=20)
        self.evaluatebutton.place(x=100, y=500)
        self.evaluatebutton.configure(bg="ivory2")

        self.exitbutton = Button(self, text="Exit", command=exit, width=5, height=2, padx=2, pady=20)
        self.exitbutton.place(x=200, y=500)
        self.exitbutton.configure(bg="ivory2")
        
    def evaluate(self):
        expr=self.exprtext.get(1.0,END)
        #print(expr)
        varval=self.variablevalue.get(1.0,END)
        #print(varval)
        a=literal_eval(varval)
        #self.lframe.textbox.delete(1.0,END)
        #print(a)
        z=[]
        b=[]
        for x in np.linspace(a[0],a[1],10):
            expr=expr.strip('\n')
            y=eval(expr)
            z.append(x)
            b.append(y)
            #print(expr+' ( '+str(x)+' ) '+' = '+str(y))
            #self.rframe.textbox.insert(END,expr+' ( '+str(x)+' ) '+' = '+str(y)+'\n')
         
        fig = Figure(figsize = (3, 3),dpi = 100)   
        plot1 = fig.add_subplot(111) 
  
        # plotting the graph 
        plot1.plot(b) 
        canvas = FigureCanvasTkAgg(fig,master = self)   
        canvas.draw() 
        canvas.get_tk_widget().place(x=100,y=150)  
        toolbar = NavigationToolbar2Tk(canvas,self) 
        toolbar.update()  
        canvas.get_tk_widget().place(x=300,y=300) 

            



class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        master.geometry("1000x600")
        
        self.leftframe = LeftFrame(master)
        self.rightframe = RightFrame(master,self.leftframe)
        master.wm_title("expression calculator")
        self.grid(row=0,column=0,sticky="nsew")

 
# initialize tkinter
root = Tk()
app = Window(root)

# set window title
#root.wm_title("Tkinter window")

# show window
root.mainloop()