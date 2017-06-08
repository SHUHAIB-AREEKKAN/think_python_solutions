# Twice as old- x and y two birthdates- when y twice as x

from datetime import datetime
from datetime import date
def input_dates():
  dob1=datetime.strptime('5/1/1994','%m/%d/%Y')
  dob2=datetime.strptime('4/13/1999','%m/%d/%Y')

  #first=input(('Enter First pearson older one age: MM:DD:YYYY'))
  #second=input(('Eter second pearson younger age:   MM:DD:YYYY'))
  #dob1 = datetime.strptime(first, '%m/%d/%Y')
  #dob2 = datetime.strptime(second, '%m/%d/%Y')
  #today=date.today()
  #age1=calculate_age(dob1)
  #age2=calculate_age(dob2)
  return (dob1,dob2)


def calculate_age(born):
  today = date.today()
  return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def Double_day(tup):
  birth1,birth2=tup
  now =datetime.now()
  if now > datetime(birth1.year,birth1.month,birth1.day) :
    birth1_year=birth1.year
  else: 
    birth1_year=birth1.year+1
  if now > datetime(birth2.year,birth2.month,birth2.day) :
    birth2_year=birth2.year
  else:
    birth2_year=birth2.year+1
  # calculate
  #factor=birth1_year-(2*birth2_year)
  print(factor)


Double_day(input_dates())
