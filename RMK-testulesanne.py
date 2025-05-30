from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Aeg, mis kulub Rital liigeldes
kodust_bussipeatus = timedelta(seconds=300)
bussisoit = timedelta(minutes=13)
bussipeatusest_toole = timedelta(seconds=240)

# koosoleku aeg
koosolek = datetime.strptime("09:05", "%H:%M")

#Bussi graafiku loomine, et saaks täpsemalt arvutada, millal bussid liiguvad.
def bussigraafik(algus="08:05", lopp="08:59", interval_minutites=10):
    graafik = []
    algusaeg = datetime.strptime(algus, "%H:%M")
    lopp_aeg = datetime.strptime(lopp, "%H:%M")
    hetkeaeg = algusaeg

    while hetkeaeg <= lopp_aeg:
        graafik.append(hetkeaeg)
        hetkeaeg += timedelta(minutes=interval_minutites)
    return graafik

# Kontrollib kas Rita jõuab koosolekule õigeks ajaks või mitte.
def saabumine(lahkumise_aeg, bussigraafik):
    lahkumise_aeg = datetime.strptime(lahkumise_aeg, "%H:%M")

    # Millal Rita jõuab bussipeatusesse
    bussipeatuses = lahkumise_aeg + kodust_bussipeatus

    # Otsib bussigraafikust bussi, mis läheb, kui Rita jõuab bussipeatusesse
    sobiv_buss = next((buss for buss in bussigraafik if buss >= bussipeatuses), None)
    if not sobiv_buss:
        return True
    
    # Aruvtamine, millal Rita jõuab tööle
    saabumine_toole = sobiv_buss + bussisoit + bussipeatusest_toole
    return saabumine_toole > koosolek

def simulatsioon():
    bussid = bussigraafik ()
    ajad = []
    hilinemised = []

    algus = datetime.strptime("08:00", "%H:%M")
    lopp = datetime.strptime("09:00", "%H:%M")
    hetkeaeg = algus

    while hetkeaeg <= lopp:
        aeg = hetkeaeg.strftime("%H:%M")
        ajad.append(hetkeaeg)
        hilineb = saabumine(aeg, bussid)
        hilinemised.append(1 if hilineb else 0)
        hetkeaeg += timedelta(minutes=1)
    # Graafiku joonistamine
    plt.style.use("dark_background")
    plt.figure(figsize=(8, 5))
    plt.plot(ajad, hilinemised, color="red", linewidth=4)
    plt.xlabel("Millal Rita kodust lahkub")
    plt.ylabel("Jääb hiljaks")
    plt.title("Tõenäosus kas Rita hilineb koosolekule.")
    plt.ylim(-0.05, 1.05)
    plt.grid(True, linestyle="--", alpha=0.2)
    plt.tight_layout()
    plt.show()

# Käivitamine
simulatsioon()