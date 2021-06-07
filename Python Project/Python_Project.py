import time


def addition(): 
	print("Hello there.")
	time.sleep(4)
	print("Today we are going to calculate what " + str(a) + " plus " + str(b) + " equals")
	time.sleep(3)
	print("Setting up the problem...")
	time.sleep(3)
	print("Think of the number " + str(a) + " as " + str(a) + " boxes")
	time.sleep(3)
	print("Now add " + str(b) + " more boxes to the " + str(a) + " that you had originally")
	time.sleep(3)
	print("If you add all of the boxes up, you'd find that you have " + str(c) + " boxes")


def multiplication():
	time.sleep(3)
	print("...")
	time.sleep(3)
	print("...")
	time.sleep(3)
	print("Hello again.")
	time.sleep(2)
	print("This time I'll teach you multiplication")
	time.sleep(2)
	print("Hopefully you didn't input a big number in the last problem")
	time.sleep(2)
	print("This time around, we're going to calculate what " + str(a) + " times " + str(b) + " equals")
	time.sleep(2)
	print("Just like the last problem, we'll treat this one the same")
	time.sleep(2)
	print("Imagine that you have " + str(a) + " boxes, now imagine that you have " + str(a) + " boxes " + str(b - 1) + " more times")
	time.sleep(4)
	print("What you should be imagining, is " + str(a) + " boxes, and then another " + str(a) + " boxes " + str(b - 1) + " more times")
	time.sleep(3)
	print("When all is said and done, you should realize that you have " + str(c) + " boxes.")
	time.sleep(3)

a = int(input("Please enter a number: "))
time.sleep(2)
print("Interesting....")
time.sleep(2)
b = int(input("Now please enter another number: "))
c = a + b
time.sleep(2)
print("Thank you.")
time.sleep(2)
addition();
multiplication();