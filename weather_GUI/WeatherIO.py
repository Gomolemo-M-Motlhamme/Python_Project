import customtkinter
import requests as rs
import datetime as dt
from MyAPI import GetAPI
from tkinter import messagebox

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

api = GetAPI()

app = customtkinter.CTk()
app.title("Weather App")
app.geometry("550x650+700+100")                                                  #GUI size and position

def get_weather():
    city = UserEntry.get()

    baseUrl = "http://api.openweathermap.org/data/2.5/weather?"                 #Get the Base URL
    url = f"{baseUrl}appid={api}&q={city}"                                   #url the take in our input and api key

    try:
        response = rs.get(url)                                                  # retrive info needed
        data = response.json()                                                  # store info in place holder and convet to json

        City = data["name"]

        temp = data["main"]["temp"]
        tempC = round(temp - 273.15)
        tempF = round(tempC * (9/5) + 32)

        feel = data["main"]["feels_like"]
        feelC = round(feel - 273.15)
        feelF = round(feelC * (9/5) + 32)

        humidity = data["main"]["humidity"]
        descrip = data["weather"][0]["description"]

        #set our lb text to our weather info
        citynameLB.configure(text = City)
        HumidLB.configure(text = "Humidity is: " + str(humidity) + "%")
        tempLB.configure(text = "Temperature is: " + str(tempC) + "°C" + " or " + str(tempF) + "F")
        feelLB.configure(text = "Feels liks: " + str(feelC) + "°C" + " or " + str(feelF) + "F")
        weatherLB.configure(text = "Weather: " + descrip)

    except KeyError:
        messagebox.showerror("Error","Invalid city name. Please try again.")


OutterFrame = customtkinter.CTkFrame(master=app)
OutterFrame.pack(padx =15, pady=10, fill = "both", expand = True)

HeadingLB = customtkinter.CTkLabel(master=OutterFrame, text="Today's Weather", font=("Roboto", 40))
HeadingLB.pack(pady=20)

InnerFrame = customtkinter.CTkFrame(master=OutterFrame)
InnerFrame.pack(padx =70, pady=10, fill = "both", expand = True)

citynameLB = customtkinter.CTkLabel(master=InnerFrame,text="", font=("Bold", 30))
citynameLB.pack(pady=15)

HumidLB = customtkinter.CTkLabel(master=InnerFrame,text="", font=("Bold", 20))
HumidLB.pack(pady=15)

tempLB = customtkinter.CTkLabel(master=InnerFrame,text="", font=("Bold", 20))
tempLB.pack(pady=15)

feelLB = customtkinter.CTkLabel(master=InnerFrame,text="", font=("Bold", 20))
feelLB.pack(pady=15)

weatherLB = customtkinter.CTkLabel(master=InnerFrame,text="", font=("Bold", 20))
weatherLB.pack(pady=15)

city_text = str()
UserEntry = customtkinter.CTkEntry(master=OutterFrame, placeholder_text="City", textvariable=city_text, font=("Roboto", 20), height=30, width=350)
UserEntry.configure(justify="center")
UserEntry.pack(padx=10, pady=10, anchor="center")

getWeatherBtn = customtkinter.CTkButton(master=OutterFrame, text="Get Weather", font=("Roboto", 20), height=50, width=200, command=get_weather)
getWeatherBtn.pack(padx =50, pady=10)


app.mainloop()