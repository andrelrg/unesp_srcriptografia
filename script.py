# from cryptography.fernet import Fernet
from criptograpy import Criptograpy
import os

def main():
    os.environ["SECRETKEY"] = "TESTKEY"
    text = input("Frase: ")
    c = Criptograpy(text)
    cripted = c.create_hash()
    print("Criptografia: " + cripted)
    print("Descriptografado: " + c.decrypt(cripted))

if __name__ == "__main__":
    main()