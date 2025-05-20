import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from urllib import response
from PIL import Image, ImageTk 
import random
from datetime import datetime
from datetime import date

today = date.today()
today=str(today).split("-")
y,m,d=[int(i) for i in today]
hosts_path = r"/private/etc/hosts"
redirect= "127.0.0.1"
#Main GUI
root=tk.Tk()
root.title("~Bloxite~")
root.geometry("500x650")

#Canvas
bg = PhotoImage(file ="background.png")
canvas1 = Canvas(root, width = 400,height = 400)
canvas1.pack(fill = "both",expand = True)
canvas1.create_image( 0, 0, image = bg,anchor = "nw")

#Logo
canvas1.create_text(250,50,text="BLOXITE", fill="black", font=('Selima 60 bold'),anchor=CENTER,justify="center")

#Quotes
with open("quotes.txt") as quotes:
    q=quotes.read().split("\n")
    del q[-1]
    quote=(random.choice(q))
canvas1.create_text(250,95,text=('"'+quote+'"'),fill="black",font=('Times 12 italic bold'),anchor=CENTER,justify="center")


#Introduction
intro= tk.Label(root,text="Enter Your Desired Websites to be Blocked in the Textbox :",font="Sylfaen 13 underline",bg="#b2dff3")
intro.place(relx=0.5,rely=0.21,anchor=CENTER)

#Website_Entry_textbox
site_name= Text(root,width=26,height=6, font=("Sylfaen",14),borderwidth=8, relief="ridge",bg="#b2dff3")
site_name.place(relx=0.335,rely=0.39,anchor=CENTER)
site_name.insert(1.0,"\nType websites in the form of-\n'www.XYZ.com'\nor select a site from the list\n(CLEAR AND CONTINUE)")
site_name.tag_configure("center",justify="center")
site_name.tag_add("center",1.0,END)

#Enter_Website_Dropdown
def insert():
    site_name.insert(END,variable.get())
    site_name.insert(END,"\n")
    variable.set("Suggested Sites")

options=["www.youtube.com","www.entrar.in","www.instagram.com","www.reddit.com","www.discord.com","www.facebook.com"]
variable=StringVar(root,"Suggested Sites")

menu=OptionMenu(root,variable,*options)
menu.config(bg="#b2dff3")
menu.place(relx=0.8,rely=0.29,anchor=CENTER)
menu["menu"].config(font="Sylfaen 11")
Button(root,text="Add to List",command=insert,borderwidth=3,relief="raised",bg="#b2dff3").place(relx=0.81,rely=0.345,anchor=CENTER)

#Bloxite_SAVE&CLEAR_Buttons
WEBSITES=[]
def save():
    
    WEBSITES.append(site_name.get(1.0,END))
    
    Label(root,text="Sites have been saved!",font=('Helvetica 11 italic'),bg="#b2dff3").place(relx=0.80,rely=0.485,anchor=CENTER)
    
def clear():
    site_name.delete(1.0,END)

    
SAVE=Button(root,text="SAVE",command=save,borderwidth=1,bg="#b2dff3",fg="black",font="Calibri 11 bold").place(relx=0.75,rely=0.435,anchor=CENTER)
CLEAR=Button(root,text="CLEAR",command=clear,borderwidth=1,bg="#b2dff3",fg="black",font="Calibri 11 bold").place(relx=0.85,rely=0.435,anchor=CENTER)

#time_input
def ProperTime (time):
    if int(time)//100 >12:
        proper= str((int(time)//100)-12) + ":" + str(int(time)%100)+"pm"
    else:
        proper=str(int(time)//100)+":"+str(int(time)%100)+"am"
    temp_list=list(proper)
    colon=temp_list.index(":")
    if (list(proper)[colon+1]).isdigit() and (list(proper)[colon+2]).isdigit():
        return(proper)
    else:
        temp_list.insert(colon+1,"0")
        proper=''.join(temp_list)
        return(proper)

#Blocking,Pop_Up,Confirmation


def enter():
     Start_Time=start_time.get()
     End_Time=end_time.get()
     def popup():
         response=messagebox.askyesno("Confirmation","Are you sure you want to block these sites from\n"+ProperTime(Start_Time)+" to "+ProperTime(End_Time)+"?")
         if response==1:
             Bloxite(End_Time, Start_Time,WEBSITES)
             tk.Label(root,text = 'Websites Have Been Succesfully Blocked! from '+ProperTime(Start_Time)+" to "+ProperTime(End_Time),bg="#b2dff3",font=('calibre',11, 'bold'),justify=CENTER).place(relx=0.50,rely=0.90,anchor=CENTER)
         else:
             breakpoint
     popup()
     start_time.set("")
     end_time.set("")
     
def Bloxite(End_Time,Start_Time,WEBSITES):
    websites=WEBSITES[0].split('\n')[0:-2]
    
    End=datetime(y,m,d,int(End_Time)//100,int(End_Time)%100)
    Start=datetime(y,m,d,int(Start_Time)//100,int(Start_Time)%100)
    if datetime.now() < End and datetime.now()>Start : 
        print("Blocking sites")
        with open(hosts_path, 'r+') as hostfile:
            hosts_content = hostfile.read()
            for site in  websites:
                
                if site not in hosts_content:
                   hostfile.write(redirect + ' ' + site)
                   hostfile.write("\n")
    else:
        Unblock(websites)
def Unblock(websites):
    print('Unblocking sites')
    with open(hosts_path, 'r+') as hostfile:
        lines = hostfile.readlines()
        hostfile.seek(0)
        for line in lines:
            if not any(site in line for site in websites):
                hostfile.write(line)
        hostfile.truncate()
    
        
    
        

#Time Variables
start_time=tk.StringVar()
end_time=tk.StringVar()

#Time and Block Buttons
example=StringVar()
example.set(" Input time in 24hr format without ':', 1830 for 06:30PM")
example_label= tk.Label(root,text="Example:",bg="#b2dff3",font=('calibre',11, 'bold')).place(relx=0.12,rely=0.60,anchor=CENTER)
example_label_entry = tk.Entry(root,textvariable=example,width=47,state=DISABLED,bg="#b2dff3",font=('calibre',11, 'bold')).place(relx=0.58,rely=0.60,anchor=CENTER)
start_time_label = tk.Label(root, text = 'Start Time:',bg="#b2dff3", font=('calibre',10, 'bold')).place(relx=0.375,rely=0.67,anchor=CENTER)
start_time_entry = tk.Entry(root,textvariable = start_time,bg="#b2dff3", font=('calibre',10,'normal')).place(relx=0.65,rely=0.67,anchor=CENTER)
end_time_label = tk.Label(root, text = ' End Time: ', bg="#b2dff3",font = ('calibre',10,'bold')).place(relx=0.375,rely=0.72,anchor=CENTER)
end_time_entry=tk.Entry(root, textvariable = end_time,bg="#b2dff3", font = ('calibre',10,'normal')).place(relx=0.65,rely=0.72,anchor=CENTER)
enter_button=tk.Button(root,text = 'BLOCK', command = enter,width=8,bg="#b2dff3",font=('calibre',15,'bold')).place(relx=0.50,rely=0.80,anchor=CENTER)

root.mainloop()
