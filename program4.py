h = 30	
c = 50
k = list(map(int,input().split(',')))
for d in k:
	i = ((2*c*d)/h)**0.5
	print(int(i),end=',')
print()
