import tkinter as tk
import math
import time
from datetime import datetime
import pytz

# Functie om de analoge klok te tekenen
def draw_clock(canvas, center_x, center_y, radius, city_time, city_name):
    canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, fill="lightgray")
    
    # Teken de cijfers (1 t/m 12)
    for i in range(1, 13):
        angle = math.radians(360 * (i / 12) - 90)
        x = center_x + (radius - 30) * math.cos(angle)
        y = center_y + (radius - 30) * math.sin(angle)
        color = "black" if i in [12, 3, 6, 9] else "gray"
        canvas.create_text(x, y, text=str(i), font=("Helvetica", 12, "bold"), fill=color)
    
    # Teken de minutenstreepjes
    for i in range(60):
        angle = math.radians(360 * (i / 60) - 90)
        length = radius - 10 if i % 5 != 0 else radius - 20
        width = 3 if i % 5 != 0 else 6
        color = "black" if i % 15 == 0 else "gray"
        x1 = center_x + length * math.cos(angle)
        y1 = center_y + length * math.sin(angle)
        x2 = center_x + (radius - 5) * math.cos(angle)
        y2 = center_y + (radius - 5) * math.sin(angle)
        canvas.create_line(x1, y1, x2, y2, width=width, fill=color)
    
    # Teken de klokwijzers
    hour_angle = math.radians(360 * (city_time.hour % 12 + city_time.minute / 60) / 12 - 90)
    minute_angle = math.radians(360 * city_time.minute / 60 - 90)
    second_angle = math.radians(360 * city_time.second / 60 - 90)

    canvas.create_line(center_x, center_y, center_x + (radius - 50) * math.cos(hour_angle), 
                       center_y + (radius - 50) * math.sin(hour_angle), width=6, fill="blue")
    canvas.create_line(center_x, center_y, center_x + (radius - 30) * math.cos(minute_angle), 
                       center_y + (radius - 30) * math.sin(minute_angle), width=4, fill="blue")
    canvas.create_line(center_x, center_y, center_x + (radius - 20) * math.cos(second_angle), 
                       center_y + (radius - 20) * math.sin(second_angle), width=2, fill="red")

    # Teken een zwart bolletje in het midden van de klok
    canvas.create_oval(center_x - 5, center_y - 5, center_x + 5, center_y + 5, fill="gray")

    # Voeg de datum toe
    date_text = city_time.strftime("%d-%m-%Y")
    date_center_y = center_y + 30
    date_width = 80
    date_height = 20
    canvas.create_rectangle(center_x - date_width/2, date_center_y - date_height/2,
                             center_x + date_width/2, date_center_y + date_height/2,
                             outline="green", width=2)
    canvas.create_text(center_x, date_center_y, text=date_text, font=("Helvetica", 10, "bold"), fill="green")

    # Voeg de naam van de stad toe onder de klok
    canvas.create_text(center_x, center_y + radius + 20, text=city_name, font=("Helvetica", 20))

# Functie om de klokken bij te werken
def update_clocks():
    # Haal de actuele tijden op
    amsterdam_time = datetime.now(pytz.timezone('Europe/Amsterdam'))
    dubai_time = datetime.now(pytz.timezone('Asia/Dubai'))
    manila_time = datetime.now(pytz.timezone('Asia/Manila'))
    
    # Update de canvas
    canvas.delete("all")
    draw_clock(canvas, 100, 100, 90, amsterdam_time, "Amsterdam")
    draw_clock(canvas, 300, 100, 90, dubai_time, "Dubai")
    draw_clock(canvas, 500, 100, 90, manila_time, "Manila")

    # Roep de update_clocks functie elke 1000 ms opnieuw aan (1 seconde)
    root.after(1000, update_clocks)

# Maak het hoofdvenster
root = tk.Tk()
root.title("Clocks")
canvas = tk.Canvas(root, width=600, height=230, bg="lightblue")
canvas.pack()
root.resizable(False, False)

# Start de klok update functie
update_clocks()

# Start de GUI
root.mainloop()
