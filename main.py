# ---------------------------------------------------------
# Just Dance Controller PC - Server Application
# by: MAXZOR
# ---------------------------------------------------------
import tkinter as tk
from tkinter import ttk
import socket
import threading
import http.server
import socketserver
import qrcode
from PIL import Image, ImageTk
import sys
import os

PORT = 8000

TEXTS = {
    'es': { 'title': "JD CONTROLLER", 'subtitle': "by MAXZØR", 'instr': "Escanea con tu celular\npara conectar\n(Utiliza Firefox en Android)", 'running': "Servidor corriendo en puerto" },
    'en': { 'title': "JD CONTROLLER", 'subtitle': "by MAXZØR", 'instr': "Scan with your phone\nto connect\n(Use Firefox on Android)", 'running': "Server running on port" }
}

def resource_path(relative_path):
    """ Obtiene la ruta absoluta al recurso, funciona para dev y para PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args): pass 
    def do_POST(self):
        if self.path == '/log':
            length = int(self.headers['Content-Length'])
            self.rfile.read(length)
            self.send_response(200)
            self.end_headers()
        else:
            super().do_POST()

def start_server():
    # Usar la ruta correcta para el HTML
    web_dir = resource_path(".")
    os.chdir(web_dir)

    socketserver.TCPServer.allow_reuse_address = True
    try:
        with socketserver.TCPServer(("", PORT), QuietHandler) as httpd:
            httpd.serve_forever()
    except OSError: pass

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.current_lang = 'es'
        self.title("Just Dance Controller Server")
        self.geometry("360x520")
        self.resizable(False, False)
        self.configure(bg="#111026")

        icon_path = resource_path("favicon.ico")
        try:
            self.iconbitmap(icon_path)
        except:
            pass

        self.btn_lang = tk.Button(self, text="EN", command=self.toggle_lang, bg="#222", fg="white", bd=0, font=("Segoe UI", 8), cursor="hand2")
        self.btn_lang.place(x=320, y=10)

        self.lbl_title = tk.Label(self, text=TEXTS['es']['title'], font=("Segoe UI", 20, "bold"), bg="#111026", fg="white")
        self.lbl_title.pack(pady=(25, 5))
        
        self.lbl_subtitle = tk.Label(self, text=TEXTS['es']['subtitle'], font=("Segoe UI", 10), bg="#111026", fg="#00f3ff")
        self.lbl_subtitle.pack(pady=(0, 20))

        self.ip = get_local_ip()
        self.url = f"http://{self.ip}:{PORT}"

        qr = qrcode.QRCode(box_size=8, border=2)
        qr.add_data(self.url)
        qr.make(fit=True)
        img_qr = qr.make_image(fill_color="black", back_color="white")
        self.photo = ImageTk.PhotoImage(img_qr)

        lbl_qr = tk.Label(self, image=self.photo, bd=5, relief="flat")
        lbl_qr.pack(pady=10)

        self.lbl_instr = tk.Label(self, text=TEXTS['es']['instr'], font=("Segoe UI", 11), bg="#111026", fg="#aaa", justify="center")
        self.lbl_instr.pack(pady=15)

        self.entry_ip = tk.Entry(self, font=("Consolas", 11), justify="center", 
                                 bg="#222", fg="#00f3ff", relief="flat",
                                 readonlybackground="#1a1a2e") 
        self.entry_ip.insert(0, self.url)
        self.entry_ip.configure(state="readonly")
        self.entry_ip.pack(pady=5, ipadx=20, ipady=8) 

        self.server_thread = threading.Thread(target=start_server, daemon=True)
        self.server_thread.start()

    def toggle_lang(self):
        if self.current_lang == 'es':
            self.current_lang = 'en'
            self.btn_lang.config(text="ES")
        else:
            self.current_lang = 'es'
            self.btn_lang.config(text="EN")
        
        self.lbl_title.config(text=TEXTS[self.current_lang]['title'])
        self.lbl_subtitle.config(text=TEXTS[self.current_lang]['subtitle'])
        self.lbl_instr.config(text=TEXTS[self.current_lang]['instr'])

if __name__ == "__main__":
    app = App()
    app.mainloop()