import json
class CloudServer:

    def __init__(self,nev,cpu,ram):
        self.nev = nev
        self.cpu = cpu
        self.ram = ram

    def mentes_jsonbe(self):
        with open(self.nev + ".json","w") as f:
            json.dump(self.__dict__,f)

    @classmethod
    def from_config_string(cls,szetbont):
        adat = szetbont.split(';')
        
        nev = adat[0]
        cpu = int(adat[1])
        ram = int(adat[2])

        return cls(nev,cpu,ram)

    @staticmethod
    def is_valid_config(cpu,ram):
        return cpu > 0 and ram >= 2

