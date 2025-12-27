from miniCloud import FelhoEroforras

class VirtualisGep(FelhoEroforras):
    def __init__(self,nev,cpu,ram):
        super().__init__(nev)
        self.cpu = cpu
        self.ram = ram
        self.bekapcsolva = False


    def inditas(self):
        if self.bekapcsolva == False:
            self.bekapcsolva = True
            print(f"A/az {self.nev} szerver elindult")
        else:
            print("Hiba: A gép már fut")

    def leallitas(self):
        if self.bekapcsolva == True:
            self.bekapcsolva == False
            print(f"A/az {self.nev} szerver leállt")
        else:
            print("Hiba: A gép már nem fut")
              