# Indsamler brugernavne fra brugeren og gemmer dem i en liste

brugernavne = []

while True:
    brugernavn = input("Indtast et brugernavn (eller skriv 'stop' for at afslutte): ")
    
    if brugernavn.lower() == 'stop':
        break
    
    brugernavne.append(brugernavn)

print("Indsamlede brugernavne:")
for brugernavn in brugernavne:
    print(brugernavn)

