monster_health = 150
player_damage = 25


aantal_aanvallen = 0


while monster_health > 0:
    monster_health = monster_health - player_damage

    if monster_health < 0:
        monster_health = 0
    aantal_aanvallen = aantal_aanvallen + 1
    print(f"Het monster heeft nog {monster_health} health over.")

print(f"Het monster is verslagen na {aantal_aanvallen} aanvallen!")


monsters = [100, 200, 150]


for monster_index in range(len(monsters)):
    monster_health = monsters[monster_index]
    aantal_aanvallen = 0

    while monster_health > 0:
        monster_health = monster_health - player_damage
        if monster_health < 0:
            monster_health = 0
        aantal_aanvallen = aantal_aanvallen + 1
        print(f"Monster {monster_index + 1} heeft nog {monster_health} health over.")

    print(f"Monster {monster_index + 1} is verslagen na {aantal_aanvallen} aanvallen!\n")
