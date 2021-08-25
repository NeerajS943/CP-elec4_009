# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.

import math
def nthpowerfulnumber(n):
	# Your code goes here
	found = 0
	guess = 0
	while(found<=n):
		guess+=1
		if(power(guess)):
			found +=1
	return guess

def power(a):
	while(a%2==0):
		cnt =0
		while(a%2==0): 
			a//=2
			cnt += 1
		if(cnt==1):
			return False
	
	for i in range(3,int(math.sqrt(a))+1,2):
		cnt = 0
		while(a%i==0):
			a//=i
			cnt += 1
		if(cnt == 1):
			return False
	
	return a==1
