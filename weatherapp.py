from tkinter import *
import tkinter as tk
from geopy import Nominatim
from timezonefinder import TimezoneFinder
from tkinter import ttk , messagebox
from datetime import datetime
import requests
import pytz
from PIL import Image,ImageTk


root =Tk()
root.title("Weather app")
root.geometry("900x500+300+200")# 300 refers the postion in x axis and 200 in y axis
root.resizable(False,False) #resizable() method is used to allow Tkinter root window to change it’s size according to the users need as well we can prohibit resizing of the Tkinter window.If we dont want it to rsize then provide 0 or false

def getweather():
    try:
        city=textfield.get()
        geolocator=Nominatim(user_agent='weatherapp')
        location=geolocator.geocode(city)
        # print(location)
        obj=TimezoneFinder()
        result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
        lt=location.latitude
        ltnew=str(lt)
        lo=location.longitude
        lonew=str(lo)
        # print(lt)
        # print(lo)
        
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I : %M %p")
        clock.config(text=current_time)
        name.config(text='CURRENT TIME')

        #weather
        api="https://api.openweathermap.org/data/2.5/weather?lat="+ltnew+"&lon="+lonew+"&appid=6bc7de205dcb97b68e021c43a991e2be"
        json_data=requests.get(api).json()
        # print(json_data)
        condition=json_data['weather'][0]['main']
        description=json_data['weather'][0]['description']
        temp=int(json_data['main']['temp']-273.15)
        pressure=json_data['main']['pressure']
        humidity=json_data['main']['humidity']
        wind=json_data['wind']['speed']


        

        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
    
    except:
        messagebox.showinfo("info","Invalid input")


    
# time
name=Label(root,font=("arial",15,'bold'))
name.place(x=43,y=130)
clock=Label(root,font=("Helvetica",20))
clock.place(x=43,y=160)



image1=Image.open("search.png")

imaag3=ImageTk.PhotoImage(image1)
myimage=Label(image=imaag3)
myimage.place(x=28,y=21)

#icon
icon1=PhotoImage(file='icon.png')
root.iconphoto(True,icon1)

#maintext
textfield=Entry(root,justify="center",width=17,font=('poppins',25,"bold"),bg="#404040",fg="white",bd=0)
textfield.place(x=50,y=40)
textfield.focus()

#searchicon
searchicon=ImageTk.PhotoImage(Image.open('search_icon.png'))
myimage_icon=Button(root,image=searchicon,bd=0,cursor='hand2',bg='#404040',command=getweather)
myimage_icon.place(x=400,y=34)

#weatherlogo
# logo_image=ImageTk.PhotoImage(Image.open('logo.png'))
# logo=Label(root,image=logo_image)
# logo.place(x=210,y=100)
logo_image=PhotoImage(file='logo.png')
logo=Label(root,image=logo_image)
logo.place(x=210,y=100)



#bottom image
frame_image=ImageTk.PhotoImage(Image.open('box.png'))
frame_my_image=Label(root,image=frame_image)
frame_my_image.pack(ipadx=5,ipady=5,side='bottom')

#wind
label1=Label(root,text="WIND",font=("Hhelvetica",15),fg='white',bg="#1ab5ef")
label1.place(x=140,y=400)

#HUMIDIT
label1=Label(root,text="HUMIDITY",font=("Hhelvetica",15),fg='white',bg="#1ab5ef")
label1.place(x=280,y=400) 

#DESCRIPTION
label1=Label(root,text="DESCRIPTION",font=("Hhelvetica",15),fg='white',bg="#1ab5ef")
label1.place(x=460,y=400)

#PRESSURE
label1=Label(root,text="PRESSURE",font=("Hhelvetica",15),fg='white',bg="#1ab5ef")
label1.place(x=670,y=400)  

w=Label(root,text='...',font=('arial',20),bg="#1ab5ef",fg="white")
w.place(x=150,y=430)

h=Label(root,text='...',font=('arial',20),bg="#1ab5ef",fg="white")
h.place(x=314,y=430)

d=Label(root,text='...',font=('arial',20),bg="#1ab5ef",fg="white")
d.place(x=500,y=430)

p=Label(root,text='...',font=('arial',20),bg="#1ab5ef",fg="white")
p.place(x=710,y=430)

#teprature and condition
t=Label(root,font=("arial",70,'bold'),fg='#ee666d')
t.place(x=480,y=150)
c=Label(root,font=('arial',15,'bold'))
c.place(x=480,y=250)



root.mainloop()