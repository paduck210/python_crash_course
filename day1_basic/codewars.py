dna = "ATTGC"

string = ""

for i in list(range(len(dna))):
  if dna[i] == "T":
    string += "A"
  elif dna[i] == "A":
    string += "T"
  elif dna[i] == "G":
    string += "C"
  else:
    string += "G"

print(string)





dna = "ATTGC"
print(dna.translate(string.maketrans("ATCG","TAGC")))


obj = "python"
before = "thon"
after = "zzzz"
print(obj.translate(string.maketrans(before,after)))
