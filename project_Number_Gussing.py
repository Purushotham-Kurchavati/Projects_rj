# Build a Number guessing game, in which the user selects a range.
# Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
# Some random integer will be selected by the system and the user has to guess that integer in the minimum number of guesses
r
# import random
# import math
# # Taking Inputs
# lower = int(input("Enter Lower bound:- "))

# # Taking Inputs
# upper = int(input("Enter Upper bound:- "))

# # generating random number between
# # the lower and upper
# x = random.randint(lower, upper)
# print("\n\tYou've only ",
# 	round(math.log(upper - lower + 1, 2)),
# 	" chances to guess the integer!\n")

# # Initializing the number of guesses.
# count = 0

# # for calculation of minimum number of
# # guesses depends upon range
# while count < math.log(upper - lower + 1, 2):
# 	count += 1

# 	# taking guessing number as input
# 	guess = int(input("Guess a number:- "))

# 	# Condition testing
# 	if x == guess:
# 		print("Congratulations you did it in ",
# 			count, " try")
# 		# Once guessed, loop will break
# 		break
# 	elif x > guess:
# 		print("You guessed too small!")
# 	elif x < guess:
# 		print("You Guessed too high!")

# # If Guessing is more than required guesses,
# # shows this output.
# if count >= math.log(upper - lower + 1, 2):
# 	print("\nThe number is %d" % x)
# 	print("\tBetter Luck Next time!")

# # Better to use This source Code on pycharm!

# import random
# import math

# lower = int(input("Enter a lower Number:- "))

# upper = int(input("Enter a upper Number:- "))

# x = random.randint(lower,upper)

