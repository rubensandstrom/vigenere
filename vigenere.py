import argparse

parser = argparse.ArgumentParser(description='vigenère encryption with message and key')
parser.add_argument('-m', '--message', type=str, metavar='', required=True, help='message to encrypt')
parser.add_argument('-k', '--key', type=str, metavar='', required=True, help='key to encrypt with')
args = parser.parse_args()

alpha = [ "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E",
"F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
"V", "W", "X", "Y", "Z", "Å", "Ä", "Ö", "a", "b", "c", "d", "e", "f", "g", "h",
"i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
"y", "z", "å", "ä", "ö", " ", "!", "?", ",", ".", "+", "-", "*"]

# function to find indexnumber of a letter or symbol in list.
def find_num_in_list(list, letter):
    x = 0
    while letter != list[x]:
        x += 1
    if letter == list[x]:
        return x
# encrypt using 2 arguments: the message and the key.
def vigenere(message, key):
    x = 0
    encrypted = ''
    # loop through all letters in message
    while x < len(message):
        # index of input letter is added to index of key letter to get a new index
        # for the encrypted letter. % len(it self) is used to wrap list bottom to top.
        crypt_message = alpha[(find_num_in_list(alpha, message[x : x + 1])
        + find_num_in_list(alpha, key[x % len(key)])) % len(alpha)]
        # x keeps track of letter that is being encrypted.
        x += 1
        # encrypted letter is added to the empty string, declared befor loop,
        encrypted += crypt_message
    return encrypted
print(vigenere(args.message, args.key))
