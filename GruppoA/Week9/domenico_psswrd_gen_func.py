##adding conditions
## one uppercase character
## at least one special character
import random

def create_password_generator_v2(string: str):
    
    special=False
    
    for i in string:
        check0=i.isalnum()
        if not check0:
            special=True
            break
            
    if not special:
        
        print('The input string must contain at least one special character(!#?$). Try update the input and re-run the fucntion')
        
    if special:
    
        def child_func(n: int):

            password=''
            r=random.randint(0,n)

            for i in range(n):
                if i==r:
                    b=random.choice(string)
                    a=b.upper()
                    password+=a
                else:
                    a=random.choice(string)
                    password+=a

            list_password_charac=[i for i in password]

            for i in list_password_charac:
                check=i.isalnum()
                if check==False:
                    break

            if check:

                notalnum=[]

                for i in string:
                    alnum=i.isalnum()
                    if not alnum:
                        notalnum.append(i)

                r1=random.randint(0,n)
                list_password_charac[r1]=random.choice(notalnum)

                for i in list_password_charac:
                    password+=i


            return password

        return child_func