#FutureTime.py
#Name: Talia Astorino
#Date: 2/1/2026
#Purpose: Using variables and assignments, numeric data types, arithmetic operators, and type conversion.

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = now.hour
  currentMinute = now.minute

  #TODO:
  #Ask user for hours
  Hours = int(input("Enter the number of hours to add. "))
  #Ask user for minutes
  Minutes = int(input("Enter the number of minutes to add. "))

  #Calculate the time after the user-supplied time has passed.
  totalMinutes = currentMinute + Minutes
  futureMinutes = totalMinutes % 60
  additionalHours = totalMinutes // 60
  futureHour = (currentHour + Hours + additionalHours - 6) % 24
  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"
  print(f"The future time is {futureHour:02d}:{futureMinutes:02d}")

if __name__ == '__main__':
  main()

  # My time was 6 hours ahead, and after doing some research and realizing that the now.hour was wrong, I had to hard code the -6 into the futureHour, because it is the only solution I could find. If you have a fix you would like me to use instead, I will change it.
