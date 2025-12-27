MiniCloud Manager - OOP Projekt

Ez egy Python alapú felhőerőforrás-kezelő szimuláció, amelyet az objektumorientált programozás (OOP) alapelveinek gyakorlására készítettem.

Funkciók
Szerverek kezelése: Virtuális gépek létrehozása CPU és RAM specifikációkkal.
Tárhely kezelés: Adattárolók létrehozása fix kapacitással és feltöltési logikával.
Állapotkezelés: Erőforrások indítása és leállítása.

Felépítés
A projekt négy fő modulból áll:
1. `miniCloud.py` - Az ősosztály (`FelhoEroforras`), amely a közös tulajdonságokat tartalmazza.
2. `server.py` - A `VirtualisGep` osztály, amely a számítási kapacitásért felel.
3. `tarhely.py` - A `Tarhely` osztály az adatkezeléshez.
4. `main.py` - A program belépési pontja, ahol a példányosítás történik.

Használat
Futtasd a fő fájlt a terminálból:
```bash
python main.py
