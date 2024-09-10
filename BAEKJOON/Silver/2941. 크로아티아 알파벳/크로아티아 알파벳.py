words = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
alphabet = input()

for i in words :
    alphabet = alphabet.replace(i, '*')
print(len(alphabet))