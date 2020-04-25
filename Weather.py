import tkinter as tk
import requests
from tkinter import font

# window size
Height = 700
Width = 800


root = tk.Tk()


# Pass weather update to App
def get_info(weather):
    try:
        name = weather['name']
        description = weather['weather'][0]['description']
        temp = weather['main']['temp']
        final_str = 'City: %s \nCondition: %s \nTemperature(F): %s' % (name, description, temp)
    except:
        final_str = 'Error getting weather.\nCheck city name and retry.'
    return final_str


# Weather update from Open Weather API
def get_weather(city):
    weather_key = 'cb48279dd78cf2e103e39047d994e802'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()

    label1['text'] = get_info(weather)

# App layout
canvas = tk.Canvas(root, height=Height,width=Width)
canvas.grid()

frame1 = tk.Frame(root, bg='#2D3319', bd=10)
frame1.place(relx=0.05, rely=0.05, relwidth=0.75, relheight=0.1)

button = tk.Button(root, text='Get Weather',bg='#2D3319', command= lambda:get_weather(entry.get()))
button.place(relx=0.75, rely=0.05, relwidth=0.1, relheight=0.1)



entry = tk.Entry(frame1, bg='#D6E5E3')
entry.place(relx=.0, rely=0.0, relwidth=0.9, relheight=1)


txt = tk.Text(root, height=4, width=100, bg='#9FD8CB')
txt.insert(3.0,"Enter name of City")
txt.place(relx=0.27, rely=0.12, relwidth=0.17, relheight=0.05)

frame2 = tk.Frame(root, bg='#517664', bd=10)
frame2.place(relx=0.1, rely=0.2, relwidth=0.65, relheight=0.5)

label1 = tk.Label(frame2,font=('Arial',30))
label1.place(relx=.05, rely=0.05, relwidth=.9, relheight=.9)


root.mainloop()
