# 5. feladat, CI beüzemelése

A projekt alapból tartalmazott egy Travis CI-t, vsizont mi saját magunknak szerettünk volna egy új CI-t beüzemelni, így a Github Actionsre esett a választásunk. Először azt valósítottuk meg, hogy a unit tesztek automatikusan lefussanak. 
Itt egy kis path probléma adódott, de azt megoldva sikerült elérni, hogy a unit testek automatikusan futnak.
Ezután új tesztek fejlesztése előtt a codecov.io-t is hozzákötöttük ehhez a CI folyamathoz, hogy folyamatosan tudjuk a kódunk lefedettségét monitorozni.
