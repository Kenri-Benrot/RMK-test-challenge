from datetime import datetime, timedelta

# Aeg, mis kulub Rital liigeldes
kodust_bussipeatus = timedelta(seconds=300)
bussisoit = timedelta(minutes=13)
bussipeatusest_toole = timedelta(seconds=240)

# koosoleku aeg
koosolek = datetime.strptime("09:05", "%H:%M")

#Bussi graafiku loomine, et saaks täpsemalt arvutada, millal bussid liiguvad.
def loo_bussigraafik(algus="08:05", lopp="08:59", interval_minutites=10):
    graafik = []
    algusaeg = datetime.strptime(algus, "%H:%M")
    lopp_aeg = datetime.strptime(lopp, "%H:%M")
    hetkeaeg = algusaeg

    while hetkeaeg <= lopp_aeg:
        graafik.append(hetkeaeg)
        hetkeaeg += timedelta(minutes=interval_minutites)
    return graafik

# Kontrollib kas Rita jõuab koosolekule õigeks ajaks või mitte.
def saa_saabumise_staatus(lahkumise_aeg_str, bussigraafik):
    lahkumise_aeg = datetime.strptime(lahkumise_aeg_str, "%H:%M")

    # Millal Rita jõuab bussipeatusesse
    bussipeatuses = lahkumise_aeg + kodust_bussipeatus

    # Otsib bussigraafikust bussi, mis läheb, kui Rita jõuab bussipeatusesse
    sobiv_buss = next((buss for buss in bussigraafik if buss >= bussipeatuses), None)
    if sobiv_buss is None:
        print("ei jõua tööle!")
        return False
    
    # Aruvtamine, millal Rita jõuab tööle
    saabumine_toole = sobiv_buss + bussisoit + bussipeatusest_toole
    
    # Esitab vastuse
    if saabumine_toole <= koosolek:
        print("Jõuad kohale!")
    else:
        print("Ei jõua!")

bussigraafik = loo_bussigraafik()
lahkumise_aeg = "08:40"
tulemus = saa_saabumise_staatus(lahkumise_aeg, bussigraafik)