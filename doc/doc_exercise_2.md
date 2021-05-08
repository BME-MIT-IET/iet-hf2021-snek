# 2. feladat, egységtesztelés

Amikor megkaptuk a projektet, akkor a legtöbb függvényhez volt írva egységteszt, viszont ezen szerettünk volna javítani, úgy, hogy a legtöbb algoritmusra legyen teszt és minél inkább 100% felé vigyük a lefedettséget.
Ehhez a codecov.io-n lévő kódlefedettség mérőt vettük alapul és amelyik függvényt úgy ítéltük, hogy nincs eléggé letesztelve, azt átnéztük és javítottunk rajta.

Tipikusabb hibák az egységtesztek során:

- a függvényeknek nem volt visszatérési értéke, csupán valamit kiírt a standard kimenetre
- volt olyan függvény, melynek implementációja python3-as környezetben nem futott le
- néhány algoritmus rossz helyen volt, illetve intuitívan nem ott keresné a fejlesztő
- az algoritmusok másik fájlba nem importálva lettek, hanem be lettek másolva, így duplikációt okoztak és megzavarták a kódlefedettséget is
- az egyik algoritmus alá volt definiálva egy időmérő teszt, nem pedig a tests mappába

Ezeket a hibákat természetesen kijavítottuk és teszt hiánya esetén új teszteket is írtunk.

Megjegyzés: Az rsa-hoz tartozó teszt jelenleg ki van kommentezve, mert sok idő a lefutása és nem szeretnénk minden egyes commit-kor CI-vel kivárni a futását.

Összességében úgy gondolom, hogy az egységtesztjeink a kód minőségén és átláthatóságán is javítottak. Sikerült elérnünk, hogy a legtöbb algoritmusra legyen tesztünk, így a célunkat e téren sikeresen teljesítettük. 
