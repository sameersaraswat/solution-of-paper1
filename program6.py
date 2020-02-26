n = int(input())
l = []
l1 = []
l2 = []
for i in range(0,n):
	d = int(input())
	l.append(d)
for j in l:
	if j==0:
		l1.append(j)
	else:
		l2.append(j)
print(l2+l1)
	
