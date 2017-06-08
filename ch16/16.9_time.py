from datetime import datetime

def time_until_birthday():
    dob_input = input(('Please enter the date of your birth in '
                       'the format "mm/dd/yyyy": '))
    dob = datetime.strptime(dob_input, '%m/%d/%Y')
    now = datetime.now()
    if now > datetime(now.year, dob.month, dob.day):
        age = now.year - dob.year
        next_year = True
    else:
        age = now.year - dob.year - 1
        next_year = False
    time_to_birthday = datetime(now.year + next_year,
                                dob.month, dob.day) - now
    days = time_to_birthday.days
    hours, remainder = divmod(time_to_birthday.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    print("\nYou are {} years old.".format(age))
    print(("You have {0} days, {1} hours, {2} minutes and {3} "
           "seconds left until your next birthday.").format(
               days, hours, minutes, seconds))

time_until_birthday()
  
