class MyClass:
	name = "RAVI";
	contact ="7396625277"
	def __init__(self, uname):
		self.name= uname
		print self.name;
	
	def instanceMethod(self):
		print self.name ,self.contact
		return self
	
	@staticmethod
	def staticMethod():
		print "Im From Static Method"

	@classmethod ## class method is nothing but alternate of constructer
	def classMethod(cls ,emp_details):
		print "Im From Class Method"
		cls.name = emp_details
		cls.contact = emp_details[1]
		cls(emp_details)
		print id(cls)
		
MyClass.classMethod('raj')




