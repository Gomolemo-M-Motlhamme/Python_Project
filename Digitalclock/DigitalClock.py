import customtkinter
from time import strftime
from datetime import datetime

customtkinter.set_appearance_mode("dark")

#window
root = customtkinter.CTk()
root.geometry("400x250")
root.title("Digital Clock")

#get time function
def currentTime():
    now = datetime.now()
    time_string = now.strftime("%H:%M:%S %p")
    date_string = now.strftime("%B %d %Y")
    day_String  = now.strftime("%A")

    timeLB.configure(text = "Time: "+time_string)
    dateLB.configure(text = "Date: "+date_string)
    dayLB.configure(text = "Day of the Week: "+day_String)
    timeLB.after(1000, currentTime)

#frame
frame = customtkinter.CTkFrame(master=root)
frame.pack(padx = 20, pady = 20, fill = "both", expand = True)

#widgits
timeLB = customtkinter.CTkLabel(master=frame, font=("Roboto", 24))
timeLB.pack(padx=10, pady=20)

dateLB = customtkinter.CTkLabel(master=frame, font=("Roboto", 24))
dateLB.pack(padx=10, pady=20)

dayLB = customtkinter.CTkLabel(master=frame, font=("Roboto", 24))
dayLB.pack(padx=10, pady=20)

currentTime()

root.mainloop()
