# 1. feladat, statikus kódanalízis

A statikus kódanalízist a SonarCloud és SonarLint eszközökkel végeztük.
A SonarCloud mutatott olyan bugokat, amik valójában nem voltak bugok a kódban, például egy tesztben, ahol az elvárt eredmény 0 volt, hibának jelezte a SonarClour azt, hogy egy "-" operátor két oldalán azonos dolog volt. Ezt a SonarCloud Issues oldalán Resolved as False positivenek jelöltem. Voltak viszont valós problémák, például exception dobás utáni return, ami tényleg elérhetetlen kód, ezt a kódban kellett kijavítani. Megtanultuk ebből, hogy a statikus analízis eszköz is tévedhet, és figyelemmel kell eljárni a kódjavításkor.  
Emellett a code smelleket is megnéztük, azt nem mindet javítottuk ki, mert nagyon sok volt(260-nál több). 
  
Volt közöttük:
- Kikommentezett kód
- Túl komplex függvény
- Nem használt lokális változó
- Változó, ami beépített változó/függvény nevét kapta, így azt "beárnyékolja" (shadowing)
- Nem megfelelő nevű változó (nem követi a PEP 8 irányelvet)
- String literal, többször felhasználva, ahelyett, hogy konstans változóban lenne tárolva
- Kikommentezett kód
- Tagváltozó, ami az osztály nevével rendelkezik

Ezek közül nem mindet javítottuk, viszont súlyosság szerint megnéztük azokat, és átnéztük, hogy valós problémát jelentenek-e.
