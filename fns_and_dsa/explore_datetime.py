from datetime import datetime, date, time, timedelta
now = datetime.now()

def display_current_datetime():
    return now.strftime("%Y-%m-%d %H:%M:%S")

current_date = display_current_datetime()
print(current_date)

number_of_days = int(input("Enter the number of days to add to the current date:"))

def calculate_future_date():
    future = now + timedelta(days=number_of_days)
    return future

future_date = calculate_future_date()
print(future_date.strftime("%Y-%m-%d %H:%M:%S"))