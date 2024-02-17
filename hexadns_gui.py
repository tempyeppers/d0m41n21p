import re
import socket 
import tkinter as tk
from tkinter import messagebox

def extract_ipaddr(url, mode):
    try:
        if mode == "domain to ip":
            domains =  re.findall(r'(?:https?://)?(?:www\d?\.)?([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})(?:\/|\s|\[|$)', url)
            converter = socket.gethostbyname
        elif mode == "ip to domain":
            domains = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', url)
            converter = socket.gethostbyaddr
        else:
            return"invalid"
    
        res = ""
        for domain in domains:
            try:
                if mode == "domain to ip":
                    res += f"{domain}:{converter(domain)}\n"
                else:
                    res += f"{domain}: {converter(domain)[0]}\n"
            except (socket.gaierror, socket.herror) as nou:
                res += f"Error: {str(nou)}\n"
        return res 
    except Exception as nou:
        messagebox.showerror("Error", f"An error occurred: {str(nou)}")

def process():
    mode = mode_var.get()
    url = url_text.get("1.0", "end-1c")
    res = extract_ipaddr(url, mode)
    output.delete("1.0", "end")
    output.insert("1.0", res)


#added gui 
gui = tk.Tk()
gui.title("DNS Resolver by L30")

mode_var = tk.StringVar(gui, "domain to ip")
mode_label = tk.Label(gui, text="select mode:")
mode_label.pack()
mode_option = tk.OptionMenu(gui, mode_var, "domain to ip", "ip to domain")
mode_option.pack()

url_label = tk.Label(gui, text="enter domain/ip:")
url_label.pack()
url_text = tk.Text(gui, height=4, width=50)
url_text.pack()

process_button = tk.Button(gui, text="process", command=process)
process_button.pack()

output_label = tk.Label(gui, text="results:")
output_label.pack()
output = tk.Text(gui, height=10, width=50)
output.pack()

gui.mainloop()
