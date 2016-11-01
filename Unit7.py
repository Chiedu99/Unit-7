# Chiedu Nduka-eze November 1st
# This program encodes a string and decodes an encoded string


def getEDQ():
    """This function asks the user for encoding, decoding, or quiting"""
    EDQ = input("Do you want to encode, decode, or quit?")
    return EDQ


def encode():
    """This function encodes the user string"""
    userString = input("please give me a scentence to encode:")
    stringRotation = int(input("please give me the rotating number:"))
    x = stringRotation
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shiftedAlphabet = alphabet[x:] + alphabet[:x]
    encodedString = ""
    for x in userString.lower():
        pie = alphabet.index(x)
        encodedString += shiftedAlphabet[pie]
    print(encodedString)


def decode():
    """This function decodes an encoded string"""
    userstring = input("Please give me your string:")
    stringRotation = int(input("give me the shift key:"))
    x = stringRotation
    alphabetstring = "abcdefghijklmnopqrstuvwxyz"
    shiftedAlphabet = alphabetstring[x:] + alphabetstring[:x]
    decodeString = ""
    for x in userstring.lower():
        pie = shiftedAlphabet.index(x)
        decodeString += alphabetstring[pie]
    print(decodeString)


def main():
    userChoice = getEDQ()
    if userChoice == "encode":
        encode()
    elif userChoice == "decode":
        decode()
    else:
        print("leave then.")

main()
