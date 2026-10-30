print("hello world")
from datetime import datetime, date, time

now = datetime.now()              # local date + time
print(now)                        # 2026-10-28 14:35:02.123456

import tkinter as tk
import math
from datetime import datetime

def draw_clock():
    canvas.delete("all")
    now = datetime.now()

    # Clock face
    cx, cy, r = 200, 200, 180
    canvas.create_oval(cx-r, cy-r, cx+r, cy+r, outline="black", width=3)

    # Hour marks
    for i in range(12):
        angle = math.radians(i * 30 - 90)
        x1 = cx + (r - 15) * math.cos(angle)
        y1 = cy + (r - 15) * math.sin(angle)
        x2 = cx + r * math.cos(angle)
        y2 = cy + r * math.sin(angle)
        canvas.create_line(x1, y1, x2, y2, width=3)

    # Hands
    def hand(angle_deg, length, width, color):
        a = math.radians(angle_deg - 90)
        x = cx + length * math.cos(a)
        y = cy + length * math.sin(a)
        canvas.create_line(cx, cy, x, y, width=width, fill=color)

    sec = now.second + now.microsecond / 1e6
    minute = now.minute + sec / 60
    hour = (now.hour % 12) + minute / 60

    hand(hour * 30, r * 0.5, 8, "black")
    hand(minute * 6, r * 0.7, 5, "blue")
    hand(sec * 6, r * 0.85, 2, "red")

    canvas.create_oval(cx-5, cy-5, cx+5, cy+5, fill="black")
    root.after(50, draw_clock)

root = tk.Tk()
root.title("Analog Clock")
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()
draw_clock()
root.mainloop()