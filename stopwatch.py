from tkinter import *
from tkmacosx import Button


window = Tk()
window["bg"] = "black"
window.title("Stopwatch")
window.geometry("485x180")
window.resizable(False, False)

sec, min, hour = 0, 0, 0

running = False

def update():
    global update_time, sec, min, hour
    sec += 1
    if sec == 60:
        sec = 0
        min += 1
    if min == 60:
        min = 0
        hour += 1
    if sec > 9:
        sec_time = str(sec)
    else:
        sec_time = str(0) + str(sec)

    if min > 9:
        min_time = str(min)
    else:
        min_time = str(0) + str(min)

    if hour > 9:
        hour_time = str(hour)
    else:
        hour_time = str(0) + str(hour)

    time_label.config(text = hour_time + ":" + min_time + ":" + sec_time)

    update_time = time_label.after(1000, update)

def start():
    global running
    if not running:
        update()
        running = True


def reset():
    global running, sec, min, hour

    if running:
        time_label.after_cancel(update_time)

        running = False

    sec, min, hour = 0, 0, 0

    time_label.config(text = "00:00:00")


def pause():
    global running
    if running:
        time_label.after_cancel(update_time)

        running = False




start_button = Button(window, text = "Start", font = ("arial", 18), bg = "green", fg = "black", borderless = True, command = start)
start_button.place(x = 60, y = 120)

pause_button = Button(window, text = "Pause", font = ("arial", 18), bg = "yellow", fg = "black", borderless = True, command = pause)
pause_button.place(x = 180, y = 120)

reset_button = Button(window, text = "Reset", font = ("arial", 18), bg = "red", fg = "black", borderless = True, command = reset)
reset_button.place(x = 300, y = 120)

time_label = Label(window, text = "00:00:00", font = ("arial", 80), bg = "black")
time_label.place(x = 80, y = 10)


window.mainloop()