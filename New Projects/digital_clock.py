from datetime import datetime, timezone
from zoneinfo import ZoneInfo
from tkinter import *

root = Tk()
root.title('Digital Clock')
root.geometry('350x100')


def times():
    sofia_time = datetime.now(ZoneInfo('Europe/Sofia'))
    current_time = sofia_time.strftime('%H:%M:%S')
    Sofia_clock.config(text=current_time)
    Sofia.config(text='Sofia')
    Sofia_clock.after(1000, times)

    london_time = datetime.now(ZoneInfo('Europe/London'))
    current_time = london_time.strftime('%H:%M:%S')
    london_clock.config(text=current_time)
    london.config(text='London')
    london_clock.after(1000, times)


Sofia = Label(root, font=('calibri', 20, 'bold'))
Sofia.place(x=44, y=5)
Sofia_clock = Label(root, font=('calibri', 25, 'bold'))
Sofia_clock.place(x=15, y=40)

london = Label(root, font=('calibri', 20, 'bold'))
london.place(x=224, y=5)
london_clock = Label(root, font=('calibri', 25, 'bold'))
london_clock.place(x=205, y=40)

times()
mainloop()
