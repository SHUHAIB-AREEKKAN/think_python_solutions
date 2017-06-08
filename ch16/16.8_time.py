from datetime import date

def current_weekday():
  i=date.today()
  print(i.strftime('%A'))
current_weekday()
