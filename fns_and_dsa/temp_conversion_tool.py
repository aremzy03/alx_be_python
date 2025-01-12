from datetime import datetime, date, time, timedelta
now = datetime.now()

def display_current_datetime():
    return now.strftime("%Y-%m-%d %H:%M:%S")

current_date = display_current_datetime()
print(current_date)

num_of_days = int(input("Enter a number of days "))

def calculate_future_date():
    future = now + timedelta(days=num_of_days)
    return future

future_date = calculate_future_date()
print(future_date)