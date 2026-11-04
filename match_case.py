player_class = "Warrior"


match player_class:
    case "Warrior":
        health = 150
        damage = 20
    case "Mage":
        health = 80
        damage = 35
    case "Archer":
        health = 100
        damage = 25
    case "Rogue":
        health = 90
        damage = 30
    case "Paladin":
        health = 180
        damage = 15
    case "Necromancer":
        health = 70
        damage = 40
    case _:
        health = None
        damage = None
        print(f"Onbekende class: {player_class}. Kies een geldige class.")


if health is not None:
    print(f"Gekozen class: {player_class}")
    print(f"Health: {health}")
    print(f"Damage: {damage}")
