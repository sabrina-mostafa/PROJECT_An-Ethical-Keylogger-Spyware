from cryptography.fernet import Fernet
import os



# Generate the key
key = Fernet.generate_key()

# Specify the folder path
folder_path = "C:\\Users\\User\\Documents\\IIUC\\7th_Computer_Security\\Final_Project\\Cryptography" # Enter the file path you want your files to be saved to

# Specify the key file path
key_file_path = os.path.join(folder_path, "encryption_key.txt")

# Write the key to the file
with open(key_file_path, 'wb') as file:
    file.write("ENCRYPTION KEY :    ".encode())  # Convert the string to bytes
    file.write(key)
    file.close()