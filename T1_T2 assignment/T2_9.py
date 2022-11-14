num =input("Guess the num: ")

#while num!=6:
#    print("entered is not lucky number")
 #   num =input("gGuess the num:")

#num =-1
#answer ='yes'
#while num!=5  and answer != 'no':
 #   num = input("Guess the num: ")
 #   if num!=5:
#        print("entered is not lucky num")
#        ansewr= input("would you like to guess again? ")
'''
counter = 1
while counter <= 5:
   number = input("Guess the " + str(counter) + ". number ")
   if number != 5:
       print ("Try again.")
   else:
       print ("Good guess!")
   counter = counter +1
else:
   print ("Game over")'''


counter = 1
while counter <= 5:
   num = input("Guess the " + str(counter) + ". number ")
   if num != 5:
       print ( "Try again.")
   else:
       print ("Good guess!")
       break
   counter = counter +1
else:
   print ("Sorry but that was not very successful")
