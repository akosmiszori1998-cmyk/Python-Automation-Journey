from miniCloud import FelhoEroforras

class Tarhely(FelhoEroforras):
    def __init__(self,nev,kapacitas_gb):
        super().__init__(nev)
        self.kapacitas = kapacitas_gb
        self.foglalthely = 0

    def adat_feltoltes(self,mennyiseg):
        uj_foglalt_hely = self.foglalthely + mennyiseg

        if uj_foglalt_hely <= self.kapacitas:
            self.foglalthely = uj_foglalt_hely
            print(f"{mennyiseg} GB feltöltve. (Hely: {self.foglalthely}/{self.kapacitas} GB")
            return True
        else:
            print(f"Hiba, A tárhely megtelt!")
            return False
                
