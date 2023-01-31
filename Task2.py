#Task 2
def jainsall(liste):

  N = len(liste) #using len() to get the total numbers of elements

  teller = sum(liste) #
  nevner = sum(i**2 for i in liste) #for løkke fordi vi ikke vet hvor mange elementer det er som forrige oppgave
  return (teller**2) / (N * nevner) #teller/nevner

result = jainsall([1, 2])
print("The JFI is", result)
