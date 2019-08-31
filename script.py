from cryptography.fernet import Fernet
import os

def main():
    os.system('clear')
    while(1):
        print("Trabalho de Criptografia")
        print("Sistema ira criptopgrafar e descriptografar uma frase/palavra")
        print("\n")
        inp = input("Digite 1 para digitar a frase ou 2 para sair:")
        if inp == "1":
            text = input("Frase: ")
            generated, f = cript(text)
            print("Frase criptografada: " + str(generated))
            input("Aperte enter para descriptografar")
            print(decript(generated, f))
            input("Start Again...")
            os.system('clear')
        else:
            break

def cript(text):
    key = Fernet.generate_key()

    f = Fernet(key)
    return f.encrypt(bytes(text, 'utf-8')), f

def decript(generated, f):
    return f.decrypt(generated)

if __name__ == "__main__":
    main()