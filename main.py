from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=APIkey").json()
    if 'weather' in data:
        w_label1.config(text=data["weather"][0]["main"])
        wb_label1.config(text=data["weather"][0]["description"])
    if 'main' in data:
        t_label1.config(text=str(round(float(data["main"]["temp"]-273.15), 2))+" °C")
        p_label1.config(text=str(data["main"]["pressure"])+" bar")


win = Tk()
win.title("Caerus app")
win.config(bg="black")
win.geometry("500x600")

name_label = Label(win, text="Caerus The Weather App", font=("Time New Roman", 28, "bold"))
name_label.place(x=25, y=25, height=50, width=450)

list_name = ["Andhra Pradesh", "Arunachal Pradesh ", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat",
             "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh",
             "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim",
             "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal",
             "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep",
             "National Capital Territory of Delhi", "Puducherry"]

city_name = StringVar()
com = ttk.Combobox(win, text="Caerus The Weather App", values=list_name, font=("Times New Roman", 25, "bold"), textvariable=city_name)
com.place(x=50, y=120, height=50, width=400)

w_label = Label(win, text="Weather Climate", font=("Time New Roman", 18, "bold"))
w_label.place(x=25, y=260, height=50, width=210)
w_label1 = Label(win, text="", font=("Time New Roman", 18, "bold"))
w_label1.place(x=250, y=260, height=50, width=210)

wb_label = Label(win, text="Weather Description", font=("Time New Roman", 16, "bold"))
wb_label.place(x=25, y=330, height=50, width=210)
wb_label1 = Label(win, text="", font=("Time New Roman", 18, "bold"))
wb_label1.place(x=250, y=330, height=50, width=210)

t_label = Label(win, text="Temperature ", font=("Time New Roman", 18, "bold"))
t_label.place(x=25, y=400, height=50, width=210)
t_label1 = Label(win, text="", font=("Time New Roman", 18, "bold"))
t_label1.place(x=250, y=400, height=50, width=210)

p_label = Label(win, text="Pressure", font=("Time New Roman", 18, "bold"))
p_label.place(x=25, y=470, height=50, width=210)
p_label1 = Label(win, text="", font=("Time New Roman", 18, "bold"))
p_label1.place(x=250, y=470, height=50, width=210)


find_button = Button(win, text="Find", font=("Time New Roman", 20, "bold", "italic"),command=data_get)
find_button.place(x=200, y=200, height=25, width=100)

end_label = Label(win, text="Thanks for using this App", font=("Time New Roman", 25, "bold"), fg= "yellow", background="black")
end_label.place(x=25, y=530, height=50, width=450)


win.mainloop()
