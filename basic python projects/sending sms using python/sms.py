# API(Application programming interface )
# which is a software intermidiary that allows two applications to talk each other

import requests
import json
from tkinter import *   # all modules in the tkinter will import
from tkinter.messagebox import showinfo,showerror # next import dailougebox, showinfo,showerror
                                                  # sms sent showinfo and sms error is showerror


def send_sms(number,message):    #number and message are paarmeters 
    url = 'https://www.fast2sms.com/dev/bulk'
    params = {
        'authorization': 'iPbSBHVP1M5EBsNSYZi877FnJkzONoAu0VQ8sMZCGUUxiBvvCPKKG1tNBjLR',
        'sender_id': 'FSTSMS',
        'message' : message,
        'language':'english',
        'route'  : 'p',   # p is the promotion
        'numbers' : number    
    }
    response = requests.get(url, params=params)   # request.get means the website given the permission or not                                                  
    dic = response.json()                  #dictionary format        
    print(dic)
    return dic.get('return')

def btn_click():
    num = textNumber.get()             # it get the number
    msg = textMsg.get("1.0",END)       # it get the msg
    r = send_sms(num,msg)             # r is a variable and send sms to number and msg
    if r:
        showinfo("Send Success", "Sucessfully sent")    #msg sent
    else:
        showerror("Error","Something went wrong..")     #msg error
        
# creating GUI
root = Tk()
root.title("message sender")
root.geometry("400x550")
font =("Helvetica",22,"bold")
textNumber = Entry(root,font=font)   # root is passing to a function because root is 
                                      #taken as a function
textNumber.pack(fill=X,pady=20)    
textMsg = Text(root)
textMsg.pack(fill=X)
sendBtn = Button(root, text="SEND SMS ",command=btn_click)   #creation of send button
sendBtn.pack()
root.mainloop()