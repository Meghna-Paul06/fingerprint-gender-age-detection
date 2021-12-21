import sys
import os
import PIL
from PIL import ImageTk,Image  
import tkinter
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
import centroid
import main
import knn

values={}
top=tkinter.Tk()
top.geometry('800x800')
def load():
    imgname.configure(text="")
    preprocess_img.configure(image="")
    preprocess_label.configure(text="")
    values['filename'] = filedialog.askopenfilename()#(filetypes=[("Jpeg","*.jpg")])
    x=values['filename']
    im=PIL.Image.open(x)
    fp_img = ImageTk.PhotoImage(im)  
    load_img.configure(image=fp_img)
    load_img.image=fp_img
    load_img.place(x=200,y=200)
    imgname.place(x=100,y=450)
    imgname.configure(text=x)
    messagebox.showinfo("Image load", "Image loaded successfully!!")
    
def extract():
    if(load_img.cget('image')==""):
        messagebox.showwarning("Warning", "No Image loaded for preprocessing !")
    else:
        a,b,c,d,e=centroid.centroid(values['filename'])
        x='plot.png'
        im=PIL.Image.open(x)
        fp_img = ImageTk.PhotoImage(im)  
        preprocess_img.configure(image=fp_img)
        preprocess_img.image=fp_img
        preprocess_img.place(x=700,y=50)
        preprocess_label.place(x=1000,y=550)
        preprocess_label.configure(text="Scatter plot")
        messagebox.showinfo("Extraction", "Feature Extraction done!!")

def predict():
    if(preprocess_img.cget('image')==""):
        messagebox.showinfo("Warning", "Preprocess the image first !")
    else:
        values['gender','age']=knn.knn(values['filename'])
        g,a=values['gender','age']
        string="Gender: "+g+"\nAge: "+a
        messagebox.showinfo("Prediction", string)
            
def exit_win():
    top.destroy()
    sys.exit()
    
Label(top,text="GENDER AND AGE PREDICTION ",font=('Times New Roman',21,'bold')).place(x=450)
#img=Label(top)
#img.pack(fill=X)
load_img=Label(top)
imgname=Label(top)
preprocess_img=Label(top)
preprocess_label=Label(top)
tkinter.Button(top,text="Load Image",font=('Times New Roman',11,'bold'),command=load).place(width=100,height=50, x=450,y=600)
tkinter.Button(top,text="Extract",font=('Times New Roman',11,'bold'),command= extract).place(width=100,height=50, x=550,y=600)
tkinter.Button(top,text="Predict",font=('Times New Roman',11,'bold'),command=predict).place(width=100,height=50, x=650,y=600)
tkinter.Button(top,text="Exit",font=('Times New Roman',11,'bold'),command=exit_win).place(width=100,height=50, x=750,y=600)
top.mainloop()
