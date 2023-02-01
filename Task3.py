#Task 3
def jainsall(liste):

  N = len(liste) #using len() to get the total numbers of elements

  teller = sum(liste) #
  nevner = sum(i**2 for i in liste) #for løkke fordi vi ikke vet hvor mange elementer det er som forrige oppgave
  return (teller**2) / (N * nevner) #teller/nevner


bw = []
with open ("/Users/dibashishegar/Documents/GitHub/Datasikkerhet og skytjenester/LAB1/Lab1-Datanettverk-og-skytjenester/data.txt") as file:#kode fra timen den 31.01.2023
    for line in file: 
        print(line.split()) #tar en string og gjør den om til en liste av strings som separeres med mellomrom. hele lista tas inn her
        bw.append(int(line.split()[0])) #legger til i lista bw       

result = jainsall(bw)
print("The JFI is", result)