from cloudinfrautomat import CloudServer
class DatabaseServer(CloudServer):
    def __init__(self, nev, cpu, ram,db_tipus):
        super().__init__(nev, cpu, ram)
        self.tipus = db_tipus
    
