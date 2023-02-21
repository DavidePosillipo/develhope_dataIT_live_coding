import random

def password_pool(pool):
    return lambda length: "".join(random.choices(pool, k = length))

alpha_pass = password_pool("abc")
symbol_pass  = password_pool("!@#")
num_pass = password_pool("345123")
print(num_pass(8))
print(alpha_pass(10))
print(symbol_pass(5))




"""Testing
import random

def password_pool(pool):
     def generator(length): 
        return random.choices(pool, k = length)

alpha_pass = password_pool("abc")
symbol_pass  = password_pool("!@#")
print(alpha_pass(10))
print(symbol_pass(5))"""
