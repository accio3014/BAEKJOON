dial_alphabet = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

alphabet = input()
time = 0
for i in alphabet:
    for j in dial_alphabet:
        if(i in j):
            time +=  dial_alphabet.index(j) + 3

print(time)