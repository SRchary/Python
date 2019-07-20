def outer_fun(exponent):

    def inner(base):
        return pow(base ,exponent)
    return inner


inner_out_one = outer_fun(2)

print(inner_out_one(1))
print(inner_out_one(2))
print(inner_out_one(3))
print(inner_out_one(4))
print(inner_out_one(5))
print(inner_out_one(6))



