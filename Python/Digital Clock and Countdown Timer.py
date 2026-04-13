import time
import sys

def userChoice(choice):
    if choice == "1":
        digital_clock()
    elif choice == "2":
        seconds = int(input("Enter the number of seconds to countdown: "))
        countdown_timer(seconds)
    else:
        print("Invalid choice!")

def digital_clock():
    """Displays a digital clock."""
    while True:
        current_time = time.strftime("%H:%M:%S", time.localtime())
        print("\rDigital Clock: " + current_time, end = '')
        time.sleep(1)
    
# Solution as follows
def countdown_timer(seconds):
    """Counts down from a given number of seconds."""
    print("Countdown Timer started!")
    while seconds > 0:
        print("\rTime remaining: " + str(seconds) + " seconds", end = '')
        time.sleep(1)
        seconds -= 1
    print("\nTime's up!")
    
    
if __name__ == '__main__':
    while True:
        choice = input("Choose an option (1:Digital Clock, 2:Countdown Timer): ")
        userChoice(choice)