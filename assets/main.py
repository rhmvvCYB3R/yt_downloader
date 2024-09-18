import customtkinter
import pytube

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


app = customtkinter.CTk()
app.title("YT DOWNLOADER")
app.iconbitmap("public/images/app.ico")
app.geometry("720x480")
app.resizable(False,False)

link_entry = customtkinter.CTkEntry(app,width=400,height=35)
link_entry.place(x=80,y=50)

search_btn = customtkinter.CTkButton(app,text="Искать")
search_btn.place(x=510,y=53)


app.mainloop()