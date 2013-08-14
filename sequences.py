#!/usr/local/bin/python 


list=[-1,-3,-2,-2,-1,4,5,4]
c=0
tmp=0
value=0

while c<len(list)-1:
	if list[c]+list[c+1] == 0:
		print "MATCH"
		print str(list[c])+","+str(list[c+1])
		value=1
		break
		
	elif tmp + list[c+1] == 0:
		print "MATCH"
		for i in list[:c+2]:
			print str(i)
		value=1
		break
	else:
		if tmp == 0:
			tmp = list[c]
		tmp=tmp+list[c+1]
	c+=1

if value == 0:
	print "NOT MATCH"
