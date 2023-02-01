#Task 4
def jainsall(liste):

  N = len(liste) #using len() to get the total numbers of elements

  teller = sum(liste) #
  nevner = sum(i**2 for i in liste) #for løkke fordi vi ikke vet hvor mange elementer det er som forrige oppgave
  return (teller**2) / (N * nevner) #teller/nevner


bw = []
with open ("data1.txt") as file:
    for line in file:
        print(line.split())
        bw.append(int(line.split()[0]))


result = jainsall(bw)
print("The JFI is", result)