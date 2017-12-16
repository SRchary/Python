file_obj =open("ravi.txt" ,"w+")
user_inputs  = raw_input()
file_obj.write(user_inputs)
str = file_obj.read()
print str
print str.count("ravi")


