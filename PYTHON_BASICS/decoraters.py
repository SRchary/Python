def decoretor_fun(orginal_fun):
	
	def inner_fun():
		print "IM FROM {}".format(orginal_fun.__name__)
		return orginal_fun()
	return inner_fun;
@decoretor_fun
def sum():
	print "TEST"

sum()

print "--------------------------------- \n";
dec = decoretor_fun(sum)
dec()


