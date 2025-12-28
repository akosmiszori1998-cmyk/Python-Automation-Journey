#from cloudinfrautomat import CloudServer
from database import DatabaseServer

elso_szerver = DatabaseServer("RR-MainServer",16,32,"SQL")

elso_szerver.mentes_jsonbe()
#Eredmény:
#{"nev": "RR-MainServer", "cpu": 16, "ram": 32, "tipus": "SQL"}