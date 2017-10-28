import random

# Start Program
print ("Hi there! I, the computer, will calculate a number. Type in a number and see if you can guess it!")

# Let user choose the max number in the range.
print ("\nYou get to choose the highest number in the range. If you choose 100, the range will be 0 to 100.")

userMax = int(input())

# Program generates the random number
randomNumber = random.randrange(userMax)
# print randomNumber - Only use for debugging purposes.

print("Number has been generated. Type your guess.")
 
 # Start while loop
while True:
	# User guess goes here
	userNumber = int(input())

	# Conditional statements begin, self-explanatory.
	if userNumber > randomNumber:
		print("Your number is too high!")
		
	elif userNumber < randomNumber:
		print("Your number is too low!")

	# Success!
	else: 
		print("Woohoo! You guessed the number! Exiting the program.")
		break