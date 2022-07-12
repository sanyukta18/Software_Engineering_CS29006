import tkinter as tk
from tkinter import Button
from tkinter import Text
import threading
import time
from tkinter import *

my_w = tk.Tk()
my_w.geometry("1000x600")  # Size of the window 
my_w.title("social network")  # Adding a title
ii=0
my_w.configure(bg = "MediumPurple3")
# create the dictionary
my_dict1={} 
my_dict2={}
my_dict3={}
i = 1 
messages = {}
groups = {}
f = open("social_network.txt", "r")
flag = 0 
for x in f:
    #print(x)
    #print(x[0])
    l1 = []
    l2=[]
    c = 0
    if(x == "# users\n"):
        flag = flag+1
    if(flag == 1 and x[0]=="<"):
        #print("Enter") 
        for l in x.split():
            # print("Enter1")
            # print(l) 
            # print(" ")
            if(l.isdigit() and c==1):
                my_dict1[i]=int(l)
                my_dict3[int(l)] = []
                my_dict2[int(l)] = []
                messages[int(l)] = []
                i = i+1
                k = int(l)
            #print('\n')    
            if(c>1 and l.isdigit()):
                my_dict2[k].append(int(l))
            
            c = c+1

  
    if(x == "# groups\n"):
        flag = flag+1
    if(flag == 2):
        for l in x.split():
            #print(l)
            #print(" ")
            if(l.isdigit() and c==1): 
                k = int(l)
                groups[(int(l))]=[]
            if(c>1 and l.isdigit()):
                my_dict3[int(l)].append(k)
                groups[k].append(int(l))
            c=c+1

        #print('\n')

print(my_dict1)  
print('\n')
print(my_dict2)
print('\n')
print(my_dict3)
print('\n')
print(groups)
print('\n')
# for keys,values in my_dict1.items():
#     print(keys)
#     print(values)                    

#print("h1");
options = tk.StringVar(my_w) # variable 
options.set(my_dict1[1]) # default value

l4= tk.Label(my_w, 
         text="Select user :")
l4.configure(bg = "MediumPurple3",font=("Courier", 11))

l4.place(x=1,y=20)
om1 =tk.OptionMenu(my_w, options, *my_dict1.values())
om1.place(x=120,y=20)

current = -1
def my_show(*args):
    global current 
    
    for i,j in my_dict1.items():
        if str(j)==options.get():
            print("i: ",i) 
            ii=i  # ii is int
            current = my_dict1[i]
            print("current: ",current)
            Output2.delete("1.0","end")
            Output3.delete("1.0","end")
            Output1.delete("1.0","end")
def print_contacts():
    global current 
    if current!=-1:
        for j in my_dict2[current]:
            Output2.insert(END,str(j)+"\n\n")
            k+=1

def print_groups(): 
    global current
    if current!=-1:
        for j in my_dict3[current]:
            Output3.insert(END,str(j)+"\n\n")

def print_messages():
    Output1.delete("1.0","end")
    global current
    print("curr: ",current)
    if current!=-1:
        for j in messages[current]:
            Output1.insert(END,str(j)+"\n\n")
     
E1=tk.StringVar()
E2=tk.StringVar()   
E3=tk.StringVar() 

def send():
    E2 = e2.get()
    E3 = e3.get()
    E1 = e1.get()
    while((len(E3)!=0) or (len(E2)!=0)):
            if(len(E2) != 0):
                if(len(E1)==0):
                    continue
                else:
                    print(E1)
                    print('\n')
                    messages[int(E2)].append(E1)

                E2 = ""  
                E1 = "" 
                e2.delete(0,END) 
                e1.delete(0,END)

            if(len(E3) != 0):
                if(len(E1) ==0):
                   continue
                else:
                    for i in groups[int(E3)]:
                        messages[int(i)].append(E1)
                E3 = ""  
                E1 = ""
                e1.delete(0,END) 
                e3.delete(0,END)
            
l2 = tk.Label(my_w, 
     text="Enter user to send message to:")
l2.configure(bg = "MediumPurple3",font=("Courier", 11))
l2.place(x=1,y=500)
e2 = tk.Entry(my_w,textvariable = E2)
e2.place(x=1,y=520)



l3 = tk.Label(my_w, 
         text="Enter group to send message to:")
l3.place(x=300,y=500)
l3.configure(bg = "MediumPurple3",font=("Courier", 11))
e3 = tk.Entry(my_w,textvariable = E3)
e3.place(x=300,y=520)

l1 = tk.Label(my_w, 
         text="Enter message")
l1.configure(bg = "MediumPurple3",font=("Courier", 11))
l1.place(x=1,y=550)
e1 = tk.Entry(my_w,textvariable = E1)
e1.place(x=140,y=550)


Display5= Button(my_w, height = 2, 
         width = 30,  
         text ="send",font=("Courier", 11),command=send )
Display5.configure(bg = "SlateGray2")
Display5.place(x=300,y=550) 


#def f1():
#    global current

# options.trace('w',my_show)
# my_w.mainloop()
# print("current2: ",current)   


#def f2():
#    global current

    #Interface

Display1 = Button(my_w, height = 2, 
                 width = 28,  
                 text ="Incoming messages",font=("Courier", 11),command= print_messages)
Display1.configure(bg = "SlateGray2")
Display1.place(x=10,y=100)   
Output1 = Text(my_w, height = 30,  
              width = 40,font=("Helvetica", 10)) 
Output1.place(x=10,y=150)

Display2 = Button(my_w, height = 2, 
                 width = 27,  
                 text ="Contacts",font=("Courier", 11),command = print_contacts)
Display2.configure(bg = "SlateGray2")
Display2.place(x=350,y=100)   
Output2 = Text(my_w, height = 30,  
              width = 40,font=("Helvetica", 10)) 
Output2.place(x=350,y=150)

Display3 = Button(my_w, height = 2, 
                 width = 35,  
                 text ="Groups",font=("Courier", 10),command =  print_groups)
Display3.configure(bg = "SlateGray2")
Display3.place(x=700,y=100)   
Output3 = Text(my_w, height = 30,  
              width = 40,font=("Helvetica", 10)) 
Output3.place(x=700,y=150)


Output1 = Text(my_w, height = 30,  
              width = 40) 
Output1.place(x=10,y=150)

options.trace('w',my_show)
#options.trace('w',my_show)
my_w.mainloop()



# t1 = threading.Thread(target=f1)
# t2 = threading.Thread(target=f2)   
# t1.start()
# time.sleep(4)
# t2.start()
# t2.join()
# t1.join()      
           



#print("h2");

# b1 = tk.Button(my_w,text="Show messages",command=send_msg_to_user)
# b1.place(x=1,y=100)
