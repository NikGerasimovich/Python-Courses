# Task 4.3 Implement The Keyword encoding and decoding for latin alphabet. The Keyword Cipher uses a Keyword to
# rearrange the letters in the alphabet. Add the provided keyword at the begining of the alphabet. A keyword is used
# as the key, and it determines the letter matchings of the cipher alphabet to the plain alphabet. Repeats of letters
# in the word are removed, then the cipher alphabet is generated with the keyword matching to A, B, C etc. until the
# keyword is used up, whereupon the rest of the ciphertext letters are used in alphabetical order, excluding those
# already used in the key.
""" Метод product используется вместо вложенных циклов для перебора 2х и более последовательностей """
import string
from itertools import product


class Chipher:
    """" Класс предназначен для кодирования и декодирование слов"""

    OutEncode = list()
    OutDecode = list()

    def __init__(self, codename):
        self.codename = " ".join(codename).split()
        self.alphabetstr = " ".join(string.ascii_lowercase).split()

    def Chiperalphabet(self, chiperword):
        """" Функция удаляет из алфавита все буквы которые встречаются в слове и добовляет слово в начало """

        self.codename_nodouble = list(set(self.codename))
        for codenameSymb, alphabetSymb in product(self.codename_nodouble, self.alphabetstr):
            if codenameSymb == alphabetSymb:
                self.alphabetstr.remove(alphabetSymb)
        self.cryptostring = self.codename + self.alphabetstr
        self.alphabetstr = " ".join(string.ascii_lowercase).split()
        return print(self.cryptostring), self.cryptostring

    def encode(self, chiperword):
        """ Функция кодирует слово по измененному алфавиту из Chiperalphabet() """

        self.chiperword = " ".join(chiperword.lower()).split()
        self.Chiperalphabet(self.chiperword)

        for nochiperwordSymb, alphabetwordSymb in product(self.chiperword, self.alphabetstr):
            if nochiperwordSymb == alphabetwordSymb:
                self.OutEncode.append(self.cryptostring[self.alphabetstr.index(alphabetwordSymb)])
        print("".join(self.OutEncode))
        self.OutEncode.clear()

    def decode(self, decodeword):
        """ Функция декодирует слово по обычному алфавиту если оно было введено такое же как и кодируемое слово"""

        self.decodeword = " ".join(decodeword).split()
        for decodSymb, cryptoSymb in product(self.decodeword, self.cryptostring):
            if decodSymb == cryptoSymb:
                self.OutDecode.append(self.alphabetstr[self.cryptostring.index(cryptoSymb)])
        print("".join(self.OutDecode))
        self.OutDecode.clear()


c = Chipher("crypto")
c.encode("Hello world")
c.decode("btggjvjmgp")

c.encode("Nikita")
c.decode("idfdqc")

v = Chipher("keksik")
v.encode("Hello world")
v.decode("bigglulogs")

d = Chipher("Most Important")
d.encode("peleng")
d.decode("dInIbp")

# Программа кодирует/декодирует слово по алфавиту где удалются буквы из введенного слова и добовляется все слово
# целиком вперёд строки алфавита.