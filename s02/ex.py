import sys

#sys.modules.keys()
#sys.path
#
def factorial(n):
	out = 1
	for i in range(1, n+1):
		out = out * i
	return out

# in bash argv[0] is this file name (ex.py)
# and argv[1] is input value, In this case, the number we want to calculate the factorial of that number

n = int(sys.argv[1])
print(factorial(n))
