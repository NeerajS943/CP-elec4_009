# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of 
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the 
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….

def reverse(a):
	n = 0
	while a>0:
		n=n*10+a%10
		a=a//10
	return n
def ispalindrome(n):
	return reverse(n)==n

def islychrel(n):
	for i in range(50):
		n += reverse(n)
		if ispalindrome(n):
			return False
	return True

def nthlychrelnumbers(n):
	# your code goes here
	count = 0
	for i in range(4000):
		if(islychrel(i)):
			count += 1
		if (count == n):
			break
	return i 