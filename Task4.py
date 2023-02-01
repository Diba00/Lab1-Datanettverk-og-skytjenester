#Task 4
def jainsall(liste):

  N = len(liste) #using len() to get the total numbers of elements

  teller = sum(liste) #
  nevner = sum(i**2 for i in liste) #for løkke fordi vi ikke vet hvor mange elementer det er som forrige oppgave
  return (teller**2) / (N * nevner) #teller/nevner


bw = []
with open ("/Users/dibashishegar/Documents/GitHub/Datasikkerhet og skytjenester/LAB1/Lab1-Datanettverk-og-skytjenester/data1.txt") as file:
    for line in file:
        data = line.split()
        print ("check", data[0], data[1])
        value = float(data[0])
        if data[1] == "Kbps":
          value = value/1000  
        bw.append(value)

print (bw)
result = jainsall(bw)

print("The JFI is", result)