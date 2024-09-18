import customtkinter
import pytube

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


app = customtkinter.CTk()
app.title("YT DOWNLOADER")
app.iconbitmap("public/images/app.ico")
app.geometry("720x480")
app.resizable(False,False)

text_label = customtkinter.CTkLabel(app,text="Youtube Video Downloader",font=("Compact",35),text_color="red")
text_label.place(x=150,y=20)

def clear_link_entry(event):
    if link_entry.get() == "Вставьте ссылку на видео! ":
        link_entry.delete(0, "end")
     

link_entry = customtkinter.CTkEntry(app,width=400,height=35,font=("Compact" , 14),text_color="blue")
link_entry.insert(0,"Вставьте ссылку на видео! ")
link_entry.place(x=80,y=110)
link_entry.bind("<FocusIn>",clear_link_entry)


search_btn = customtkinter.CTkButton(app,text="Искать")
search_btn.place(x=510,y=113)


app.mainloop()