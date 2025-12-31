class ElectricVehicle:
    def __init__(self,modell,indulo_akku):
        self.modell = modell
        self.akkuszint = indulo_akku

    @property
    def akkuszint(self):
        return self._akkuszint
    
    @akkuszint.setter
    def akkuszint(self,ertek):
        if ertek > 100:
            print("HIBA, az akku. értéke nem haladhatja meg: 100")
            self._akkuszint = 100
        elif ertek < 0:
            print("HIBA, az akku értéke nem lehet kisebb 0-nál")
            self._akkuszint = 0
        else:
            self._akkuszint = ertek
    
    @staticmethod
    def toltesi_ido_becsles(hany_szazalek, tolto_teljesitmeny):
        return hany_szazalek / tolto_teljesitmeny

    @classmethod
    def auto_konfig(cls,adat_string):
        adat = adat_string.split(";")

        modell = adat[0]
        akku = int(adat[1])
        extra = adat[2]

        if extra == "Autopilot":
            print(f"Tesla rendelés előkészítés: {modell}....")
            return Tesla(modell,akku,True)
        else:
            print(f"Sima elektromos autó rendelés: {modell}...")
            return cls(modell,akku)
        
class Tesla(ElectricVehicle):
    def __init__(self,modell,indulo_akku,onvezeto_mod):
        super().__init__(modell,indulo_akku)
        self.onvezeto = onvezeto_mod

    def hatotav_becsles(self):
        alap_hatotav = self.akkuszint*5
        if self.onvezeto :
            print("Önvezető mód aktív: 20 százalék fogyasztás korrekció")
            return alap_hatotav*0.8
        
        return alap_hatotav
    
auto1 = ElectricVehicle.auto_konfig("Modell 3;90;Autopilot")

auto1.akkuszint = 150

print(f"Hatótáv: {auto1.hatotav_becsles()} km")

ido = ElectricVehicle.toltesi_ido_becsles(40,11)
print(f"Becsült töltési idő: {ido} óra")