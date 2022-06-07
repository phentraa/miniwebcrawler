### Python3 alapok gyakorló feladat - ProgMasters
Kovács Péter, 2022.06.07. 
# MiniWebCrawler

A csomag oktatási célja, hogy segítse a Python programozási nyelv alapjainak elsajátítását 
egy gyakorlatban is használható segédeszköz növekményes leprogramozásán keresztül.
A produktum egy kis parancssori program lesz, ami

- parametrizálható
- GET kérésen keresztül lehív egy megadott url-en található HTML forráskódot  
- Ebben kigyűjti az összes linkben található url-t regex kifejezések segítségével
- A megadott mélységig rekurzívan ismétli a folyamatot
- A megadott paraméter alapján vagy fájlba vagy konzolra, behúzások használatával kiírja a gyűjtött adatokat

Konkrét oktatási lépéseket nem adok meg, de az egyes iterációs py fájlok tartalmazzák a rájuk vonatkozó célokat is.

## Lefedett témák

- Szöveg kiíratása, formázott stringek
- Típusok és változók használata (lokális/globális)
- Listák
- Feltételek (if-else) és ciklusok (for)
- Függvények
- Saját csomagok kezelése (from...import)
- Külső csomagok (request, re, click)
- Reguláris kifejezések
- Rekurzivitás
- Dekorátorok használata (parametrizálás click-el)

## Iterációk futtatása
A crawler mappában található __crawler_main.py__ használható az 1.,2. és 3. iteráció futtatására.
Írjuk át a
```Python
from crawler_iterations import crawler_iteration_N as crawler
```
sorban a behúzni kívánt verziót. Ez lehet bármi, a lényeg, hogy rendelkezzen egy meghívható run() metódussal.

A 4. iterációt megvalósító __crawler_cli.py__ önmagában futtatható.

## Iterációk tartalma
1.iteráció: **crawler_iterations/crawler_iteration_1.py**
- requests csomag importálása
- GET kérés küldése
- RESPONSE fogadása/dekódolása
- érték kiíratása konzolra

2.iteráció: **crawler_iterations/crawler_iteration_2.py**
- függvényekbe szervezés
- RESPONSE státuszkódjának ellenőrzése
- reguláris kifejezések használata  ('<a href=...>' ill. az azokban található url-ek)

3.iteráció: **crawler_iterations/crawler_iteration_3.py**
- rekurzivitás megvalósítása max. 1 mélységig
- már vizsgált linkek gyűjtése listába (önismétlés elkerülése miatt)
- behúzás alkalmazása az aktuális mélység függvényében

4.iteráció: **crawler_cli.py**
- click dekorátorok hozzáadása a main függvényhez (url, depth, file)
- paramétertől függő rekurzivitás és fájlba írás megvalósítása
