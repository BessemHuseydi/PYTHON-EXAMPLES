import tkinter as tk
import time

def update_time():
    simdiki_zaman = time.strftime('%H:%M:%S')
    saat_etiketi.config(text=simdiki_zaman)
    root.after(1000, update_time)

root = tk.Tk()
root.title("Dijital Saat")

saat_etiketi = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
saat_etiketi.pack(anchor='center')

# update_time fonksiyonunu çağırarak etiketi güncelle
update_time()

# Uygulamayı çalıştır
root.mainloop()
