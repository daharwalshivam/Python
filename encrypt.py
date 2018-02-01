alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = int(input('enter the key you want to use for encryption : '))
code = list(input('enter word to be encrypted: '))
new = []
encrypted = ''
for element in code:
    pos = alphabet.find(element)
    if (key + pos) >= 26:
        pos = (key + pos) % 26
        new.append(alphabet[pos])
    else:
        new.append(alphabet[key + pos])

for each in new:
    encrypted = encrypted + each
print(encrypted)
