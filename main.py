from tkinter import *
global count
count =0
class kronometre():
    def reset(self):
        global count
        count=1
        self.t.set('00:00:00')        
    def start(self):
        global count
        count=0
        self.timer()   
    def stop(self):
        global count
        count=1
    def close(self):
        self.root.destroy()
    def timer(self):
        global count
        if(count==0):
            self.d = str(self.t.get())
            h,m,s = map(int,self.d.split(":")) 
            h = int(h)
            m=int(m)
            s= int(s)
            if(s<59):
                s+=1
            elif(s==59):
                s=0
                if(m<59):
                    m+=1
                elif(m==59):
                    m=0
                    h+=1
            if(h<10):
                h = str(0)+str(h)
            else:
                h= str(h)
            if(m<10):
                m = str(0)+str(m)
            else:
                m = str(m)
            if(s<10):
                s=str(0)+str(s)
            else:
                s=str(s)
            self.d=h+":"+m+":"+s           
            self.t.set(self.d)
            if(count==0):
                self.root.after(1000,self.timer)     
    def __init__(self):
        self.root=Tk()
        self.root.title("Kronometre")
        self.root.geometry("250x200")
        self.t = StringVar()
        self.t.set("00:00:00")
        self.lb = Label(self.root,textvariable=self.t,font=("Times 40 bold"),bg="white")
        self.bt1 = Button(self.root,text="       Başla       ",command=self.start,font=("Times 10 bold"),bg=("gray"))
        self.bt2 = Button(self.root,text="      Duraklat      ",command=self.stop,font=("Times 10 bold"),bg=("gray"))
        self.bt3 = Button(self.root,text="       Sıfırla      ",command=self.reset,font=("Times 10 bold"),bg=("gray"))
        self.bt4 = Button(self.root, text="         Çıkış         ", command=self.close,font=("Times 10 bold"),bg=("gray"))
        self.lb.place(x=20,y=10)
        self.bt1.place(x=10,y=100)
        self.bt2.place(x=120,y=100)
        self.bt3.place(x=10,y=142)
        self.bt4.place(x=120,y=142)
        self.label = Label(self.root,text="",font=("Times 40 bold"))
        self.root.configure(bg='white')
        self.root.mainloop()
a=kronometre()      