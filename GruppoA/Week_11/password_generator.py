import random

def create_password_generator(characters):

	def create_password(lenght):
		output = []
		for i in range(lenght):
			output.append(random.choice(characters))
		return ''.join(output)

	return create_password



psw_generator = create_password_generator('abcdefghi')
print("Il tipo di dati di psw_generator è: ", type(psw_generator))

my_password = psw_generator(10)

print("La mia password: ", my_password)