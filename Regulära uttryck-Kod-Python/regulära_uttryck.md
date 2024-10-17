## Tupler
- Är lik listor i Python. Precis som listor har de en ordning och kan innehålla dubbletter och olika typer.
#### En viktig skilland:
- En Tupel går inte att ändra, den är oföränderlig.
- Eftersom en Tupel inte går att ändra kan Python använda Tupler effektivare än listor. Exempel så tar det mindre plats i minnet. Tupplers oförändlighet gör också att det kan användas som lexikon och mängder.
#### Kod: 
- Python-Tuppel med noll objekt --> ()
- Python-Tuppel med objekt --> (1,2,3,4) anger kommaseparerade värden inom parantesen
- Exempel på saker som går att göra med listor som också går att göra med tupler.
min_tupel = (2, 3, 5, 7, 11)
print(min_tupel[0]) #skriv ut det första elementet
print(min_tupel[0:3]) #de första tre elementen
print(5 in min_tupel) #finns 5 i tupeln? #True or False
#### Fel:
- om man försöker ändra i en tupel skrivs ett felmeddelande ut.
- Exempel:
tupel = ("a", "a", "c")
tupel [1] = "b" #Fel

## Listor
- Lista kan även kallas array, lista eller vektor i programmerings språk. Dock i Python så används ordet Lista.
- En lista kan innehålla vilken datatyp som helst, heltal, nummer, namn, ord osv.
- En lista tillåter dubletter. Man kan också ha en lista inuti en lista för att skapa en matris eller tvådimensionell lista.
- I en lista börjar man alltid räkna från noll. Det första elementet har index 0.
- Exempel:
frukter = ["Äpple", "Banan", "Mango"]
print(frukter[0]) #För att läsa andra elementet skriv frukter[1]

- Man kan även använda negativa index för att gå baklänges från slutet i listan.
- Exempel:
frukter = ["Äpple", "Banan", "Mango"]
print(frukter[-1]) #För att läsa sista elementet(Mango). [-2] för näst sista osv.

#### Lägga till och ta bort element
- För att skapa en tom lista kan man skriva: frukter = []
- För varje lista som skapas så kan man använda funktioner som .append() och .pop()
- .append() --> För att lägga till element i listan. Det nta elementet hamnar sist i listan när det printas.
- .pop(index) --> kan användas för att ta bort elementet på plats index ur listan.

- Exempel på att lägga till och ta bort element från en tom lista:
* frukter = []
* frukter.append('Äpple')
* frukter.append('Banan')
* frukter.append('Mango') #frukter = ['Äpple', 'Banan', 'Mango']
* print(f'frukter = {frukter}')

* frukter.pop(0) #ta bort första elementet, 'Äpple'.
* print('frukter = ' + str(frukter))
* frukter.pop(-1) #ta bort sista elementet, 'Mango'.
* print('frukter = ' + str(frukter))
- output:
* frukter = ['Äpple', 'Banan', 'Mango']
* frukter = ['Banan', 'Mango']
* frukter = ['Banan]
