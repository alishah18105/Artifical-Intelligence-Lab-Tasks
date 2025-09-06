#a Python program to extract year, month, date and time using Lambda
from datetime import datetime
date_time_str = datetime.now()
extract_year = lambda dt: dt.year
extract_month = lambda dt: dt.month 
extract_date = lambda dt: dt.day
extract_time = lambda dt: dt.strftime("%H:%M:%S")
print(f"Cuurent Date is: {extract_date(date_time_str):02d}-{extract_month(date_time_str):02d}-{extract_year(date_time_str)}")
print(f"Current Time is: {extract_time(date_time_str)}")