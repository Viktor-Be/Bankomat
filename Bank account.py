from Chernovik_fo_bank1 import RUbank
from Chernovik_fo_bank2 import ENbank
def Bankomat():
    while True:
        Language=(input("Please select a language:\n""1.Русский\n""2.English\n" ))
        if Language=="1":
            RUbank()
        elif Language=="2":
            ENbank()
Bankomat()