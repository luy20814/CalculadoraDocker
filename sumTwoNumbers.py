def sumTwo(a):
	print a
	num= a.split(":")
	sum= 0
	for temp in num:
		sum = int(sum) + int(temp)
	return sum
	
def resTwo(a, b):
    return int(a)-int(b)
	
def mulTwo(a):
	num= a.split(":")
	mul=1
	for temp in num:
		mul = int(mul) * int(temp)
	return mul
	
def divTwo(a, b):
    return int(a)/int(b)