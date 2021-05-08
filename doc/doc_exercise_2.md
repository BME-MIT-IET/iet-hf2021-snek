# 2. feladat, egységtesztelés

Az egységtesztelés során a célunk közös megegyezés alapján az lett, hogy lehetőleg az összes fontosabb algoritmus legyen tesztelve. Így tehát a százalékos értékekre mentünk rá, hanem azt tartottuk a legfontosabbnak, hogy jelentőségteljes teszteket írjunk. Ez úgy gondolom siekrült is, hiszen sok tesztnél a kódba is bele kellett nyúlnunk, ennek okai a következők voltak:
- a függvényeknek nem volt visszatérési értéke, csupán valamit kiírt a standard kimenetre
- volt olyan függvény, melynek implementációja python3-as környezetben nem futott le
- néhány algoritmus rossz helyen volt, illetve intuitívan nem ott keresné a fejlesztő

A tesztesetek során többször csupán elírás oka volt, hogy egy adott algoritmus nem volt ellenőrizve, ezt is javítottuk. 

Összességében úgy gondolom, hogy az egységtesztjeink a kód minőségén és átláthatóságán is javítottak. Sikerült elérnünk, hogy a legtöbb algoritmusra legyen tesztünk, így a célunkat e téren sikeresen teljesítettük. 
