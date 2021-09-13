### Used as practice for importing custom modules.

def load(my_character, foe_list, location_list, Location, Character, item_list):
    try:
        with open("save_game.txt", "r") as file_object:
            lines = file_object.readlines()
            lines = list(lines)
            for line in lines:
                line = line.strip()
                for foe in foe_list:
                    if foe.name in line:
                        res_int = int(line.replace(f"{foe.name},", ""))
                        foe.hp = res_int
                for location in location_list:
                    if location.name in line:
                        res_bool = (line.replace(f"{location.name},", ""))
                        location.discovered = eval(res_bool)
                if "my_character_name" in line:
                    my_character.name = str(line.replace("my_character_name,", ""))
                elif "my_character_attack" in line:
                    my_character.attack = int(line.replace("my_character_attack,", ""))
                elif "my_character_hp" in line:
                    my_character.hp = int(line.replace("my_character_hp,", ""))
                elif "my_character_speed" in line:
                    my_character.speed = int(line.replace("my_character_speed,", ""))
                elif "my_character_money" in line:
                    my_character.money = int(line.replace("my_character_money,", ""))
                elif "inventory_item" in line:
                    item_name = str(line.replace("inventory_item,", ""))
                    for item in item_list:
                        if item.name == item_name:
                            my_character.inventory.append(item)
                elif "my_character_badge_count" in line:
                    my_character.badge_count = int(line.replace("my_character_badge_count,", ""))
                elif "armour_item" in line:
                    armour_name = str(line.replace("armour_item,", ""))
                    for item in item_list:
                        if item.name == armour_name:
                            my_character.armour = item
                elif "weapon_item" in line:
                    weapon_name = str(line.replace("weapon_item,", ""))
                    for item in item_list:
                        if item.name == weapon_name:
                            my_character.weapon = item
                elif "undiscovered_locations" in line:
                    Location.undiscovered_locations = int(line.replace("undiscovered_locations,",""))
                elif "foes_remaining" in line:
                    Character.foes_remaining = int(line.replace("foes_remaining,", ""))
                elif "wins" in line:
                    Character.wins = int(line.replace("wins,", ""))
                elif "losses" in line:
                    Character.losses = int(line.replace("losses,", ""))
    except FileNotFoundError:
        print("File not found")
