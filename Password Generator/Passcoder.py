import customtkinter
import random
import string
import tkinter.messagebox
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

def slider(value):
    length = int(passSlider.get())
    passlengthLB.configure(text=length)
    
    characters = string.ascii_letters + string.digits + string.punctuation
    passCode = ''.join(random.choice(characters) for _ in range(length))
    passwordField.delete(0, "end")  # Clear the current content
    passwordField.insert(0, passCode)  # Insert the generated password

def refresh_button_clicked():
    if not(passwordField.get()):
        tkinter.messagebox.showerror("Error", "Select password length")
        print("pick a length")
    else:
        length = int(passSlider.get())
        characters = string.ascii_letters + string.digits + string.punctuation
        passCode = ''.join(random.choice(characters) for _ in range(length))
        passwordField.delete(0, "end")  # Clear the current content
        passwordField.insert(0, passCode)  # Insert the new generated password

def save():
    if not(Linkinput.get()):
        tkinter.messagebox.showerror("Error", "Link not provided")
    
    else:
        f = open("Passwords.txt", "a")
        f.write("Link: "+Linkinput.get()+"||"+"Password: "+passwordField.get()+"\n")
        f.close()

        #open and read the file after the appending:
        f = open("Passwords.txt", "r")
        print(f.read())

ui = customtkinter.CTk()
ui.geometry("400x500+700+100")
ui.title("PassCoder")


HeaderLB = customtkinter.CTkLabel(master=ui,text="Genarate", font=("Bold", 40))
HeaderLB.pack(pady = 50)

passwordLB = customtkinter.CTkLabel(master=ui,text="Password Length: ", font=("Roboto", 16))
passwordLB.pack()

passlengthLB = customtkinter.CTkLabel(master=ui,text="", font=("Roboto", 20))
passlengthLB.pack(pady = 5)

passSlider = customtkinter.CTkSlider(ui, from_=8, to=40, number_of_steps=4, command=slider)
passSlider.set(8)
passSlider.pack(pady = 20)

passwordField = customtkinter.CTkEntry(master=ui, font=("Roboto", 20), height=30, width=340)
passwordField.configure(justify = "center")
passwordField.pack(pady = 10)

link = str()
Linkinput = customtkinter.CTkEntry(master=ui, placeholder_text="Link", textvariable=link, font=("Roboto", 20), height=30, width=340)
Linkinput.configure(justify = "center")
Linkinput.pack(pady = 5)

refreshBtn = customtkinter.CTkButton(master=ui, text="refresh", font=("Roboto", 20), height=10, width=80, command = refresh_button_clicked)
refreshBtn.pack(pady = 15)

saveBtn = customtkinter.CTkButton(master=ui, text="Save", font=("Roboto", 20), height=10, width=80, command = save)
saveBtn.pack(pady = 5)


ui.mainloop()