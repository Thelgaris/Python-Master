#Complete the function to calculate how many hours and minutes are passed since midnight.
def hours_minutes(secs):
  
  return ("Minutes " +str(secs//60), "Hours " +str(secs//3600))

#Invoke the funtion and pass any interger as its argument.
print(hours_minutes(3900))