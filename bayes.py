pAF = int(input())
print("The probability that it is Friday and that a student is absent :", pAF)

pF = int(input())
print("The probability that it is Friday : ", pF)

pResult = (pAF / pF)

print("The probability that a student is absent given that today is Friday :", pResult * 100, "%")
