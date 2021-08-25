# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.


import math

def fun_kth_occurrences(s, n):
	d = dict()
	for i in s:
		if i in d:
			d[i] += 1
		elif i.isspace():
			pass
		else:
			d[i] = 1
	
	cnt = 1

	while cnt<n:
		max_num = max(d.values())
		for k,v in d.items():
			if max_num == v:
				d[k] = 0
				cnt += 1
	
	return max(d,key=d.get)


