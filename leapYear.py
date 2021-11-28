# A leap year is exactly divisible by 4 except for century years (years ending with 00). 
# The century year is a leap year only if it is perfectly divisible by 400. 

while True :
  year = int(input("Enter year: "))
  if (year % 4 == 0):
    if (year % 100 == 0):
      if (year % 400 == 0):
        print ("Year {} is a leap year".format(year))
      else:
        print ("Year {} is NOT a leap year".format(year)) 
    else: 
        print ("Year {} is a leap year".format(year))
  else: 
    print ("Year {} is NOT a leap year".format(year))  
