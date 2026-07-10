import time
class Timer:
 def __init__(self):
     self.minutes = 0
     self.seconds = 0
 def timer(self):
    self.minutes=int(input("how many minutes?: "))
    self.seconds= self.minutes * 60
    while self.seconds > 0:
       print(self.seconds)
       time.sleep(1)
       self.seconds -= 1
    print("time is up")




