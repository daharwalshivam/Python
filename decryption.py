alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = int(input('enter the decryption key in integers : '))
code = list(input('enter word to be decrypted: '))
new = []
new_ = []
decrypted = ''
decrypted_ = ''
for element in code:
    pos = alphabet.find(element)
    if (pos - key) >= -26:
        new_.append(alphabet[pos - key])

    elif (pos - key) < -26:
        pos = (pos - key)%26
        new_.append(alphabet[pos])

    if (key + pos) < 26:
        new.append(alphabet[key + pos])

    elif (key + pos) >= 26:
        pos = (key + pos)%26
        new.append(alphabet[pos])

for each in new:
    decrypted = decrypted + each
print(decrypted)
for each_ in new_:
    decrypted_ = decrypted_ + each_
print(decrypted_)
