from cryptography.fernet import Fernet

def decrypt(filename, key):
	f = Fernet(key)
	with open(filename, 'rb') as file:
		encrypted_data = file.read()
	decrypted_data = f.decrypt(encrypted_data)
	with open(filename, 'wb') as file:
		file.write(decrypted_data)
