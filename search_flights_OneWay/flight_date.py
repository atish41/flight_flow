import datetime

def flightdate(date_str):
  # Convert the string to a datetime object
  date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
  # Get the day of the week
  weekday = date_obj.strftime("%a")
  # Get the day of the month
  day = date_obj.strftime("%d")
  # Get the month name
  month = date_obj.strftime("%B")
  # Format the output string
  output_str = f"{weekday}, {day}th {month}"
  # Print the output string
  return output_str
