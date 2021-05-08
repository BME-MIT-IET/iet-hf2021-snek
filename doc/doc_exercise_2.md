# 2. feladat, egységtesztelés

Amikor megkaptuk a projektet, akkor a legtöbb függvényhez volt írva egységteszt, viszont ezen szerettünk volna javítani és minél inkább 100% felé vinni ezt a számot.
Ehhez a codecov.io-n lévő kódlefedettség mérőt vettük alapul és amelyik függvényt úgy ítéltük, hogy nincs eléggé letesztelve, azt átnéztük és javítottunk rajta.

A math mappában több ilyen függvényre is bukkantunk, viszont kiderült ennek nem az az oka, hogy nincsenek egységtesztek készítva hozzá, hanem, hogy a fejlesztők egy másik fájlban definiált függvényt nem importálták a fájla, hanem egyszerűen átmásolták.
Így a későbbi definíció lépett életbe és ezért volt alacsony a kódlefedettség ebben a mappában. 
Ezeket a duplikált kódokat helyettesítettük importokkal így javítva a kódminőséget, átláthatóságot és a kódlefedettséget is.
Ebben a mappában szerepelt még az rsa algoritmus is, ami nem volt tesztelve, de ennek a tesztjét a fejlesztők csak kikommentezték, mert túl sok időt vett igénybe (a saját számítógépemen 15 percet), amit nem szeretnék minden egyes commit-nál lefuttatni, ezért kikommentezve hagytuk.

A matrix mappában szerepelt egy algoritmus, melyhez egy időmérő tesztet készítettek a függvény alá, nem pedig a tests mappában, ezért azt áthelyeztük a megfelelő helyére.