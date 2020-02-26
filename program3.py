import math
k = list(map(int,input().split()))
for i in k:
	f = math.factorial(i)
	print(f,end=',')
