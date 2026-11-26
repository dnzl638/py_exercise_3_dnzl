# !/usr/bin/env python3

"""
.. moduleauthor:: Deniz Litschauer <denizl.litschi@gmail.com>
"""

def encode(text):
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            shifted = chr((ord(char)- ord('a') + 13) % 26 + ord('a'))
            result.append(shifted)
        elif 'A' <= char <= 'Z':
            shifted = chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
            result.append(shifted)
        else:
            result.append(char)
    return "".join(result)

def decode(text):
    return encode(text)

if __name__ == "__main__":
    sample = "Arire gehfg nalbar"
    print("Decoded:", decode(sample))
