import datetime
import time


class Alarm:

    def get_alarm_time(self):
        return input("Enter the alarm time (HH:MM) format: ")

    def validate_time(self, alarm_time):
        parts = alarm_time.split(":")

        if len(parts) != 2:
            print("Invalid time format")
            return False

        try:
            hour = int(parts[0])
            minute = int(parts[1])
        except ValueError:
            print("Invalid time format")
            return False

        if hour < 0 or hour > 23:
            print("Invalid hour")
            return False

        if minute < 0 or minute > 59:
            print("Invalid minute")
            return False

        now = datetime.datetime.now()

        if hour < now.hour:
            print("Today has passed")
            return False

        if hour == now.hour and minute < now.minute:
            print("Today has passed")
            return False

        return True

    def wait_for_alarm(self, alarm_time):
        print(f"Alarm set for {alarm_time}")

        while True:
            now = datetime.datetime.now().strftime("%H:%M")

            if now == alarm_time:
                print("ALARM!")
                break

            time.sleep(1)

    def alarm(self):
        alarm_time = self.get_alarm_time()

        if not self.validate_time(alarm_time):
            return

        self.wait_for_alarm(alarm_time)