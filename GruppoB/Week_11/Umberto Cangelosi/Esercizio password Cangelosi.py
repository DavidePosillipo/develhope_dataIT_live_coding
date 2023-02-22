import random
import string 


def create_password_generator(string_input):
    list1 =[element for element in string_input]
    
    def password_creator(lenght):
        password = "".join([random.choice(string_input) for i in range(0,lenght)])    
        return password 
    
    return password_creator        
            
alpha_password = create_password_generator(string.ascii_letters)
digit_password = create_password_generator(string.digits)
symbol_password = create_password_generator(string.punctuation)

print(alpha_password(6))
print(digit_password(7))
print(symbol_password(8))
        