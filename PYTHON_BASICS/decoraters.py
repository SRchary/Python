
def decoreter_fun(fun):

	def inner():
		print("X"*20)
		fun()
		print("Y"*20)

	return inner


def say_hellow():

	print("hellow World")

#Way 1
# decoretor normal Way
dec =  decoreter_fun(say_hellow)
# delete decoreter_fun from memory for closer
#del decoreter_fun
dec()


#Way 2

@decoreter_fun
def say_hellow_tow():
	print("say_hellow_tow ")

say_hellow_tow()

'''

Decoretor is function it takes a function as parameter

Why :  With using decorater we can extend function funcatinality with out dusturbing  a function 

closer also working in decoretor

'''





