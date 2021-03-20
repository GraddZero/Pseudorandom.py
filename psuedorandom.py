#Made by GraddZer0
#Created: 20/03/2021

#imports required libraries
import datetime
import math
from time import sleep

#defines function, sets default value to 1 digit.
def number(digits=1):
	try:
		#error if not an int
		digits = int(digits)
		if digits == 0:
			digits = 1
		arr = []	#array for final number
		#sets seed based of current date including ms, strips it from datetime format(yyyy-mm-dd hh:mm:ss.ssssss)
		seed = str(datetime.datetime.now())
		seed = seed.replace('-','')
		seed = seed.replace(':','')
		seed = seed.replace('.','')
		seed = int(seed.replace(' ',''))
		#sets seed2
		seed2 = math.pow(seed, 2)
		number = seed2 % seed
		number = str(number)
		#print(number)
		arr.append(number[-13]) #adds to final number array
		nextSeed = number[-12:-5]
		#adds digit to array until it is the requested length
		for i in range(digits-1):
			seed2 = math.pow(seed, 9)
			number = seed2 % int(nextSeed)
			number = math.pow(number, 20)
			number = str(number)
			#print(number)
			arr.append(number[-13])
			nextSeed = number[-12:-5]
		final  = ''.join(arr)
		final = int(final)
		if len(str(final)) < digits: #ensures that value is the correct amount of digits long, else adds 0s to end
			for i in range(digits - len(str(final))):
				final = str(final) +'0'
		final = int(final)
		sleep(0.002) #ensures numbers requested in quick succession aren't the same.
		return final
		#exceptions in the event function doesnt break when adding NOT int
	except TypeError:
		raise TypeError("Number function expects an integer argument.")
	except ValueError:
		raise ValueError("Number function expects an integer argument.")
