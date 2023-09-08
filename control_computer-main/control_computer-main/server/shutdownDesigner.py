import tkinter as tk
from tkinter import messagebox
import time
import threading
import os

class ShutdownApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shutdown Countdown")
        self.root.geometry("350x300")  # Đặt kích thước cửa sổ
        
        self.title_label = tk.Label(root, text="Đếm ngược đến khi tắt máy", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=10)
        
        self.message_label = tk.Label(root, text="Máy tính sẽ tắt sau:", font=("Helvetica", 12))
        self.message_label.pack()
        
        self.countdown_label = tk.Label(root, text="", font=("Helvetica", 24, "bold"))
        self.countdown_label.pack()
        
        self.legend_frame = tk.LabelFrame(root, text="Message", font=("Helvetica", 10, "bold"), bg="#F0F0F0", padx=10, pady=5)
        self.legend_frame.pack(padx=10, pady=10, fill="both", expand=True)
        
        self.warning_message = tk.Label(self.legend_frame, text="Hãy lưu tất cả công việc quan trọng trước khi tiến hành tắt máy!", font=("Helvetica", 10), fg="red", wraplength=280, justify="left")
        self.warning_message.pack(anchor="w")
        
        self.countdown_thread = threading.Thread(target=self.update_countdown)
        self.countdown_thread.start()
        
    def update_countdown(self):
        seconds_left = 5
        
        while seconds_left > 0:
            hours = seconds_left // 3600
            minutes = (seconds_left % 3600) // 60
            seconds = seconds_left % 60
            time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            self.countdown_label.config(text=time_str)
            time.sleep(1)
            seconds_left -= 1

        self.perform_shutdown()
        
    def perform_shutdown(self):
        messagebox.showinfo("Thông báo", "Máy tính sẽ tắt ngay bây giờ!")
        os.system("shutdown /s /f /t 1")  # Lệnh để tắt máy ngay lập tức

def open_shutdown_app():
    root = tk.Toplevel()
    root.configure(bg="#EFEFEF")  # Đặt màu nền cho cửa sổ
    app = ShutdownApp(root)
    root.mainloop()