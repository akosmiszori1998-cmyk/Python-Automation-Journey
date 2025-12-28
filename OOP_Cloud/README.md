Felhő Szerver Szimulátor OOP alapokon

Ez a projekt a haladó Python objektumorientált programozási koncepciókat mutatja be egy felhőalapú infrastruktúra szimulációján keresztül.

Megvalósított koncepciók: Az öröklődés során a DatabaseServer osztály a CloudServer képességeit kapja meg és egészíti ki. 
A Class és Static metódusok közül a classmethod a konfigurációs szövegek feldolgozását végzi, a staticmethod pedig az adatok ellenőrzését.
Az adatvédelem érdekében privát és védett attribútumokat használtunk az osztályokon belül. 
A JSON mentés során az adatok automatikusan fájlba kerülnek a dict attribútum segítségével.
Fájlok listája: A main.py a program indításáért felel. A cloudinfrautomat.py tartalmazza az alaposztályt és a fő logikát. 
A database.py tartalmazza a speciális adatbázis szerver osztályt.
