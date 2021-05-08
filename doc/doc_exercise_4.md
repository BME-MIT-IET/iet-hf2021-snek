# 4. feladat, Behavior-driven development

A BDD gyakorlására a pythonos behave könyvtárat használtuk fel. A behave a cucumber semi-official pythonos implementációja, a többi cucumber eszközben megismert Gherkin syntaxot alkalmazza.   
Az algoritmusok két részhalmazát teszteltük le, a kereséseket, illetve a rendezéseket.

A tesztek létrehozása során próbáltuk szem előtt tartani a célt, hogy valós környezetben akár egy üzleti kolléga is tudjon teszteseteket definiálni és futtatni. Ennek elérése érdekében nem bonyolítottuk túl a teszteseteket: Scenario Outlinet használva csak annyi feladata van az esetleges üzleti kollégának hogy definiálja a bemeneti paramétereket, például hogy milyen algoritmust teszteljünk vagy hogy mi az elvárt eredmény.  

Mivel dolgoztam már olyan környezetben, ahol elméletben az üzletnek kéne meghatározni a teszteseteket, de gyakorlatban a hozzá nem értés miatt nekem, mint fejlesztőnek kellett az üzlet teszteseteit is definiálnom, így könnyű volt belátni hogy hasznos lehet ezt a technológiát használni. 
