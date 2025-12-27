from server import VirtualisGep
from tarhely import Tarhely

print("---- CLOUD MANAGER RENDSZER INDUL ----")

#1. Szerver addolás

web_server = VirtualisGep("Web-Server-01",4,16)

#2. Tárhely létrehozás

kepek_backup = Tarhely("Kepek-Backup",50)

print(f"\nEszközök státusza:")
print(f"{web_server}")
print(f"{kepek_backup}")
print(f"\n--- {web_server.nev} Műveletek ---")
#Teszteled a Szervert
web_server.inditas()
web_server.inditas()
web_server.leallitas()

#Teszteled a tárhelyet
kepek_backup.adat_feltoltes(40)
#kepek_backup.adat_feltoltes(20)  Hibát dob helyesen 




