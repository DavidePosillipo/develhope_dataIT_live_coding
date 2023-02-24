import random 

def create_password_generator(characters):

	def create_password(length):
		output = []
		for i in range(length):
			output.append(random.choice(characters))

		return ''.join(output)

	return create_password


pw_generator = create_password_generator("abcdefgi")

print("Il tipo di dati di pw_generator è: ", type(pw_generator))

my_password = pw_generator(10)

print("La mia password è: ", my_password)