from cryptography.fernet import Fernet
def create_key():
	key = Fernet.generate_key()
	with open('crypto.key', 'wb') as key_file:
		key_file.write(key)

create_key()