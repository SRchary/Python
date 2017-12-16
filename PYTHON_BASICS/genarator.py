def myfun(lst):
	a = []
	for l in lst:
		yield (l*l)
		
ls  = myfun([10,1 ,2])		
print type(ls)

print ls.next()
print ls.next()
print ls.next()	

