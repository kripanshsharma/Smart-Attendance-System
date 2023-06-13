from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from Developer import Developer
from help_Desk import HelpDesk


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x600+0+0")
        self.root.title("Face Recognition System")

        # first image
        img=Image.open(r"E:\Face Recognition Project\images\Facial.jpg")
        img=img.resize((430,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=430,height=130)

        # second image
        img1=Image.open(r"E:\Face Recognition Project\images\Three face.jpeg")
        img1=img1.resize((430,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=430,y=0,width=430,height=130)

        # third image
        img2=Image.open(r"E:\Face Recognition Project\images\images.jpg")
        img2=img2.resize((430,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=860,y=0,width=430,height=130)
        
        
        # Background image
        img3=Image.open(r"E:\Face Recognition Project\images\bgimg.jpg")
        img3=img3.resize((1300,570),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1300,height=570)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",30,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1300,height=40)

        # time
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(title_lbl,font=('times new roman',10,'bold'),background='white',foreground='blue')
        lbl.place(x=2,y=-7,width=80,height=50)
        time()
        

        #student button
        img4=Image.open(r"E:\Face Recognition Project\images\student.jpg")
        img4=img4.resize((180,160),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=120,y=60,width=180,height=160)

        b1_1=Button(bg_img,text="Students Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=120,y=220,width=180,height=40)


        #face detector button
        img5=Image.open(r"E:\Face Recognition Project\images\face_detector1.jpg")
        img5=img5.resize((180,160),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_recogniton)
        b1.place(x=400,y=60,width=180,height=160)

        b1_1=Button(bg_img,text="Face detector",cursor="hand2",command=self.face_recogniton,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400,y=220,width=180,height=40)

        #attendace button
        img6=Image.open(r"E:\Face Recognition Project\images\attendance.jpg")
        img6=img6.resize((180,160),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=680,y=60,width=180,height=160)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=680,y=220,width=180,height=40)

        #help desk button
        img7=Image.open(r"E:\Face Recognition Project\images\help-desk.jpg")
        img7=img7.resize((180,160),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_Desk)
        b1.place(x=980,y=60,width=180,height=160)

        b1_1=Button(bg_img,text="Help desk",cursor="hand2",command=self.help_Desk,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=980,y=220,width=180,height=40)

        #Train data button
        img8=Image.open(r"E:\Face Recognition Project\images\train.jpg")
        img8=img8.resize((200,160),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,command=self.train_data,cursor="hand2")
        b1.place(x=120,y=290,width=180,height=160)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=120,y=450,width=180,height=40)


        #Photos button
        img9=Image.open(r"E:\Face Recognition Project\images\photos.jpg")
        img9=img9.resize((200,160),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.openimg,)
        b1.place(x=400,y=290,width=180,height=160)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.openimg,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400,y=450,width=180,height=40)
        
        #Developer button
        img10=Image.open(r"E:\Face Recognition Project\images\developer.jpg")
        img10=img10.resize((200,160),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=680,y=290,width=180,height=160)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=680,y=450,width=180,height=40)
        
        
        # Exit button
        img11=Image.open(r"E:\Face Recognition Project\images\exit.jpg")
        img11=img11.resize((200,160),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=980,y=290,width=180,height=160)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=980,y=450,width=180,height=40)


    def openimg(self):
        os.startfile("data")

    
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition System","Are you to exit?",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return
# ===================== Functions Button ========================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    
    def face_recogniton(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

        
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)


    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_Desk(self):
        self.new_window=Toplevel(self.root)
        self.app=HelpDesk(self.new_window)


if __name__ =="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()