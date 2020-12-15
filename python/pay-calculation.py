#Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
try:
    hours = int(hours)
    rate = int(rate)
except:
    print("not valid input")

if hours>40:
    pay = (hours-40)*rate*1.5+40*rate
else:
    pay = hours*rate
print(pay)