boodschappenlijst = ["melk", "brood", "eieren", "boter", "kaas"]


boodschappenlijst.append("appels")
boodschappenlijst.append("yoghurt")


boodschappenlijst.remove("boter")


print(f"Aantal producten op de boodschappenlijst: {len(boodschappenlijst)}")


print(f"Boodschappenlijst: {boodschappenlijst}")


product = "eieren"
if product in boodschappenlijst:
    print(f"{product} staat op de boodschappenlijst.")
else:
    print(f"{product} staat niet op de boodschappenlijst.")
