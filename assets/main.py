import customtkinter
import yt_dlp
from tkinter import messagebox,filedialog

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
    if video_link.get() == "Вставьте ссылку на видео! ":
        video_link.delete(0, "end")
     

video_link = customtkinter.CTkEntry(app,width=400,height=35,font=("Compact" , 18),text_color="blue")
video_link.insert(0,"Вставьте ссылку на видео! ")
video_link.place(x=80,y=110)
video_link.bind("<FocusIn>",clear_link_entry)

progress_label = customtkinter.CTkLabel(app, text="0% скачано", font=("Compact", 12))
progress_label.place(x=300, y=170)

progress_bar = customtkinter.CTkProgressBar(app, width=400)
progress_bar.place(x=150, y=200)
progress_bar.set(0)


def progress_hook(d):
    if d['status'] == 'downloading':
        total_bytes = d.get('total_bytes', 0)
        downloaded_bytes = d.get('downloaded_bytes', 0)
        if total_bytes > 0:
            percent = downloaded_bytes / total_bytes
            progress_bar.set(percent) 
            progress_label.configure(text=f"{int(percent * 100)}% скачано")



def dwnl_btn_funk():
    download_Directory = filedialog.askdirectory(
            initialdir="YOUR DIRECTORY PATH", title="Save Video")
    if download_Directory:
        ask_user = messagebox.askquestion("Скачать?","Вы уверены что хотите скачать?")
     
        if ask_user == "yes":
            download_path = download_Directory
            Youtube_link = video_link.get()
            
            ydl_opts = {
                'outtmpl': f'{download_path}/%(title)s.%(ext)s',
                'progress_hooks': [progress_hook]
            }
            
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([Youtube_link])
                messagebox.showinfo("Удачно сохранено!", f"Скачано в \n{download_path}")
            except Exception as e:
                messagebox.showerror("Ошибка!", f"Ошибка при загрузке видео: {e}")

dwnl_btn = customtkinter.CTkButton(app,text="СКАЧАТЬ",command= dwnl_btn_funk)
dwnl_btn.place(x=510,y=113)


app.mainloop()  