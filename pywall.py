from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import socket  #importing library
import re
from PIL import ImageTk, Image
import platform
main = Tk()
width= main.winfo_screenwidth()
height= main.winfo_screenheight()
#setting tkinter window size

main.geometry("%dx%d" % (width, height))


#deletes everything
def allclear():
    for widget in main.winfo_children():
                                        widget.destroy()
 
 
 
 
#core objects                                       
main.title("FIREWALL")
listofopen=[]
namelessopen=[]
Blacklist=[]
main.frame()
blackip=[]
ip = socket.gethostbyname (socket.gethostname())
table_data=[]

#checks ip syntax
def validate_ip_address(address):
    match = re.match(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", address)

    if bool(match) is False:

        raise ValueError

    for part in address.split("."):
        if int(part) < 0 or int(part) > 255:

            raise ValueError

    return address

#blocks ip
def ip_blocker(ip):
    global blackip
    if ip in blackip:
        return "Already blocked"
    else:
        blackip.append(ip)
        return "ip blocked Successfully"
#unblocks ip
def ip_unblocker(ip):
    global blackip
    if ip in blackip:

        blackip.pop(blackip.index(ip))
        return "unblocked Successfully"


    else:
        return "ip Not blocked"
#ip blocking widget
def ip_widg():
     global blackip
     allclear()
     allwhite()
     tk.Label(main, text="""Blocage de IP:""",justify = tk.LEFT,padx = 20,background="#9ce0ff",font="arial").pack()

     l = Label(main, text = "Liste des adresse Ip bloquès:",background="#9ce0ff")

     l.place(x=60, y=80)
     T = Text(main, height = 30, width = 40)
     T.config(state=DISABLED)
     T.place(x=50, y=100)

     l1 = Label(main, text = "Entre IP:",background="#9ce0ff")
     l1.place(x=200, y=20)
     T1 = Text(main, height = 2, width = 15)
     T1.place(x=200, y=50)
     def blocked_ip():
         global blackip

         for x in range(len(blackip)):
             s=blackip[x]
             print(s)
             T.config(state= NORMAL)
             s=str(s)+"\n"
             T.insert(tk.END,s) 
         T.config(state= DISABLED)
         
         
         
     blocked_ip()
     def ip_getter():
         global blackip

         try:

             Target=(T1.get("1.0",END))
             a=validate_ip_address(Target)

             print(a)
             messagebox.showinfo("Success", ip_blocker(a))
             T.config(state= NORMAL)


             T.delete('1.0', tk.END)
             blocked_ip()

         except:
                  messagebox.showinfo("Value Error", "Not a valid Ip adresse")

     def ip_free():
         global blackip


         try:
             T.config(state= NORMAL)


             T.delete('1.0', tk.END)
             Target=(T1.get("1.0",END))
             a=validate_ip_address(Target)

             messagebox.showinfo("Success", ip_unblocker(a))
             blocked_ip()

         except:
            messagebox.showinfo("Value Error", "Not a valid Ip adresse")

            # Target=(T1.get("1.0",END))
            # messagebox.showinfo("Success", ip_unblocker(Target))
     b3 = Button(main, text = "Block ",command=ip_getter )
     b3.place(x=300, y=20)
     b3 = Button(main, text = "UnBlock ",command=ip_free )
     b3.place(x=370, y=20)
     b5 = Button(main, text = "Menu principal",width=20,command=acceuil,background="white",font="arial"  )
     b5.place(x=600, y=650)
     b6 = Button(main, text = "Quitter",command = main.destroy,font="Arial")
     b6.place(x=900, y=650)



#ports blocking widget
def BlockingPorts():
                global currentLine,listofopen,namelessopen,Blacklist,l
                allclear()
                allwhite()
                
                b6 = Button(main, text = "Quitter",command = main.destroy,font="Arial")
                b6.place(x=900, y=650)

                l = Label(main, text = "Entrer le nombre de Port:" ,background="#9ce0ff")

                T = Text(main, height = 2, width = 15)
                T1 = Text(main, height = 30, width = 40)
                T1.place(x=400,y=70)
                T1.config(state=DISABLED)
                l1=Label(main, text = "Ports Bloqués :",background="#9ce0ff")
                l1.place(x=400,y=50)
                l3 = Label(main, text = "de:",background="#9ce0ff")
                l4 = Label(main, text = "à:",background="#9ce0ff")
                T3 = Text(main, height = 2, width = 8)
                T4 = Text(main, height = 2, width = 8)
                T1.config(state=NORMAL)

                for x in range(len(Blacklist)):
                                                             s=Blacklist[x]
                                                             s=str(s)+"\n"
                                                             T1.insert(tk.END,s) 
                                                             main.update()

                T1.config(state=DISABLED)

                v = tk.IntVar()
                
                v.set(1)  # initializing the choice, i.e. Python
                
                choices= [("Bloquer un Port" , 101), ("Bloquer plusieurs Ports:", 102) ]

                def ShowChoice():
                        global currentLine,listofopen,namelessopen
                        b1 = Button(main, text = "Bloquer",command=Blocker )
                        b1.place(x=60, y=200)


                        if v.get()==101:
                            l3.place(anchor="nw", x=0, y=0, width=0, height=0)
                            T3.place(anchor="nw", x=0, y=0, width=0, height=0)
                            l4.place(anchor="nw", x=0, y=0, width=0, height=0)
                            T4.place(anchor="nw", x=0, y=0, width=0, height=0)
                            

                            l.place(x=20, y=80,height = 50, width = 130)
                            T.place(x=180, y=80,height = 30, width = 80)
                            b1 = Button(main, text = "Bloquer",command=Blocker )
                            b1.place(x=60, y=200)
                            
                        elif v.get()==102:
                            l.place(anchor="nw", x=0, y=0, width=0, height=0)
                            T.place(anchor="nw", x=0, y=0, width=0, height=0)

                            l3.place(x=20, y=80,height = 30, width = 30)
                            T3.place(x=80, y=80,height = 30, width = 80)
                            l4.place(x=170, y=80,height = 30, width = 30)
                            T4.place(x=190, y=80,height = 30, width = 80)
                            b1 = Button(main, text = "Bloquer",command=Blockerplage )
                            b1.place(x=60, y=200)
                def Blocker():
                                    # T.insert(tk.END, T)
                                    try:
                                       pr=int(  T.get("1.0",END))
                                       if pr<0 or pr>65535:
                                           messagebox.showinfo("Invalid Port", "Port Must be Between 0 and 65535")
                                           T.delete(1.0,END)

                                       else:
                                           T1.config(state= NORMAL)
                                           T1.delete('1.0', tk.END)
                                           if pr not in Blacklist and pr in listofopen:
                                                Blacklist.append(pr)
                                                open_ports()
                                                T.delete(1.0,END)
                                                for x in range(len(Blacklist)):
                                                             s=Blacklist[x]
                                                             s=str(s)+"\n"
                                                             T1.insert(tk.END,s) 
                                                             main.update()



                                                messagebox.showinfo("Success", "Port blocked Successfully!")
                                           elif pr  in Blacklist and pr not in listofopen:
                                                messagebox.showinfo("Success", "Port is already Blocked!")
                                                for x in range(len(Blacklist)):
                                                             s=Blacklist[x]
                                                             s=str(s)+"\n"
                                                             T1.insert(tk.END,s) 
                                                             main.update()

                                                T.delete(1.0,END)
                                           elif pr not in Blacklist:
                                                     T.delete(1.0,END)
                                                     Blacklist.append(pr)
                                                     messagebox.showinfo("Success", "Port blocked Successfully!")
                                                     for x in range(len(Blacklist)):
                                                             s=Blacklist[x]
                                                             s=str(s)+"\n"
                                                             T1.insert(tk.END,s) 
                                                             main.update()


                                    except:
                                             T.delete(1.0,END)
                                             for x in range(len(Blacklist)):
                                                             s=Blacklist[x]
                                                             s=str(s)+"\n"
                                                             T1.insert(tk.END,s) 
                                                             main.update()


                                             messagebox.showinfo("Type Error", "Digits Only!")
                                    T1.config(state=DISABLED)
                def Blockerplage():
                                    # T.insert(tk.END, T)


                                    try:
                                       pr=int(  T3.get("1.0",END))
                                       prh=int(  T4.get("1.0",END))
                                       if (pr<0 or pr>65535) and (prh<0 or prh>65535) or pr>prh  :
                                           messagebox.showinfo("Invalid Port", "Port Must be Between 0 and 65535")
                                           T.delete(1.0,END)

                                       else:
                                           T1.config(state= NORMAL)
                                           T1.delete('1.0', tk.END)
                                           if pr not in Blacklist and pr in listofopen and prh not in Blacklist and prh in listofopen:
                                                for i in range(pr,prh+1):
                                                    if i not in Blacklist:
                                                                    Blacklist.append(i)
                                                open_ports()
                                                T3.delete(1.0,END)
                                                T4.delete(1.0,END)

                                                for x in range(len(Blacklist)):
                                                             s=Blacklist[x]
                                                             s=str(s)+"\n"
                                                             T1.insert(tk.END,s) 
                                                             main.update()

                                           elif pr not in Blacklist and prh not in Blacklist :
                                                     for i in range(pr,prh+1):
                                                         if i not in Blacklist:
                                                                    Blacklist.append(i)

                                                             
                                                     T3.delete(1.0,END)
                                                     T4.delete(1.0,END)

                                                     messagebox.showinfo("Success", "PortS blocked Successfully!")
                                                     for x in range(len(Blacklist)):
                                                             s=Blacklist[x]
                                                             s=str(s)+"\n"
                                                             T1.insert(tk.END,s) 
                                                             main.update()


                                    except:
                                             T3.delete(1.0,END)
                                             T4.delete(1.0,END)

                                             for x in range(len(Blacklist)):
                                                             s=Blacklist[x]
                                                             s=str(s)+"\n"
                                                             T1.insert(tk.END,s) 
                                                             main.update()


                                             messagebox.showinfo("Type Error", "Digits Only!")
                                    T1.config(state=DISABLED)                
                ShowChoice()

                tk.Label(main, text="""Blocage des Ports:""",justify = tk.LEFT,padx = 20,background="#9ce0ff",font="arial").pack()

                for choices, val in choices:tk.Radiobutton(main, text=choices,padx = 20, variable=v, command=ShowChoice,value=val,background="#9ce0ff").pack(anchor=tk.W)

                b3 = Button(main, text = "Menu principal",width=20,command=acceuil,background="white",font="arial" )
                b3.place(x=600, y=650)
                main.update()


#open ports object
def open_ports(a=0,b=65536):
        global currentLine,listofopen,namelessopen
        open=[]
        for port in range(a,b):      

            try:

                serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
                serv.bind((ip,port))
            except:

                try:
                        if port in Blacklist and port in listofopen:
                              listofopen.pop(listofopen.index(port))

                              serv.close()
                        else:

                           r= str(port)+" "+socket.getservbyport(port, "TCP")+"\n"

                           if port not in listofopen and port not in Blacklist:
                                    listofopen.append(port)

                except:
                        if port not in namelessopen :

                              namelessopen.append(port)

        # for i in open:
        #     listofopen.append(i)
        #     try:
        #        listofopen.append((socket.getservbyport(i, "tcp")))


        #     except:

        #       continue
        # listofopen=open
        serv.close() #close connection
        x='\n'.join([str(e) for e in open])
        return x

op=open_ports()
currentLine=0


#open ports widget
def PorteScan():
            global currentLine,listofopen,namelessopen
            allclear()
            allwhite()

            def write():
                            T.config(state= NORMAL)

                            global currentLine,listofopen,namelessopen
                            for i in range(len(listofopen)):
                                por=listofopen[i]
                                r= str(por)+" "+socket.getservbyport(por, "TCP")+" est ouvert \n"

                                T.insert(tk.END,r) 
                                main.update()
                            for i in range(len(namelessopen)):
                                por=namelessopen[i]


                                r=str(por)+" name unavailable est ouvert \n"

                                T.insert(tk.END,r) 
                                main.update()

            b3 = Button(main, width=20,text = "Menu principal",command=acceuil,background="white",font="arial" )
            b3.place(x=600, y=650)
            def refresh():
                T.config(state= NORMAL)
                T.delete('1.0', tk.END)
                main.update()
                open_ports()
                write()
                
                
                # messagebox.showinfo("showinfo", "Refreshed Successfully")

                T.config(state= DISABLED)

            # Create text widget and specify size.
            T = Text(main, height = 30, width = 52)
            T.config(state= DISABLED)


            tk.Label(main, text="""Scan des Ports:""",justify = tk.LEFT,padx = 20,background="#9ce0ff",font="arial").pack()

            # Create label
            l = Label(main, text = "Liste des ports ouverts:",background="#9ce0ff")


            # Create button for next text.
            b1 = Button(main, text = "Démarrer",command=refresh )

            # Create an Exit button.
            b2 = Button(main, text = "Quitter",command = main.destroy,font="arial")

            l.place(x=70, y=65)
            T.place(x=50, y=100)
            b1.place(x=50, y=600)
            b2.place(x=900, y=650)
            write()
            main.update()
            
            
            
            
#packet filtering widget
def filter_table():                         
                                global tablecount
                                tablecount=0
                                allclear()
                                allwhite()
                                tk.Label(main, text="""Filtrage des Paquets:""",justify = tk.LEFT,padx = 20,background="#9ce0ff",font="arial").pack()
                                textlab=["Adresse destination inferieur","Adresse destination superieur","Adresse source inferieur","Adesse source superieur","Port source inferieur","Port source superieur","Port Destinataire inferieur","Port Destinataire superieur","Protocole"]
                                table = ttk.Treeview(main)
                                table.place_configure(width=1400)
                                table["columns"]=("zer","one","two","three","four","five","six","seven","eight","nine")
                                table.heading("#0",text="")
                                table.heading("zer", text="Action")
                                table.heading("one", text="Adresse destination inferieur")
                                table.heading("two", text="Adresse destination superieur")
                                table.heading("three", text="Adresse source inferieur")
                                table.heading("four", text="Adesse source superieur")
                                table.heading("five", text="Port source inferieur")
                                table.heading("six", text="Port source superieur")
                                table.heading("seven", text="Port Destinataire inferieur")
                                table.heading("eight", text="Port Destinataire superieur")
                                table.heading("nine", text="Protocole")
                                table.column("#0", width=0, minwidth=0)
                                table.column("zer", width=30, minwidth=30)
                                table.column("one", width=90, minwidth=90)
                                table.column("two", width=90, minwidth=50)
                                table.column("three", width=90, minwidth=50)
                                table.column("four", width=90, minwidth=50)
                                table.column("five", width=90, minwidth=50)
                                table.column("six", width=90, minwidth=50)
                                table.column("seven", width=90, minwidth=50)
                                table.column("eight", width=90, minwidth=50)
                                table.column("nine", width=25, minwidth=25)
                                
                               

                                table.place(x=30,y=300)

                                # Create entry widgets for the Name, Age, Gender
                                # l = Label(main, text = "Adresse Destination inferieur:")
                                
                                v = tk.IntVar()
                                v.set(1)
                                v1 = tk.IntVar()
                                v.set(1)
                               
                
                                  # initializing the choice, i.e. Python
                                def rad():
                                    global act
                                    if v.get()==101:
                                        act="Autoriser"
                                    elif  v.get()==102: 
                                                        act="Bloquer"
                                def rad1():
                                    global pt
                                    if v1.get()==101:
                                        pt="TCP"
                                    elif  v1.get()==102: 
                                             pt="UDP"                        
                                    elif  v1.get()==103:  
                                                 pt="Autres"                        
                                                
                                        
                                type = Label(main, text = "Type de Filtrage:",background="#9ce0ff")
                                type.place( x=380,y=10)

                                choices= [("Autoriser" , 101), ("Bloquer", 102) ]
                                padplus=0
                                for choices, val in choices:
                                    tk.Radiobutton(main, text=choices,padx = 410, variable=v, command=rad,value=val,background="#9ce0ff").pack(anchor=tk.W)
                                    



                                type = Label(main, text = "Protocoles:",background="#9ce0ff")
                                type.place( x=380,y=100)

                                choices2= [("TCP" , 101), ("UDP", 102),("Autres",103) ]
                                for choices2, val2 in choices2:
                                    tk.Radiobutton(main, text=choices2, variable=v1, command=rad1,value=val2,background="#9ce0ff").place(x=410,y=120+padplus)
                                    padplus+=20
                                   


                                
                                ipdest_infer_entry = tk.Entry(main)
                                ip_dest_supeentry = tk.Entry(main)
                                ip_src_supeentry = tk.Entry(main)
                                ip_src_inferntry = tk.Entry(main)
                                port_dest_inf = tk.Entry(main)
                                port_dest_spr = tk.Entry(main)
                                port_src_spr= tk.Entry(main)
                                port_src_inf= tk.Entry(main)
                                viewLab=[]
                                yaxis=80
                                for i in range(0,8):
                                     a=Label(main, text = textlab[i] ,background="#9ce0ff")
                                     a.place(x=25,y=yaxis)
                                     viewLab.append(a)
                                     yaxis+=20
                                # Create a button to add the data to the table
                                add_button = tk.Button(main, text="Ajouter", command=lambda: add_data())
                                delete_button = tk.Button(main, text="Supprimer", command=lambda: delete_data())
                                # Function to add the data to the table
                                
                                def add_data():
                                    global tablecount
                                    tablecount+=1
                                    try:
                                        
                                         ipdest_infer_entr =validate_ip_address(ipdest_infer_entry.get())
                                         ip_dest_supeentr = validate_ip_address(ip_dest_supeentry.get())
                                         ip_src_supeentr =validate_ip_address ( ip_src_supeentry.get())
                                         ip_src_inferntr=validate_ip_address (ip_src_inferntry.get())
                                         port_dest_in=  port_dest_inf.get()
                                         port_dest_sp= port_dest_spr.get()
                                         port_src_sp=port_src_spr.get()
                                         port_src_in=port_src_inf.get()
                                    except:
                                            messagebox.showinfo("Value Error", "adresse non valide")
                                   
                                    

                                    table.insert("", "end",text="" ,values=(act,ipdest_infer_entr,ip_dest_supeentr, ip_src_supeentr,ip_src_inferntr,port_dest_in,port_dest_sp,port_src_sp,port_src_in,pt))
                                    data=[act,ipdest_infer_entr,ip_dest_supeentr, ip_src_supeentr,ip_src_inferntr,port_dest_in,port_dest_sp,port_src_sp,port_src_in,pt]
                                    table_data.append(data)
                                

                                # Position the entry widgets and button on the window
                                ipdest_infer_entry.place(x=190,y=80)
                                ip_dest_supeentry.place(x=190,y=100)
                                ip_src_supeentry.place(x=190,y=120)
                                ip_src_inferntry.place(x=190,y=140)
                                port_dest_inf.place(x=190,y=160)
                                port_dest_spr.place(x=190,y=180)
                                port_src_spr.place(x=190,y=200)
                                port_src_inf.place(x=190,y=220)
                                
                                add_button.place(x=190,y=240)

                                def delete_data():
                                        selected_items = table.selection()
                                        for item in selected_items:
                                            table.delete(item)
                                            
                                           
                                delete_button.place(x=30,y=260)
                                b5 = Button(main, text = "Menu principal",width=20,command=acceuil,background="white",font="arial"  )
                                b5.place(x=600, y=650)
                                b6 = Button(main, text = "Quitter",command = main.destroy,font="arial")
                                b6.place(x=900, y=650)
                                if len(table_data)!=0:
                                    for x in table_data:
                                         table.insert("", "end",text="" ,values=x)
                                main.update()           

#windows background
def allwhite():
                                            load = Image.open("res/LOG.png")
                                            render = ImageTk.PhotoImage(load)
                                            img = Label(main, image=render,height=height,width=width)
                                            img.image = render
                                            img.place(x=0, y=0)
 
 
 
 #buttons icon                                           
def icon(src,x1,y1,w,h):
    load = Image.open(src)
    render = ImageTk.PhotoImage(load)
    img = Label(main, image=render,width=w,height=h,background="#9ce0ff")
    img.image = render

    img.place(x=x1, y=y1)
    
                                                
#system info                                            
def sysinfo():
    l = Label(main, text = "Votre Adresse Ip : "+ socket.gethostbyname (socket.gethostname()) +"\nSystem : "+platform.system()+"\nVersion : "+platform.version(),background="#9ce0ff",justify = tk.LEFT,font="arial")    
    l.place(x=1000, y=300)                                      
 
 
 
#credit
def credit():
                 messagebox.showinfo("A propos", "Développé par EL AAOUAM MOHAMED et LAKHDAR ABDERAFIA")
 
 
#main                                             
def acceuil():            
                                allclear()
                                allwhite()
                                sysinfo()
                                tk.Label(main, text="""Menu principal:""",justify = tk.LEFT,padx = 20,background="#9ce0ff",font="arial").pack()

                                b3 = Button(main, text = "Quitter",command = main.destroy ,background="white",font="arial")
                                b3.place(x=900, y=650)

                                b1 = Button(main, text = "Blocage de ports" ,width=20,command=BlockingPorts,background="white", font="arial" )
                                
                                b1.place(x=600+100, y=300)
                                icon("res/red.png",550+100,300,41,45)
                                b2 = Button(main, text = "Scan de ports",command=PorteScan,width=20,background="white",font="arial" )
                                b2.place(x=100+100, y=400)
                                icon("res/server.png",70+100,400,45,49)
                                
                                

                                b4 = Button(main, text = "Blocage de IP",command=ip_widg,width=20,background="white",font="arial"  )
                                b4.place(x=600+100, y=400)
                                icon("res/block.png",550+100,400,41,45)
                                
                                l = Button(main, text = "A propos",command=credit,font="arial")  
                                l.place(x=100, y=600) 



                                b1 = Button(main, text = "Filtre de Packets",width=20,command=filter_table,background="white",font="arial" )
                                b1.place(x=100+100, y=300)
                                icon("res/filters-icon.png",60+100,290,52,62)

                                main.update()


while True :
       acceuil()
       main.mainloop()







