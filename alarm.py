import datetime
import time
def alarm():
    alarm_time = input("Enter the alarm time in (HH:MM) format: ")
    parts = alarm_time.split(":")
    if len(parts) != 2:
        print("Invalid time format. Please enter the time in HH:MM format.")
        return
    try:
        hour = int(parts[0])
        minute = int(parts[1])
    except ValueError:
        print("Invalid time format")
        return
    if hour < 0 or hour > 23 :
        print("Invalid hour. Please enter a value between 0 and 23.")
        return
    if minute < 0 or minute > 59:
        print("Invalid minute. Please enter a value between 0 and 59.")
        return
    now = datetime.datetime.now()
    if hour < now.hour:
        print("Today don pass. Please enter a future time.")
        return
    if hour == now.hour and minute < now.minute:
        print("Today don pass. Please enter a future time.")
        return
    print(f"current time: {now.strftime('%H:%M')}")
    print(f"Alarm set for: {alarm_time}")
    print("Waiting ...")
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == alarm_time:
            print("ALARM!")
            break
        time.sleep(1)