#Task 4
def jainsall(liste):

  N = len(liste) #using len() to get the total numbers of elements

  teller = sum(liste) #
  nevner = sum(i**2 for i in liste) #for løkke fordi vi ikke vet hvor mange elementer det er som forrige oppgave
  return (teller**2) / (N * nevner) #teller/nevner


bw = []
with open ("/Users/dibashishegar/Documents/GitHub/Datasikkerhet og skytjenester/LAB1/Lab1-Datanettverk-og-skytjenester/data1.txt") as file:
    for line in file:
        data = line.split() #Får det linje for linje 
        #print(line.split()) Dette hadde skrevet linje for linje som i oppg 3 med ['7', 'Mbps']
        print ("check", data[0], data[1]) #tar ikke inn hele lista som i oppg 3
        value = float(data[0]) #tallene i kolonne 1 skal være float
        if data[1] == "Kbps": #if setning, hvis vi støter på Kbps skal vi dele verdien på 1000 for å få Mbps
          value = value/1000  
        bw.append(value) # use append to add an item to a list, so we add the value in our list

print (bw) #printer ut [7.0, 1.2, 15.0, 32.0]
result = jainsall(bw)

print("The JFI is", result) #printer resultatet