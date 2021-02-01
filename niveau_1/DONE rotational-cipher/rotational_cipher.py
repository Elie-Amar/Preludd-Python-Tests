def rotate(text, key):
    res = ""
    for i in range(len(text)):
        char = text[i]
        if(char.isalpha()): # if it's a letter
            if (char.isupper()): # if is uppercase
                res += chr((ord(char) + key - 65) % 26 + 65)
            else: # if is lowercase
                res += chr((ord(char) + key - 97) % 26 + 97)
        else:
            res += char
    return res
