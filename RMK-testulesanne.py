from datetime import datetime, timedelta

# Tööle jõudmiseks minevad ajad
kodust_bussipeatus = timedelta(minutes=5)
bussisoit = timedelta(minutes=18)
bussipeatusest_toole = timedelta(minutes=4)
koosolek = datetime.strptime("09:05", "%H:%M")
# Sõiduks kuluva aja arvutus
soiduaeg = kodust_bussipeatus + bussisoit + bussipeatusest_toole

# Tööle jõudmise aja arvutus
def saa_saabumise_staatus(lahkumise_aeg_str):
    lahkumise_aeg = datetime.strptime(lahkumise_aeg_str, "%H:%M")
    saabumise_aeg = lahkumise_aeg + soiduaeg
    saabumise_str = saabumise_aeg.strftime("%H:%M")

    if saabumise_aeg <= koosolek:
        print("Jõuad kohale!")
    else:
        print("Ei jõua!")

lahkumise_aeg = "08:39"
tulemus = saa_saabumise_staatus(lahkumise_aeg)
print(tulemus)
