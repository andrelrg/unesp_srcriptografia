import os

class Criptograpy:
    
    def __init__(self, word):
        self.word = word
        self.key_origin = os.environ["SECRETKEY"]

    def create_hash(self):
        key = self.key_gen()
        new = ""
        key2 = len(self.word)
        for c in self.word:
            new = new + chr(round(ord(c)+key / key2)) + chr(ord(c)+key % key2)
            key2 = ord(c)+key % key2
            key = abs(key-key2)

        return new

    def key_gen(self):
        num = 0
        for c in self.key_origin:
            num = num + ord(c)
        num = round(num/len(self.key_origin))
        return num
    
    def decrypt(self, word):
        key = self.key_gen()
        old = ""
        d = ""
        key2 = len(word)/2
        first = True
        for c in word:
            result = ord(c)
            if first:
                d = round(result - key/key2)
                old = old + chr(d)
                key2 = ord(c)+key % key2
                key = abs(key-key2)
                first = False
            else:
                first = True
                

        return old
