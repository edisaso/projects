import tkinter as tk
from tkinter import ttk, messagebox
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_data():
    url = url_entry.get()
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            all_text = soup.get_text()
            with open('scraped_data.txt', 'w', encoding='utf-8') as f:
                f.write(all_text)
            convert_to_excel()
            messagebox.showinfo("Scraping Complete", "Data has been saved to scraped_data.xlsx")
        else:
            messagebox.showerror("Error", "Failed to retrieve the web page.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Request Exception: {e}")

def convert_to_excel():
    data = []
    with open('scraped_data.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                data.append([line])
    df = pd.DataFrame(data, columns=['Data'])
    df.to_excel('scraped_data.xlsx', index=False)

app = tk.Tk()
app.title("Web Scraping Tool")
app.geometry("400x200")

style = ttk.Style()
style.configure('TEntry', foreground='black')
url_label = ttk.Label(app, text="Enter URL:")
url_label.pack(pady=10)
url_entry = ttk.Entry(app, width=30)
url_entry.pack(pady=5)

#button for scraping
scrape_button = ttk.Button(app, text="Scrape Data", command=scrape_data)
scrape_button.pack(pady=10)

app.mainloop()
