def reverseWords():
    name=input("Nome: ")
    nameA = name.split()[::-1]
    nameB = []
    for i in nameA:
        nameB.append(i)
    print(" ".join(nameB))
reverseWords()