# Integrációs és Ellenőrzési Technikák - Ellenőrzési Technikák Házi Feladat

## A projekt célja:

 [Algorithms](https://github.com/keon/algorithms) repositoryhoz kódminőségének javítása, emellett különböző eszközök megismerése.   
 A projekthez alapból is léteznek unit testek, amiknek kódlefedettségét lemérjük, majd ezután teszteket fejlesztünk a kellő lefedettség eléréséhez. A lefedettségnél nem a 100%-ra törekszünk, hanem arra, hogy minden megvalósított algoritmus le legyen tesztelve, és az a teszt rendesen lefusson. Természetesen szükség szerint változtatunk az algoritmuson, hogy a tesztek ténylegesen a kódminőség javítása érdekében készüljenek.  
 Emellett statikusan is megvizsgáljuk a kódot, az úgy talált problémákat is átnézzük, megbeszéljük, ha kell, javítjuk.  
 Ezen ellenőrzésekhez beüzemelünk egy CI rendszert, hogy azok minden pushra fussanak, így később sem romlik majd el a kód minősége!  
 Néhány algoritmus futásidejét benchmarkokkal fogjuk mérni, így dokumentálni tudjuk azt, hogy a futási idejük tényleg megegyezik-e az ígérttel, jó-e az implementáció.  
 Azt is megtekintjük, hogy hogyan tudjuk BDD irányelvek szerint leírni az algoritmusokat, így megismerve a Pythonos BDD lehetőségeket.  
 Természetesen nem minden algoritmushoz fogunk BDD-t és benchmarkolást csinálni, mivel azokból nagyon sok van.

### Technológia fókusz
 - CI rendszer beüzemelése
 - Statikus analízis
 - Unit testek

### Termék/felhasználó fókusz
 - Teljesítmény benchmarking
 - BDD
