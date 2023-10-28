import tkinter as tk
from tkinter import messagebox
from gtts import gTTS
import os

output_count = 0

def download_audio():
    global output_count
    text = text_box.get("1.0", "end-1c")
    if text:
        tts = gTTS(text)
        output_count += 1
        save_path = f"output{output_count}.mp3"

        if os.path.isfile(save_path):
            messagebox.showinfo("Download Audio", "You cannot download the same file twice!")
        else:
            tts.save(save_path)
            messagebox.showinfo("Download Audio", f"Audio saved as {save_path}")

window = tk.Tk()
window.title("Text-to-Speech Converter")

text_box = tk.Text(window, height=10, width=40)
text_box.pack()

download_button = tk.Button(window, text="Download Audio (MP3)", command=download_audio)
download_button.pack()

window.mainloop()
