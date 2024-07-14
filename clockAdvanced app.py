from tkinter import *
import datetime
import time
import winsound
from threading import *

root = Tk()
root.geometry('400x400')
root.title('Clock Advanced App')

 # functions
def Threading():
     t1 = Thread(target= alarm)
     t1.start()
def alarm():
    while True:
        # set alarm and waiting for one second
        set_alarm_time = f"{hour.get() }:{minute.get()}: {second.get()}"
        time.sleep(1)

        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        label3.config(text=str(current_time))
        label3.after(1000, alarm)
        # print(current_time)

        # Cheking the current time and alarm time
        if current_time == set_alarm_time:
            text = "Time is up 😉"
            label3.config(text=str(text))

             # sound
            winsound.playSound("sound.wav", winsound.SND_ASYNC)

Label(root, text="Timer Clock", font=("Helvetica",20, "bold"), fg="red").pack(pady=10)
Label(root, text="Set Time", font=("Helvetica",15, "bold")).pack()
label3 = Label(root, text="", font=("Helvetica",15, "bold"))
label3.pack()
frame = Frame(root)
frame.pack()
hour = StringVar(root)
hours =('00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24')
hour.set(hours[0])

hrs = OptionMenu(frame ,hour,*hours)
hrs.pack(side=LEFT)

minute = StringVar(root)
minutes = ('00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31', '32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60')
minute.set(minutes[0])
mins = OptionMenu(frame ,minute,*minutes)
mins.pack(side=LEFT)

second = StringVar(root)
seconds = ('00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31', '32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60')
second.set(seconds[0])
secs = OptionMenu(frame ,second,*seconds)
secs.pack(side=LEFT)

Button(root, text="Start", font=("Helvetica 15"), command=Threading).pack(pady=30)
# alarmBtn.grid(row=5, column=0, columnspan=2)

root.mainloop()

