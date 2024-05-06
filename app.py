import tkinter as tk
import requests

def get_weather():
    city = entry.get()
    api_key = '3dec4a61ebcbd13b0886e0b1b9a1ce2b'  # Replace 'API_KEY' with your actual API key which you can get from api.openweathermap.org
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    weather_data = response.json()

    if weather_data['cod'] != '404':
        weather_info = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        result_label.config(text=f'Weather Info: {weather_info}\nTemperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s')
    else:
        result_label.config(text='City not found')

app = tk.Tk()
app.title('Weather App')
app.geometry('400x300')  # Set window size

title_label = tk.Label(app, text='Enter City:', font=('Arial', 14, 'bold'))
title_label.pack(pady=10)

entry = tk.Entry(app, font=('Arial', 12))
entry.pack()

button = tk.Button(app, text='Get Weather', command=get_weather, font=('Arial', 12))
button.pack(pady=10)

result_label = tk.Label(app, text='', font=('Arial', 12), wraplength=380, justify='left')
result_label.pack(padx=10, pady=20)

app.mainloop()
