import random
import string

def create_password_generator(characters: str | list[str]):

    if isinstance(characters, list):
        characters = ''.join(characters)

    def password_generator(password_len: int) -> str:
        return ''.join(random.choices(characters, k=password_len))

    return password_generator

alpha_password = create_password_generator('abcdef')
symbol_password = create_password_generator('!@#$%')
alphanumsim_password = create_password_generator([string.ascii_letters, string.digits, '!?£$%&/-_'])

print(alpha_password(10))
print(symbol_password(10))
print(alphanumsim_password(10))