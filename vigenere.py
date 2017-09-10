import argparse

parser = argparse.ArgumentParser(description='vigenère encryption with message and key')
parser.add_argument('-m', '--message', type=str, metavar='', required=True, help='message to encrypt')
parser.add_argument('-k', '--key', type=str, metavar='', required=True, help='key to encrypt with')
args = parser.parse_args()

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'å', 'ä', 'ö', ' ']
def find_num_in_list(list, letter):
    x = 0
    while letter != list[x]:
        x += 1
    if letter == list[x]:
        return x

def vigenere(message, key):
    x = 0
    encrypted = ''
    while x < len(message):
        crypt_message = alpha[(find_num_in_list(alpha, message[x : x + 1])
        + find_num_in_list(alpha, key[x % len(key)])) % len(alpha)]
        x += 1
        encrypted += crypt_message
    return encrypted
print(vigenere(args.message, args.key))
