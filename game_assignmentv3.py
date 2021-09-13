#modules
import random
from game_module import load


#classes w/ inheritance
class Item:
    """Item. (name, value). Contains sell function."""

    def __init__(self, name, value):

        self.name = name
        self.value = value


    def sell(self, character):
        sell_conf = "x"
        while sell_conf == "x":
            sell_conf = input(f"Are you sure you would like to sell your {self.name} for {self.value} gold? ")
            if sell_conf.lower() == "yes":
                character.money += self.value
                character.inventory.remove(self)
            elif sell_conf.lower() == "no":
                print("The shopkeeper asks you to leave for wasting his time.\
                \n")
                break
            else:
                print("Invalid Input. Please enter 'yes' or 'no'.\
                    \n ")
                sell_conf = "x"


class Weapon (Item):
    """Weapon. (name (iht), value(iht), attack)"""

    def __init__(self, name, value, attack):
        super().__init__(name, value)
        self.attack = attack


class Armour (Item):
    """Armour. (name (iht), value(iht), hp)"""

    def __init__(self, name, value, hp):
        super().__init__(name, value)
        self.hp = hp


class Location:
    """Locations. Functions include decision, discover and puzzle."""
    
    undiscovered_locations = 0
    current_location = 0 #used to position player at different locations which each have a different number. 0 is the Battle Hub where all adventuring begins.

    def __init__(self, name, number, description, discovered = False):
        self.name = name
        self.number = number
        self.description = description
        self.discovered = discovered
        Location.undiscovered_locations += 1


    def decision(self):
        direction_decision = "x"
        while direction_decision == "x":
            direction_decision = input(f"From The {self.name}, would you like to go left, right or back to the Battle Hub? ")
            print("")
            direction_decision = direction_decision.lower()
            if direction_decision == "left":
                Location.current_location += 1 #left child of binary tree
            elif direction_decision == "right":
                Location.current_location += 10 #right child of binary tree
            elif direction_decision == "back":
                Location.current_location = 0 #root node
                return Location.current_location
            else:
                print("Invalid input. Please enter 'left', 'right' or 'back'.\
                    \n ")
                direction_decision = "x"


    def discover(self,character):
        character.money -= 5 #adventuring costs 5 gold per turn regardless of new discovery
        if self.discovered == True:
            print(f"You have already discovered the secrets of The {self.name}")
        elif self.discovered == False:
            print(f"You have just discovered The {self.name}. {self.description}\
                \nThe {self.name} has an undiscovered badge within its boundary. This badge will allow you to \
                \nbattle the next foe at The Battle Hub and grant +5 points to your chosen attribute.\
                \n ")
            self.discovered = True
            Location.undiscovered_locations -= 1
        

    def puzzle(self, puzzle_no, character):

        #Button game. Random number generation allows different combination each time function called.
        if puzzle_no in [1, 20, 11]:
            print(f"On the ground in front of you, you notice 5 buttons. There is also a note inside a bottle that reads:\
            \nTo reveal the badge of The {self.name}, you must correctly press the buttons on the ground. They must be\
            \npress either 1, 2 or 3 times....but take care, as you must start from the beginning if you get any wrong.\
            \n")
            button_1 = random.randint(1, 3)
            button_2 = random.randint(1, 3)
            button_3 = random.randint(1, 3)
            button_4 = random.randint(1, 3)
            button_5 = random.randint(1, 3)
            choice_1 = 0 #must get all 5 correct or it returns to start with same numbers. 
            while choice_1 == 0:
                try:
                    choice_1 = int(input("How many times would you like to press the first button? "))
                except ValueError:
                    print("Enter a number, not a letter!\n ")
                    choice_1 = 0
                else:
                    if choice_1 == button_1:
                        print("Correct! Continue to the next button.\n ")
                        try:
                            choice_2 = int(input("How many times would you like to press the second button? "))
                        except ValueError:
                            print("Enter a number, not a letter\n ")
                            choice_1 = 0
                        else:
                            if choice_2 == button_2:
                                print("Correct! Continue to the next button.\n ")
                                try:
                                    choice_3 = int(input("How many times would you like to press the third button? "))
                                except ValueError:
                                    print("Enter a number, not a letter\n ")
                                    choice_1 = 0
                                else:
                                    if choice_3 == button_3:
                                        print("Correct! Continue to the next button.\n ")
                                        try:
                                            choice_4 = int(input("How many times would you like to press the fourth button? "))
                                        except ValueError:
                                            print("Enter a number, not a letter\n ")
                                            choice_1 = 0
                                        else:
                                            if choice_4 == button_4:
                                                print("Correct! Continue to the next button.\n ")
                                                try:
                                                    choice_5 = int(input("How many times would you like to press the fifth button? "))
                                                except ValueError:
                                                    print("Enter a number, not a letter!\n ")
                                                    choice_1 = 0
                                                else:
                                                    if choice_5 == button_5:
                                                        print(f"Congratulations! You have completed the puzzle and The {self.name} badge has revealed itself.\
                                                            \n ")

                                                        character.badge_count += 1
                                                        chosen_attribute = "x"
                                                        while chosen_attribute.lower() == "x":
                                                            chosen_attribute = input("Would you like to enhance your attack, health, or speed? ")
                                                            chosen_attribute = chosen_attribute.lower()
                                                            if chosen_attribute in ["attack", "health", "speed"]:
                                                                character.train(chosen_attribute)
                                                                character.money += 10
                                                            else:
                                                                print("Invalid input. Please enter 'attack', 'health' or 'speed'.\
                                                                    \n")
                                                                chosen_attribute = "x"
                                                        print("")

                                                    elif choice_5 != button_5:
                                                        print("Wrong! Start again.\n ")
                                                        choice_1 = 0   
                                            elif choice_4 != button_4:
                                                print("Wrong! Start again.\n ")
                                                choice_1 = 0
                                    elif choice_3 != button_3:
                                        print("Wrong! Start again.\n ")
                                        choice_1 = 0
                            elif choice_2 != button_2:
                                print("Wrong! Start again.\n ")
                                choice_1 = 0
                    elif choice_1 != button_1:
                        print("Wrong! Start again.\n ")
                        choice_1 = 0

        #riddle game x 3
        elif puzzle_no in [2, 21, 10]:
            print("A mysterious figure appears and tells you that in order for the badge to be revealed, you must\
                \nfirst complete a riddle...\n ")
            riddle_answer = "x"
            if puzzle_no == 2:
                while riddle_answer == "x":
                    riddle_answer = input(f"{character.name}, what must be broken before it can be used??? ")
                    if "egg" in riddle_answer.lower():
                        print(f"Correct!\
                            \nThe mysterious figure points you towards The {self.name} badge.\
                            \n")
                        character.badge_count += 1
                        chosen_attribute = "x"
                        while chosen_attribute.lower() == "x":
                            chosen_attribute = input("Would you like to enhance your attack, health, or speed? ")
                            chosen_attribute = chosen_attribute.lower()
                            if chosen_attribute in ["attack", "health", "speed"]:
                                character.train(chosen_attribute)
                                character.money += 10
                            else:
                                print("Invalid input. Please enter 'attack', 'health' or 'speed'.\
                                    \n")
                                chosen_attribute = "x"
                        print("")
                    else:
                        print("Incorrect.")
                        riddle_answer = "x"
            elif puzzle_no == 21:
                while riddle_answer == "x":
                    riddle_answer = input(f"{character.name}, what is full of holes but can still hold water??? ")
                    if "sponge" in riddle_answer.lower():
                        print(f"Correct!\
                            \nThe mysterious figure points you towards The {self.name} badge.\
                            \n ")
                        character.badge_count += 1
                        chosen_attribute = "x"
                        while chosen_attribute.lower() == "x":
                            chosen_attribute = input("Would you like to enhance your attack, health, or speed? ")
                            chosen_attribute = chosen_attribute.lower()
                            if chosen_attribute in ["attack", "health", "speed"]:
                                character.train(chosen_attribute)
                                character.money += 10
                            else:
                                print("Invalid input. Please enter 'attack', 'health' or 'speed'.\
                                    \n")
                                chosen_attribute = "x"
                        print("")
                    else:
                        print("Incorrect.")
                        riddle_answer = "x"
            elif puzzle_no == 10:
                while riddle_answer == "x":
                    riddle_answer = input(f"{character.name}, what is always in front of you but cannot be seen??? ")
                    if "future" in riddle_answer.lower():
                        print(f"Correct!\
                            \nThe mysterious figure points you towards The {self.name} badge.\
                            \n")
                        character.badge_count += 1
                        chosen_attribute = "x"
                        while chosen_attribute.lower() == "x":
                            chosen_attribute = input("Would you like to enhance your attack, health, or speed? ")
                            chosen_attribute = chosen_attribute.lower()
                            if chosen_attribute in ["attack", "health", "speed"]:
                                character.train(chosen_attribute)
                                character.money += 10
                            else:
                                print("Invalid input. Please enter 'attack', 'health' or 'speed'.\
                                    \n")
                                chosen_attribute = "x"
                        print("")
                    else:
                        print("Incorrect.")
                        riddle_answer = "x"

        #conundrum game
        elif puzzle_no in [3, 12, 30]:
            print("A smartly dressed man appears in front of you...it's t.v. and tax Bad-Guy Jimmy Carr!\
                \nJimmy explains to you that you must solve his countdown conundrum before he reveals the badge.\
                \n")

            if puzzle_no == 3:
                conundrum_answer = "x"
                while conundrum_answer == "x":
                    conundrum_answer = input("Clue: 'Thanks, but i'll pass' Letters: 'IBEDSANTA' ")
                    print("")
                    if conundrum_answer.lower() == "abstained":
                        print(f"Correct!\
                            \nJimmy Carr points you towards The {self.name} badge.\
                            \n")
                        character.badge_count += 1
                        chosen_attribute = "x"
                        while chosen_attribute.lower() == "x":
                            chosen_attribute = input("Would you like to enhance your attack, health, or speed? ")
                            chosen_attribute = chosen_attribute.lower()
                            if chosen_attribute in ["attack", "health", "speed"]:
                                character.train(chosen_attribute)
                                character.money += 10
                            else:
                                print("Invalid input. Please enter 'attack', 'health' or 'speed'.\
                                    \n")
                                chosen_attribute = "x"
                        print("")
                    else:
                        print("Incorrect!")
                        conundrum_answer = "x"
            
            elif puzzle_no == 12:
                conundrum_answer = "x"
                while conundrum_answer == "x":
                    conundrum_answer = input("Clue: 'Peter waved goodbye to his Dad and then...' Letters: 'PETERDAD' ")
                    print("")
                    if conundrum_answer.lower() == "departed":
                        print(f"Correct!\
                            \nJimmy Carr points you towards The {self.name} badge.\
                            \n")
                        character.badge_count += 1
                        chosen_attribute = "x"
                        while chosen_attribute.lower() == "x":
                            chosen_attribute = input("Would you like to enhance your attack, health, or speed? ")
                            chosen_attribute = chosen_attribute.lower()
                            if chosen_attribute in ["attack", "health", "speed"]:
                                character.train(chosen_attribute)
                                character.money += 10
                            else:
                                print("Invalid input. Please enter 'attack', 'health' or 'speed'.\
                                    \n")
                                chosen_attribute = "x"
                        print("")
                    else:
                        print("Incorrect!")
                        conundrum_answer = "x"

            elif puzzle_no == 30:
                conundrum_answer = "x"
                while conundrum_answer == "x":
                    conundrum_answer = input("Clue: 'Nyccegirls take care of the planet' Letters: 'NYCCEGIRL' ")
                    print("")
                    if conundrum_answer.lower() == "recycling":
                        print(f"Correct!\
                            \nJimmy Carr points you towards The {self.name} badge.\
                            \n")
                        character.badge_count += 1
                        chosen_attribute = "x"
                        while chosen_attribute.lower() == "x":
                            chosen_attribute = input("Would you like to enhance your attack, health, or speed? ")
                            chosen_attribute = chosen_attribute.lower()
                            if chosen_attribute in ["attack", "health", "speed"]:
                                character.train(chosen_attribute)
                                character.money += 10
                            else:
                                print("Invalid input. Please enter 'attack', 'health' or 'speed'.\
                                    \n")
                                chosen_attribute = "x"
                        print("")
                    else:
                        print("Incorrect!")
                        conundrum_answer = "x"

class Character:
    """Character. Functions include check_stats, modify_stats, train, fight (strike & counter)."""


    #-2 as my character will be in this class and will be created twice upon starting a new game....DONT CHANGE
    foes_remaining = -2
    wins = 0 ##nice to know when checking stats.
    losses = 0

    #items required for default value
    clothes = Armour("clothes",0, 5)
    gloves = Weapon("gloves", 0, 5)

    def __init__(self, name, attack, hp, speed, money, armour=clothes, weapon=gloves, inventory=[], badge_count = 0):

        self.name = name
        self.hp = hp
        self.attack = attack
        self.speed = speed
        self.money = money
        self.armour = armour
        self.weapon = weapon
        self.inventory = inventory
        self.badge_count = badge_count
        Character.foes_remaining += 1

    
    def check_stats(self):

        stat_data = [['NAME', 'ATTACK', 'HEALTH', 'SPEED', 'GOLD'],
        [str(self.name.title()), str(self.attack), str(self.hp), str(self.speed), str(self.money)],
        [str(self.weapon.name.title()), str(self.weapon.attack), str(0), str(0), str(self.weapon.value)],
        [str(self.armour.name.title()), str(0), str(self.armour.hp), str(0), str(self.armour.value)]]
        dash = '-' * 60
        for i in range(len(stat_data)):
            if i == 0:
                print(dash)
                print('{:^16s}{:^12s}{:^12s}{:^12s}{:^12s}'.format(stat_data[i][0],stat_data[i][1],stat_data[i][2],stat_data[i][3],stat_data[i][4]))
                print(dash)
            else:
                print('{:^16s}{:^12s}{:^12s}{:^12s}{:^12s}'.format(stat_data[i][0],stat_data[i][1],stat_data[i][2],stat_data[i][3],stat_data[i][4]))
        print("") ####prints nice table

        print(f"There are {Character.foes_remaining} Bad Guys left to defeat. You have currently won {Character.wins} battles and lost {Character.losses}.\
            \nThere are {Location.undiscovered_locations} undiscovered locations left to find.\
            \n\
            \nInventory:")
        if len(self.inventory) > 0:
            for item in self.inventory:
                print (item.name.title())
        print("")

    def modify_stats(self, attack, hp, speed):

        total_points = int(attack + hp + speed) - 30
        total_points_original = total_points
        self.attack = 10
        self.hp = 10
        self.speed = 10
        while total_points > 0:
            print(f"You have {total_points} points remaining to spend. You can spend these on:\
                \n'Attack' (currently {self.attack})\
                \n'Health' (currently {self.hp})\
                \n'Speed' (currently {self.speed})\
                \n.")
            stat = str(input("Which stat would you like to assign points to? "))
            if stat.lower() in ["attack", "health", "speed"]:
                points_assigned = "x"
                while points_assigned == "x":
                    try:
                        points_assigned = int(input("How many points would you like to assign "))
                    except ValueError:
                        print("Please enter a number not letters.")
                        points_assigned = "x"
                if stat.lower() == "attack":
                    self.attack += points_assigned
                    total_points -= points_assigned
                    if total_points < 0:
                        self.attack = 10
                        self.hp = 10
                        self.speed = 10
                        total_points = total_points_original
                        print("Sorry but you have tried to reassign more points than you have.\
                            \n")
                elif stat.lower() == "health":
                    self.hp += points_assigned
                    total_points -= points_assigned
                    if total_points < 0:
                        self.attack = 10
                        self.hp = 10
                        self.speed = 10
                        total_points = total_points_original
                        print("Sorry but you have tried to reassign more points than you have.\
                            \n")
                elif stat.lower() == "speed":
                    self.speed += points_assigned
                    total_points -= points_assigned
                    if total_points < 0:
                        self.attack = 10
                        self.hp = 10
                        self.speed = 10
                        total_points = total_points_original
                        print("Sorry but you have tried to reassign more points than you have.\
                            \n")
            else:
                print("Please enter 'attack', 'health' or 'speed'.\
                    \n")
        print("Points have been reassigned successfully!\
            \n")


    def strike(self, opponent):
        damage = int((self.attack + self.weapon.attack)/random.randint(2,5)) #element of chance to damage inflicted but also influenced by character attack.
        opponent.hp = int(opponent.hp - damage)
        print(f"{opponent.name.title()} took {damage} damage from {self.name.title()}'s {self.weapon.name}!")
        if (opponent.hp + opponent.armour.hp) > 0:
            print(f"{opponent.name.title()} has {opponent.hp + opponent.armour.hp} hp remaining\
                \n")
        else:
            print(f"{opponent.name.title()} has been defeated!!")


    def counter(self, opponent):
        counter_success = random.randint(1,2) # 1=successful counter attack. 2=unsuccessful counter attack.
        if counter_success == 1:
            damage = int((self.attack + self.weapon.attack)/random.randint(2,5))
            opponent.hp = opponent.hp - damage
            print(f"{self.name.title()} dodged and countered causing {damage} damage!")
            if (opponent.hp + opponent.armour.hp) > 0:
                print(f"{opponent.name.title()} has {opponent.hp + opponent.armour.hp} hp remaining.\
                    \n")
            elif (opponent.hp + opponent.armour.hp) <= 0:
                print(f"{opponent.name.title()} has no hp remaining.\
                    \n")
        elif counter_success == 2:
            print(f"The dodge and counter move by {self.name.title()} failed and {opponent.name.title()} inflicted some damage")
            opponent.strike(self)


    def fight(self, opponent): #contains strike and counter functions
        battle_data = [['Name', 'Total Att.', 'Total Hp', 'Speed'],
        [str(self.name.title()), str(self.attack + self.weapon.attack), str(self.hp + self.armour.hp), str(self.speed)],
        [str(opponent.name.title()), str(opponent.attack + opponent.weapon.attack), str(opponent.hp + opponent.armour.hp), str(opponent.speed)]]
        dash = '-' * 50
        for i in range(len(battle_data)):
            if i == 0:
                print(dash)
                print('{:^12s}{:^12s}{:^12s}{:^12s}'.format(battle_data[i][0],battle_data[i][1],battle_data[i][2],battle_data[i][3]))
                print(dash)
            else:
                print('{:^12s}{:^12s}{:^12s}{:^12s}'.format(battle_data[i][0],battle_data[i][1],battle_data[i][2],battle_data[i][3]))
        print("") #nicely presented table with character stats so player knows how to approach fight. Should they try to dodge or strike?
        heal_limit = int(self.hp)
        heal_limit_opponent = int(opponent.hp)
        while (opponent.hp + opponent.armour.hp) > 0 and (self.hp + self.armour.hp) > 0:
            fight_action = input("Would you like to strike, dodge or drink a potion to replenish up to 30hp? ")
        
            if fight_action.lower() == "drink":
                if potion_hp in self.inventory:
                    drink_test = self.hp + 30
                    if drink_test <= heal_limit:
                        self.hp += 30
                        print(f"You now have {self.hp + self.armour.hp} hp\
                            \n ")
                        self.inventory.remove(potion_hp)
                    elif (self.hp + 30) > heal_limit:
                        self.hp = heal_limit
                        print(f"You now have {self.hp + self.armour.hp} hp\
                            \n")
                        self.inventory.remove(potion_hp)
                else:
                    print("You have no potions to drink!\
                            \n")
            elif fight_action.lower() == "strike":
                opponent_action = random.randint(1,2) #what will the opponent do? think of 1 as strike and 2 as dodge
                if opponent_action == 1:
                    if self.speed >= opponent.speed:
                        self.strike(opponent)
                        if (opponent.hp + opponent.armour.hp) > 0:
                            opponent.strike(self)
                    elif self.speed < opponent.speed:
                        opponent.strike(self)
                        if (self.hp + self.armour.hp) > 0:
                            self.strike(opponent)
                elif opponent_action == 2:
                    opponent.counter(self)      
            elif fight_action.lower() == "dodge":
                opponent_action = random.randint(1,2) #what will the opponent do? think of 1 as strike and 2 as dodge
                if opponent_action == 1:
                    self.counter(opponent)
                elif opponent_action == 2:
                    print(f"{self.name.title()} and {opponent.name.title()} both tried to dodge which is embarrassing!\
                        \n")
            else:
                print(f"{self.name.title()} did not understand your silly language. Please enter 'strike', 'dodge' or 'drink'\
                    \n")
        if (self.hp + self.armour.hp) > 0:
            print("Congratulations on your victory!\
                \nThe medics on site will return your health to normal.\
                \n")
            Character.wins += 1
            Character.foes_remaining -= 1
            loot_data = [['NAME', 'POWER', 'HEALTH', 'VALUE'], #lots of modifications to do here. Give both armour and weapons a health and power stat
            [str(opponent.weapon.name.title()), str(opponent.weapon.attack), str(0), str(opponent.weapon.value)],
            [str(opponent.armour.name.title()), str(0), str(opponent.armour.hp), str(opponent.armour.value)]]
            dash = '-' * 60
            for i in range(len(loot_data)):
                if i == 0:
                    print(dash)
                    print('{:<15s}{:>10s}{:>14s}{:>12s}'.format(loot_data[i][0],loot_data[i][1],loot_data[i][2],loot_data[i][3]))
                    print(dash)
                else:
                    print('{:<15s}{:>8s}{:>12s}{:>14s}'.format(loot_data[i][0],loot_data[i][1],loot_data[i][2],loot_data[i][3]))
            print("") #nicely presented table with weapon and armour details to let player decide on what to take.
        while (self.hp + self.armour.hp) > 0:
            loot_choice = input(f"As a sign of respect you must take only 1 of {opponent.name}'s items along with their {opponent.money} gold.\
                \nThe item will be automatically equipped and the item it replaces will be placed in your inventory.\
                \nWhich would you like to take? ")
            print("")
            if loot_choice.lower() == opponent.armour.name.lower():
                self.inventory.append(self.armour)
                self.armour = opponent.armour
                break
            elif loot_choice.lower() == opponent.weapon.name.lower():
                self.inventory.append(self.weapon)
                self.weapon = opponent.weapon
                break
            elif loot_choice.lower() == "neither":
                break
            else:
                print("Invalid input. Please type the name of the item you would like to take or 'neither'.\
                    \n")
        self.money += opponent.money
        self.hp = heal_limit
        while (opponent.hp + opponent.armour.hp) > 0:
            print("You have been defeated and will be taken to the Battle-Hub Hospital for treatment to restore your health.\
                \n")
            self.hp = heal_limit
            Character.losses += 1
            opponent.hp = heal_limit_opponent
            break

    def train(self, attribute):

        if attribute == "health":
            self.hp += 5
            print("Hp + 5")

        elif attribute == "attack":
            self.attack += 5
            print("Attack + 5")

        elif attribute == "speed":
            self.speed += 5
            print("Speed + 5")

        self.money -= 10



#LOCATIONS
#name, location_no, description
jungle = Location("Jungle", 1, "A gloomy but serene oasis of green, with plants and trees at every turn which block\nthe sunlight and where the thick, humid air is saturated with a cacophony of birdsong.")
desert = Location("Desert", 2, "Waves of desolate sand stretching in every direction as far as\nthe eye can see, where the hot sun fiercely pierces the ground.")
swamp = Location("Swamp", 3, "A dismal, flat and featureless marshland, where the air is\nstagnant, and the ground is damp and sticky underfoot.")
abandoned_city = Location("Abandoned City", 10, "Eerily quiet streets, houses and shop fronts, once bustling with life that\nhas been extinguished, leaving behind a raided corpse of the city before.")
lost_temple = Location("Lost Temple", 11, "A magnificent but calming ornate building, with giant pillars, abandoned\nand overgrown with ivy but strewn with remnants of Buddhist worship in the past.")
bull_ring = Location("Bull Ring", 12, "A gigantic arena with staring and un-forgiving faces in every direction, where the\nair is shattered with screaming and chanting voices and where the dusty ground is covered with bloodspots of previous slaughters.")
great_plain = Location("Great Plains", 20, "A vast and undulating prairie exposed to the hot and sticky sun,\nwhere no life is safe from the predators that roam the grasslands.")
mountain = Location("Mountains", 21, "A peaceful but breath-taking giant which towers above\nthe land, where the jagged snow covered-tip seems a world away.")
volcano = Location("Volcano", 30, "A place where no life can survive, where the earth is shattered\nin places and luminescent liquid fire oozes and bubbles from its core.")

location_list = [jungle, desert, swamp, abandoned_city, lost_temple, bull_ring, great_plain, mountain, volcano]

#ITEMS
#name, value, attack/hp
clothes = Armour("clothes",0, 5)
gloves = Weapon("gloves", 0, 5)
potion_hp = Item("Health Potion", 50)
ring_of_power = Armour("Ring of Power", 20, 15)
oddjob = Weapon("Odd-Job", 40, 30)
sith_armour = Armour("Sith Armour", 50, 35)
lightsaber = Weapon("Lightsaber", 60, 40)
infinity_gauntlet = Armour("Gauntlet",70,55)
stasis_rifle = Weapon("Stasis Rifle",50,35)
helmet = Armour("Magneto Helmet",50,50 )
magnet = Weapon("Magnetic Powers", 85, 65)
batsuit = Armour("Batsuit", 70, 55)
batmobile = Weapon("Bat Mobile", 100, 80)
kevlar_armour = Armour("Kevlar Armour", 60, 60)
assault_rifle = Weapon("Assault Rifle", 60, 60)
cloak = Armour("Cloak", 60, 70)
elder_wand = Weapon("Elder Wand", 80, 100)
item_list = [clothes, gloves, potion_hp, ring_of_power, oddjob, sith_armour, lightsaber, stasis_rifle, infinity_gauntlet,helmet, magnet, batsuit, batmobile, kevlar_armour, assault_rifle, cloak, elder_wand]


#CHARACTERS
#name, attack, hp, speed, money, armour=clothes, weapon=gloves, inventory=[]
foe_1 = Character("Gollum", 5, 5, 25, 15, ring_of_power)
foe_2 = Character("Goldfinger", 10, 15, 15, 20, weapon=oddjob)
foe_3 = Character("Darth Vader", 25, 20, 20, 50,sith_armour,lightsaber)
foe_4 = Character("Magneto", 20, 30, 25, 70, helmet, magnet)
foe_5 = Character("Bane", 40, 40, 30, 90, kevlar_armour, assault_rifle)
foe_6 = Character("Batman", 40, 40, 35,120,batsuit,batmobile)
foe_7 = Character("Voldemort", 40, 50, 40, 100, cloak, elder_wand)
foe_8 = Character("Thanos", 80, 80, 45,1000,infinity_gauntlet,stasis_rifle)
my_character = Character("x",1,1,1,1)

foe_list = [foe_1, foe_2, foe_3, foe_4, foe_5, foe_6, foe_7, foe_8]

load_or_new = "x"
while load_or_new == "x":
    load_or_new = input("Welcome, would you like to load or start a new game? ")
    load_or_new = load_or_new.lower()
    if "load" in load_or_new:
        try: #prevents error and crash when trying to load a save game that doesnt exist.
            load(my_character, foe_list, location_list, Location, Character, item_list)
        except:
            FileNotFoundError
            print("No save game found. Please start a new game by typing new.\
                \n")
            load_or_new = "x"

    elif "new" in load_or_new:
        print("\
        \nWelcome to the Bad-Guy Brawl universe, where Bad Guys from every\
        \nfranchise can fight it out to discover... Who is the Bad-Guy Brawl Champion?!\
        \n\
        \nThroughout the next hour of you life, you must adventure, train and battle\
        \nyour way to your calling... becoming The Bad-Guy Brawl Champion.\
        \n\
        \nYou will be based at the Battle Hub, where you are free to battle your way up the Bad-Guy ladder.\
        \nHowever, no warrior has the skills necessary (or luck) to become the Bad-Guy Brawl Champion without\
        \nsome training to boost your abilities and adventure to gain the necessary badges.\
        \n")
        my_name = "x"
        while my_name == "x":
            my_name = input("What would you like to call your character? ")
            my_character = Character(my_name,10,10,10,15)
            if len(my_character.name) > 10:
                my_name = "x"
                Character.foes_remaining -= 1 #keep here otherwise each time name is invalid an extra foe will register
                print("Your name can be a maximum of 10 characters.\
                    \n")

        difficulty = "x"
        while difficulty == "x":
            difficulty = input("Would you like to play in easy medium or hard? ")
            if difficulty.lower() == "easy":
                my_character.money = int(my_character.money * 3) + 20
                my_character.attack = int(my_character.attack * 3)
                my_character.hp = int(my_character.hp * 3)
                my_character.speed = int(my_character.speed * 3)
            elif difficulty.lower() == "medium":
                my_character.money = int(my_character.money * 2) + 5
                my_character.attack = int(my_character.attack * 2)
                my_character.hp = int(my_character.hp * 2)
                my_character.speed = int(my_character.speed * 2)
            elif difficulty.lower() == "hard":
                break
            else:
                print("Invalid input. Please enter 'easy', 'medium' or 'hard'.\
                    \n")
                difficulty = "x"
        print(f"Your difficulty has been set to {difficulty}.\
            \n")
        print("")

    else:
        print("Invalid Input. Please enter 'load' or 'new'.\
            \n")
        load_or_new = "x"



while Character.foes_remaining > -1: ##-1 allows game to continue once all characters are defeated. the only reward for winning is an improved sense of self worth.
    Location.current_location = 0     
    action = input("Would you like to battle, train, adventure, shop, quit or go to game options? ")
    print("")
    if action.lower() == "quit":
        break


    elif action.lower() == "battle":
        battle_access = my_character.badge_count + Character.foes_remaining
        if battle_access >= 9:
            for foe in foe_list:
                if foe.hp > 0:
                    my_character.fight(foe)
                    break
                elif Character.foes_remaining == 0:
                    print("There is no one left to fight!! You are the Bad-Guy Brawl CHAMPION!!!.\
                        \n") #as i said, the only real reward will be the improved sense of self worth.
                    break
        else:
            print("You must collect more badges through adventuring to reach your next foe.\
                \n")

    
    elif action.lower() == "train":
        if my_character.money >= 10:
            train_conf = "x"
            while train_conf == "x":
                train_conf = input(f"You have {my_character.money} gold. Training will cost 10 gold and improve the attribute by 5.\
                    \nAre you sure you would like to train? ")
                if train_conf.lower() == "yes":
                    to_train = "x"
                    while to_train == "x":
                        to_train = input("Would you like to train for greater speed, attack or health? ")
                        to_train = to_train.lower()
                        if to_train in ["speed", "attack", "health"]:
                            my_character.train(to_train)
                            print("")
                        else:
                            to_train = "x"
                            print("Invalid input. Please enter 'speed', 'attack' or 'health'.\
                                \n")
                elif train_conf.lower() == "no":
                    break
                else:
                    print("Invalid Input. Please enter 'yes' or 'no'.\
                        \n ")
                    train_conf = "x"
        else:
            print("You don't have enough gold to pay for training.\
                \n")


    elif "option" in action.lower():
        option_action = "x"
        while option_action == "x":
            option_action = input("Would you like to go back to game, check stats, save or load? ")
            if "stat" in option_action.lower():
                my_character.check_stats()
                stats_option = "x"
                while stats_option == "x":
                    stats_option = input("Would you like to modify some of your stat points? ")
                    stats_option = stats_option.lower()
                    if stats_option == "no":
                        print("")
                        break
                    elif stats_option == "yes":
                        my_character.modify_stats(my_character.attack, my_character.hp, my_character.speed)
                    else:
                        print("Please enter 'yes' or 'no'.\
                            \n")
                        stats_option = "x"
            elif "back" in option_action.lower():
                print("")
                break
            elif option_action.lower() == "save": #didn't make a function as code to save is only required in one place in the game.
                with open("save_game.txt", "w") as file_object:
                    for character in foe_list:
                        file_object.write(f"{character.name},{character.hp}\n")
                    file_object.write(f"my_character_name,{my_character.name}\n")
                    file_object.write(f"my_character_attack,{my_character.attack}\n")
                    file_object.write(f"my_character_hp,{my_character.hp}\n")
                    file_object.write(f"my_character_speed,{my_character.speed}\n")
                    file_object.write(f"my_character_money,{my_character.money}\n")
                    for item in my_character.inventory:
                        file_object.write(f"inventory_item,{item.name}\n")
                    file_object.write(f"my_character_badge_count,{my_character.badge_count}\n")
                    file_object.write(f"weapon_item,{my_character.weapon.name}\n")
                    file_object.write(f"armour_item,{my_character.armour.name}\n")
                    for location in location_list:
                        file_object.write(f"{location.name},{location.discovered}\n")
                    file_object.write(f"undiscovered_locations,{Location.undiscovered_locations}\n")
                    file_object.write(f"foes_remaining,{Character.foes_remaining}\n")
                    file_object.write(f"wins,{Character.wins}\n")
                    file_object.write(f"losses,{Character.losses}\n")

                    print("Game saved.\
                        \n")
                    

            elif option_action.lower() == "load":
                try:
                    load(location_list, foe_list, item_list, my_character, Location, Character)
                except:
                    FileNotFoundError
                    print("No save game found. Please start a new game by typing new.\
                        \n")
                    option_action = "x"   
            else:
                print("Invalid input. Please enter 'back', 'stats', 'save' or 'load'.\
                    \n ")
                option_action = "x"

            

    elif action.lower() == "shop":
        print("Welcome to the shop!\
            \n ")
        shop_action = "x"
        while shop_action == "x":
            shop_action = input("Would you like to buy, sell or go back to The Battle Hub? ")
            print("")
            if shop_action.lower() == "sell":
                if int(len(my_character.inventory))>0:
                    print("You have the following items available to sell:")
                    for item in my_character.inventory:
                        print(f"{item.name.title()}, {item.value} Gold ")
                    print("")
                    to_sell = input("Which item would you like to sell? ")
                    if to_sell.lower() != "back":
                        for item in my_character.inventory:
                            if to_sell.lower() == item.name.lower():
                                item.sell(my_character)
                                print(f"{item.name.title()} sold.\
                                    \n")
                                shop_action = "x"
                                break
                        if shop_action != "x":
                            print("This item wasn't in your inventory.\
                                \n")
                            shop_action = "x"
                    else:
                        shop_action = "x"
                else:
                    print("You have nothing to sell in your inventory.\
                        \n")
                    shop_action = "x"
            elif shop_action.lower() == "buy":
                buy_conf = "x"
                while buy_conf == "x":
                    buy_conf = input("This shop only sells health potions! Would you like to buy one for 50 gold? ")
                    if buy_conf.lower() == "yes":
                        if my_character.money > 50:
                            my_character.inventory.append(potion_hp)
                            my_character.money -= 50
                            print("A health potion has been added to your inventory.\
                                \n")
                            shop_action = "x"
                        else:
                            print(f"You only have {my_character.money} gold and can't afford a health potion.\
                                \nYou are asked to leave the shop.\
                                \n ")
                    elif buy_conf.lower() == "no":
                        print("The shopkeeper asks you to leave for wasting his time.\
                            \n")
                        break
                    else:
                        buy_conf = "x"
                        print("Invalid input. Please enter 'yes' or 'no'.\
                            \n")
            elif shop_action.lower() == "back":
                break
            else:
                shop_action = "x"
                print("Invalid input. Please enter 'buy', 'sell' or 'back'.\
                    \n")



    elif action.lower() == "adventure":
        if Location.undiscovered_locations > 0:
            while Location.current_location == 0:
                direction_decision_hub = input("You are now outside The Battle-Hub and you can take a road to the left or right...\
                    \nBe warned, the roads ahead are tough and you will need to spend 5 gold per turn to survive.\
                    \nAlternatively, you could go back into the Battle Hub. Would you like to go left, right or back? ")
                print("")
                if direction_decision_hub.lower() == "right":
                    Location.current_location += 10 #think of a binary tree where each time you go to the right your node increases by 10
                elif direction_decision_hub.lower() == "left":
                    Location.current_location += 1 #think of a binary tree where each time you go to the left your node increases by 1
                elif direction_decision_hub.lower() == "back":
                    print("You have re-entered The Battle Hub.\
                        \n")
                    break 
                else:
                    print("Invalid Input. Please enter 'left', 'right' or 'back'.\
                        \n")
            
            while Location.current_location in [1, 2, 3, 10, 20, 30, 11, 12, 21]:
                if my_character.money >= 5:
                    for loc in location_list:
                        if my_character.money < 5:
                            print("You no longer have enough gold to buy food while adventuring and decided to return to the Battle Hub for sustinance.\
                                \nPerhaps you should sell some items from your inventory or deafeat a foe in battke to earn their gold.\
                                \n ")
                            break
                        elif loc.number == Location.current_location:
                            if loc.discovered == False:
                                loc.discover(my_character)
                                loc.puzzle(int(loc.number), my_character)
                                loc.decision()
                            elif loc.discovered == True:
                                loc.discover(my_character)
                                loc.decision()
                    if Location.current_location in [4, 13, 22, 31, 40]:   #this is the edge of the map, will allow for game extension if more nodes are wanted in game updates.
                        print("It turns out that all roads lead to The Battle Hub eventually!\
                            \nYou decide you are tired from adventuring and re-enter to rest.\
                            \n ")
                        Location.current_location = 0
                        break
                    else:
                        print("You have returned to the Battle Hub.\
                            \n")
                        Location.current_location = 0
                        break
                else:
                    print("You no longer have enough gold to buy food while adventuring and decided to return to the Battle Hub for sustinance.\
                        \nPerhaps you should sell some items from your inventory.\
                        \n ")
                    Location.current_location = 0
        else:
            print("You have no where left to discover!\
                \nAdventuring would be a waste of precious gold.\
                \n")
    else:
        print("Invalid input. Please enter 'battle', 'train', 'adventure', 'shop', 'quit' or 'options'.")


