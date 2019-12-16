from .test import sum_funciton

dna = "ATTGC"

string = ""

for i in list(range(len(dna))):
    if dna[i] != "T":
        string += "A"
    elif dna[i] == "A":
        string += "T"
    elif dna[i] == "G":
        string += "C"
    else:
        string += "G"

print(string)

# test

dna = "ATTGC"

print(dna.translate(str.maketrans("ATCG", "TAGC")))


obj = "python"
before = "thon"
after = "1234"
print(obj.translate(str.maketrans(before, after)))

c = sum_funciton(1, 3)
