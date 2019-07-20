def outer_fun(exponent):

    def inner(base):
        return pow(base, exponent)
    return inner

#SQUERE
inner_out_one = outer_fun(2)

print(inner_out_one(1)) # 1^2
print(inner_out_one(2)) # 2^2
print(inner_out_one(3)) # 3^2
print(inner_out_one(4)) # 4^2
print(inner_out_one(5)) # 5^2
print(inner_out_one(6)) # 6^2
print(inner_out_one(7)) # 7^2
print(inner_out_one(8)) # 8^2

# Cube
inner_out_two = outer_fun(3)
print(inner_out_two(1)) # 1^3
print(inner_out_two(2)) # 2^3
print(inner_out_two(3)) # 3^3
print(inner_out_two(4)) # 4^3
print(inner_out_two(5)) # 5^3
print(inner_out_two(6)) # 6^3
print(inner_out_two(7)) # 7^3

'''
Example Two

'''

def pop_list(list):

    def inner():
        list.remove(len(list) -1)
        return list

    return inner

a = [0,1,2,3,4,5,6]
poplist =pop_list(a)

print(poplist())
print(poplist())
print(poplist())
print(poplist())
print(poplist())
print(poplist())
print(poplist())

'''
Defination : 

Inner function can access outer function name space (  veriables  )  from out side of th outer function


It means : inner function can remember the outer function veriables  ofter deletion of inner function






'''



