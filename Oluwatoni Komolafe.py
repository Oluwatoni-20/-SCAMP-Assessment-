n = int(input("Enter nth term of fibonacci number:  "))
Start_of_fibonacci = 0
next_number = 1
sum = Start_of_fibonacci + next_number
if n <=0:
   print ("please Enter a positive number")
 
while Start_of_fibonacci <n:
        Start_of_fibonacci = next_number
        next_number = sum
        sum = Start_of_fibonacci + next_number
        print (sum)
        
