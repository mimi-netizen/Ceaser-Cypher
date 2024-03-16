# Caesar cipher.
text = input("Enter your message: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)

'''line 02: ask the user to enter the open (unencrypted), one-line message;
line 03: prepare a string for an encrypted message (empty for now)
line 04: start the iteration through the message;
line 05: if the current character is not alphabetic...
line 06: ...ignore it;
line 07: convert the letter to upper-case (it's preferable to do it blindly, rather than check whether it's needed or not)
line 08: get the code of the letter and increment it by one;
line 09: if the resulting code has "left" the Latin alphabet (if it's greater than the Z code)...
line 10: ...change it to the A code;
line 11: append the received character to the end of the encrypted message;
line 13: print the cipher.'''