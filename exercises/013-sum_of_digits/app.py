#Complete the function "digits_sum" so that it prints the sum of a three digit number.
def digits_sum(num):
  
  return num%10 + ((num)%100)//10 + ((num)%1000)//100


#Invoke the function with any three-digit-number
#You can try other three-digit numbers if you want
print(digits_sum(147))