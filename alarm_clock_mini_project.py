import time
import datetime
from playsound import playsound

def set_alarm(alarm_time):
    print(f"Alarm is set for {alarm_time}")
    
    while True:
        # Get current time in HH:MM format
        now = datetime.datetime.now().strftime("%H:%M")
        
        # Check if it's time to wake up
        if now == alarm_time:
            print("Wake up! ⏰")
            # Play your alert sound
            playsound('C:\\Users\\gopir\\OneDrive\\Documents\\playsound.mpeg')
            break # Stop the loop after the alarm rings
            
        # Wait 1 second before checking the time again
        time.sleep(1)

# Example usage
user_input = input("Enter alarm time in HH:MM format (24-hour): ")
set_alarm(user_input)
