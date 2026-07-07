import time
def timer():
    minute=int(input("how many minutes?: "))
    seconds=minute*60
    print(f"timing {minute} minutes now")
    while seconds > 0:
       minutes=seconds/60
       remaining_seconds=minutes%60
    time.sleep(1)
    seconds-=1
