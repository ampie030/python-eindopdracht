cijfer_vak_1 = 6.0
cijfer_vak_2 = 3.5
cijfer_vak_3 = 7.0


gemiddelde = (cijfer_vak_1 + cijfer_vak_2 + cijfer_vak_3) / 3


if cijfer_vak_1 < 4 or cijfer_vak_2 < 4 or cijfer_vak_3 < 4:
    print("Gezakt!")

elif gemiddelde >= 5.5:
    print("Geslaagd!")
else:
    print("Gezakt!")