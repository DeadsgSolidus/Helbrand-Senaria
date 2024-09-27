import random
import json

# Race and sub-race definitions
races = {
    "Beast Race": {
        "health": 120,
        "strength": 15,
        "defense": 10,
        "magic": 5,
        "agility": 10
    },
    "Half-Orc": {
        "health": 110,
        "strength": 20,
        "defense": 15,
        "magic": 5,
        "agility": 7
    },
    "Elves": {
        "health": 100,
        "strength": 8,
        "defense": 5,
        "magic": 20,
        "agility": 15
    },
    "Terrans": {
        "health": 100,
        "strength": 10,
        "defense": 10,
        "magic": 10,
        "agility": 10
    }
}

sub_races = {
    "Demonic": {
        "health": -10,
        "strength": 5,
        "defense": 0,
        "magic": 10,
        "agility": 5
    },
    "Angelic": {
        "health": 0,
        "strength": 5,
        "defense": 10,
        "magic": 15,
        "agility": 10
    },
    "Vampire": {
        "health": 20,
        "strength": 10,
        "defense": -5,
        "magic": 10,
        "agility": 5
    },
    "Werewolf": {
        "health": 30,
        "strength": 15,
        "defense": 10,
        "magic": -10,
        "agility": 5
    },
    "Succubus": {
        "health": -10,
        "strength": 5,
        "defense": -5,
        "magic": 25,
        "agility": 10
    },
    "Incubus": {
        "health": -10,
        "strength": 5,
        "defense": 0,
        "magic": 20,
        "agility": 10
    }
}

class SkillTree:
    def __init__(self):
        self.skills = {
            "Strength": {
                "level": 0,
                "description": "Increases melee attack damage.",
                "cost": 1,
                "max_level": 5,
                "dependencies": []
            },
            "Power Strike": {
                "level": 0,
                "description": "Increases critical hit chance. Requires Strength Level 2.",
                "cost": 2,
                "max_level": 3,
                "dependencies": ["Strength", 2]
            },
            "Berserk": {
                "level": 0,
                "description": "Grants bonus damage when health is low. Requires Power Strike.",
                "cost": 3,
                "max_level": 1,
                "dependencies": ["Power Strike", 1]
            },
            "Dexterity": {
                "level": 0,
                "description": "Increases ranged attack accuracy.",
                "cost": 1,
                "max_level": 5,
                "dependencies": []
            },
            "Agility": {
                "level": 0,
                "description": "Increases chance to dodge. Requires Dexterity Level 2.",
                "cost": 2,
                "max_level": 3,
                "dependencies": ["Dexterity", 2]
            },
            "Precision": {
                "level": 0,
                "description": "Increases critical hit chance with ranged weapons. Requires Agility.",
                "cost": 3,
                "max_level": 1,
                "dependencies": ["Agility", 1]
            },
            "Magic": {
                "level": 0,
                "description": "Increases magical damage and mana.",
                "cost": 1,
                "max_level": 5,
                "dependencies": []
            },
            "Fireball": {
                "level": 0,
                "description": "Casts a fireball that deals AoE damage. Requires Magic Level 2.",
                "cost": 2,
                "max_level": 3,
                "dependencies": ["Magic", 2]
            },
            "Lightning Strike": {
                "level": 0,
                "description": "Calls down lightning on enemies. Requires Fireball.",
                "cost": 3,
                "max_level": 1,
                "dependencies": ["Fireball", 1]
            }
        }

    def display_skills(self):
        print("\n=== Skill Tree ===")
        for skill, data in self.skills.items():
            print(f"{skill}: Level {data['level']}/{data['max_level']} - {data['description']}")
        print()

    def upgrade_skill(self, skill_name, player):
        if skill_name in self.skills:
            skill = self.skills[skill_name]

            # Check if player has enough skill points
            if player.skill_points < skill["cost"]:
                print("Not enough skill points to upgrade this skill.")
                return

            # Check if skill is already maxed out
            if skill["level"] >= skill["max_level"]:
                print(f"{skill_name} is already at max level.")
                return

            # Check if dependencies are met
            if skill["dependencies"]:
                dependency, required_level = skill["dependencies"]
                if self.skills[dependency]["level"] < required_level:
                    print(f"{skill_name} requires {dependency} to be level {required_level} first.")
                    return

            # Upgrade skill
            skill["level"] += 1
            player.skill_points -= skill["cost"]
            print(f"Upgraded {skill_name} to level {skill['level']}.")
        else:
            print(f"Skill {skill_name} not found.")

class NPC:
    def __init__(self, name, role, dialogue_options):
        self.name = name
        self.role = role
        self.dialogue_options = dialogue_options

    def talk(self):
        print(f"{self.name} ({self.role}):")
        for i, option in enumerate(self.dialogue_options, 1):
            print(f"{i}. {option}")
        choice = int(input("Choose a dialogue option: "))
        if 1 <= choice <= len(self.dialogue_options):
            print(f"{self.name} says: '{self.dialogue_options[choice - 1]}'")
        else:
            print(f"{self.name} doesn't understand what you're saying.")

# NPCs for different locations
senaria_npcs = [
    NPC("Elder Rowan", "Village Elder", ["Welcome to Senaria, the safest place in the land.", "Be careful in the dungeon, young one."]),
    NPC("Merchant Tessa", "Trader", ["I sell the finest herbs and potions.", "Need to sell something? I can offer you a fair price."])
]

dark_amazon_npcs = [
    NPC("Mysterious Wanderer", "Rogue", ["Watch your back in these woods.", "The creatures here don't take kindly to strangers."]),
]

senaria_dungeon_npcs = [
    NPC("Ghostly Guardian", "Dungeon Spirit", ["You shouldn't be here, mortal.", "The treasures here come at a great cost."]),
]

decaria_mountains_npcs = [
    NPC("Hermit Griegor", "Mountain Sage", ["The dragons rule the peaks. Only the brave survive.", "I've seen trolls bigger than trees."]),
]

crystal_caverns_npcs = [
    NPC("Gemstone Collector", "Treasure Hunter", ["I'm here for the gems. What about you?", "They say the crystals are alive..."]),
]

forgotten_swamp_npcs = [
    NPC("Swamp Shaman", "Healer", ["The swamp will take your soul if you're not careful.", "I can offer you protection, for a price."]),
]


class Player:
    def __init__(self, name, race, sub_race):
        self.name = name
        self.race = race
        self.sub_race = sub_race
        self.health = races[race]["health"] + sub_races[sub_race]["health"]
        self.strength = races[race]["strength"] + sub_races[sub_race]["strength"]
        self.defense = races[race]["defense"] + sub_races[sub_race]["defense"]
        self.magic = races[race]["magic"] + sub_races[sub_race]["magic"]
        self.agility = races[race]["agility"] + sub_races[sub_race]["agility"]
        self.inventory = []
        self.gold = 1000  # Starting gold
        self.location = "Town"
        self.level = 1
        self.exp = 0
        self.skills = {
            "Power Strike": 1,
            "Berserk": 1,
            "Fireball": 1,
            "Lightning Strike": 1,
        }
        self.skill_points = 0  # Points earned when leveling up
        self.skill_tree = SkillTree()
        self.equipped_weapon = []
        self.equipped_armor = []

    def use_skill(self, skill_name, enemy):
        skill = self.skill_tree.skills.get(skill_name)
        if skill and skill["level"] > 0:
            if skill_name == "Power Strike":
                # Example for Power Strike, increasing damage
                damage = self.strength * 1.5
                print(f"{self.name} uses {skill_name}! Deals {damage} critical damage.")
            elif skill_name == "Fireball":
                damage = self.magic * 2
                print(f"{self.name} casts {skill_name}! Deals {damage} fire damage.")
            elif skill_name == "Lightning Strike":
                damage = self.magic * 3
                print(f"{self.name} casts {skill_name}! Deals {damage} lightning damage.")
            enemy.health -= damage
        else:
            print(f"{skill_name} is not available or not upgraded yet.")

    def show_status(self):
        print(f"\n=== {self.name}'s Status ===")
        print(f"Health: {self.health}")
        print(f"Strength: {self.strength} (+{self.get_weapon_bonus()})")
        print(f"Defense: {self.defense} (+{self.get_defense_bonus()})")
        print(f"Magic: {self.magic}")
        print(f"Agility: {self.agility}")
        print(f"Gold: {self.gold}")
        print(f"Inventory: {self.inventory}")
        print(f"Equipped Weapon: {self.equipped_weapon}")
        print(f"Equipped Armor: {self.equipped_armor}")
        print(f"Level: {self.level}, EXP: {self.exp}")
        print(f"Skill Points: {self.skill_points}\n")

    def move(self, new_location):
        self.location = new_location
        print(f"\nYou have moved to {self.location}.\n")
    
    def upgrade_skill(self, skill_name):
        self.skill_tree.upgrade_skill(skill_name, self)

    def get_weapon_bonus(self):
        if self.equipped_weapon:
            if "Sword" in self.equipped_weapon:
                return 5  # Swords increase strength by 5
        return 0
    
    def get_defense_bonus(self):
        if self.equipped_armor:
            if "Steel Armor" in self.equipped_armor:
                return 10  # Armor adds a defense bonus of 10
        return 0

    def attack(self, enemy):
        # Calculate damage based on player's strength and weapon bonus
        damage = self.strength + self.get_weapon_bonus()
        enemy.health -= damage
        print(f"{self.name} attacks! {enemy.name} takes {damage} damage. Enemy health: {enemy.health}")
    
    def use_skill(self, skill_name, enemy):
        skill = self.skill_tree.skills.get(skill_name)
        
        if skill and skill["level"] > 0:
            # Power Strike increases damage based on level
            if skill_name == "Power Strike":
                base_damage = self.strength
                # Boost damage according to Power Strike level
                damage = base_damage * (1 + (0.25 * skill["level"]))  # 25% more damage per level
                print(f"{self.name} uses {skill_name}! Deals {damage} critical damage.")
                enemy.health -= damage

            # Berserk grants bonus damage when player's health is low
            elif skill_name == "Berserk" and self.health < (0.3 * (races[self.race]["health"] + sub_races[self.sub_race]["health"])):
                base_damage = self.strength
                # Increased damage when health is below 30%
                damage = base_damage * (1.5 + (0.2 * skill["level"]))  # +50% base damage when low on health, scaling with level
                print(f"{self.name} goes Berserk! Deals {damage} boosted damage.")
                enemy.health -= damage

            # Fireball deals magic damage based on Magic level
            elif skill_name == "Fireball":
                base_damage = self.magic
                # Scale fireball damage based on the level of Fireball skill
                damage = base_damage * (1.5 + (0.3 * skill["level"]))  # Fireball damage increases by 30% per level
                print(f"{self.name} casts {skill_name}! Deals {damage} fire damage.")
                enemy.health -= damage

            # Lightning Strike deals high damage based on skill level
            elif skill_name == "Lightning Strike":
                base_damage = self.magic
                # Deal more lightning damage depending on Lightning Strike's level
                damage = base_damage * (2 + (0.5 * skill["level"]))  # High damage that scales with level
                print(f"{self.name} summons {skill_name}! Deals {damage} lightning damage.")
                enemy.health -= damage

        else:
            print(f"{skill_name} is not available or not upgraded yet.")
    
    def use_item(self, item_name):
        if item_name in self.inventory:
            if "Health Potion" in item_name:
                self.health += 50
                print(f"Used {item_name}. Health is now {self.health}.")
                self.inventory.remove(item_name)
            else:
                print(f"{item_name} cannot be used right now.")
        else:
            print(f"You don't have {item_name} in your inventory.")
    
    def gain_exp(self, amount):
        self.exp += amount
        print(f"Gained {amount} EXP! Current EXP: {self.exp}")
        self.check_level_up()
    
    def check_level_up(self):
        if self.exp >= self.level * 100:
            self.level += 1
            self.skill_points += 1
            print(f"Congratulations! {self.name} leveled up to Level {self.level}. Skill points available: {self.skill_points}")
    
    def equip_item(self, item_name):
        if item_name in self.inventory:
            if "Sword" in item_name or "Staff" in item_name:
                self.equipped_weapon = item_name
                print(f"Equipped {item_name}.")
            elif "Armor" in item_name:
                self.equipped_armor = item_name
                print(f"Equipped {item_name}.")
            else:
                print(f"{item_name} cannot be equipped.")
        else:
            print(f"You don't have {item_name} in your inventory.")

class Enemy:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, player):
        # Enemy attack uses attack_power to deal damage
        damage = random.randint(5, self.attack_power)
        player.health -= damage
        print(f"The {self.name} attacks you and deals {damage} damage!")

    def is_alive(self):
        return self.health > 0

class World:
    def __init__(self):
        self.locations = {
            "Senaria": "A safe place to rest and buy items.",
            "Dark Amazon": "A dark forest filled with dangerous creatures.",
            "Senaria Dungeon": "An ancient dungeon with hidden treasures and deadly traps.",
            "Senaria Ruins": "Ruins of an old kingdom. Watch out for ghosts!",
            "Decaria Mountains": "A mountainous region covered in fog. Home to trolls and dragons.",
            "Crystal Caverns": "A glittering cave filled with rare gems and fierce elementals.",
            "Forgotten Swamp": "A murky swamp with poisonous creatures and ancient curses.",
            "Battle Coliseum": "A fierce arena where endless battles await. Each victory makes the next battle harder!"
        }

    def show_locations(self):
        print("\n=== Available Locations ===")
        for location, description in self.locations.items():
            print(f"{location}: {description}")
        print()

class Store:
    def __init__(self):
        self.items = {
            "Iron Sword": 100,
            "Steel Sword": 300,
            "Magic Staff": 500,
            "Health Potion": 50,
            "Leather Armor": 150,
            "Steel Armor": 400,
            "Enchanted Armor": 600,
            "Gemstone": 800,
            "Rare Herbs": 30,
            "Magic Scroll": 1000,
        }

    def show_items(self):
        print("\n=== Store ===")
        for item, price in self.items.items():
            print(f"{item}: {price} gold")
        print()

    def buy_item(self, item_name, player):
        if item_name in self.items:
            price = self.items[item_name]
            if player.gold >= price:
                player.inventory.append(item_name)
                player.gold -= price
                print(f"{item_name} purchased! Remaining gold: {player.gold}")
            else:
                print("Not enough gold to buy this item.")
        else:
            print(f"{item_name} is not available in the store.")

    def sell_item(self, item_name, player):
        if item_name in player.inventory:
            # Items sell for half their purchase price
            sell_price = int(self.items.get(item_name, 0) * 0.5)
            if sell_price > 0:
                player.inventory.remove(item_name)
                player.gold += sell_price
                print(f"{item_name} sold for {sell_price} gold! Current gold: {player.gold}")
            else:
                print(f"{item_name} cannot be sold.")
        else:
            print(f"You don't have {item_name} in your inventory.")

class Blacksmith:
    def combine(self, player):
        if len(player.inventory) < 2:
            print("You need at least two weapons to combine.")
            return
        
        # Pick two weapons to combine
        print("\nAvailable items in inventory:")
        for idx, item in enumerate(player.inventory):
            print(f"{idx + 1}. {item}")
        
        try:
            choice1 = int(input("\nChoose the first item to combine: ")) - 1
            choice2 = int(input("Choose the second item to combine: ")) - 1
        except ValueError:
            print("Invalid input.")
            return

        # Remove the original items and add a hybrid weapon
        item1 = player.inventory.pop(choice1)
        item2 = player.inventory.pop(choice2)
        hybrid_weapon = f"Hybrid of {item1} and {item2}"
        player.inventory.append(hybrid_weapon)
        print(f"\n{item1} and {item2} were combined to create {hybrid_weapon}!")

class Game:
    def __init__(self, player):
        self.player = player
        self.world = World()
        self.store = Store()
        self.blacksmith = Blacksmith()
        self.skills = player.skill_tree.skills
        self.gold = player.gold

    def start(self):
        print("\n=== Welcome to the Dark Fantasy World ===")
        self.player.show_status()
        while True:
            self.show_menu()

    def display_skills(self):
        print("\n=== Skill Tree ===")
        for skill, data in self.skills.items():
            # Ensure that the correct structure is used
            print(f"{skill}: Level {data['level']}/{data['max_level']} - {data['description']}")
        print()

    def show_menu(self):
        print("\n=== Main Menu ===")
        print("1. Explore")
        print("2. Show Status")
        print("3. Inventory")
        print("4. Display Skill Tree")
        print("5. Upgrade Skills")
        print("6. Save Game")
        print("7. Load Game")
        print("8. Store")
        print("9. Blacksmith")
        print("10. Equip Gear")
        print("11. Use Item")
        print("12. Exit")

        choice = input("\nWhat would you like to do? (1-12): ")

        if choice == '1':
            self.explore()
        elif choice == '2':
            self.player.show_status()
        elif choice == '3':
            self.show_inventory()
        elif choice == '4':
            self.display_skills()
        elif choice == '5':
            self.upgrade_skills()
        elif choice == '6':
            self.save_game()
        elif choice == '7':
            self.load_game()
        if choice == "8":
            print("\n1. Buy Items\n2. Sell Items")
            sub_choice = input("Do you want to buy or sell? (1 for Buy, 2 for Sell): ")
            if sub_choice == "1":
                self.store.show_items()
                item = input("Enter the name of the item to buy (or 'exit' to leave): ")
                if item.lower() != 'exit':
                    self.store.buy_item(item, self.player)
            elif sub_choice == "2":
                print("\n=== Inventory ===")
                for item in self.player.inventory:
                    print(item)
                item_to_sell = input("Enter the name of the item to sell (or 'exit' to leave): ")
                if item_to_sell.lower() != 'exit':
                    self.store.sell_item(item_to_sell, self.player)
            else:
                print("Invalid option.")
        elif choice == "9":
                print("\nYou visit the blacksmith.")
                self.blacksmith.combine(self.player)
        elif choice == "10":
                item = input("\nEnter the name of the item to equip: ")
                self.player.equip_item(item)
        elif choice == "11":
                item = input("\nEnter the name of the item to use: ")
                self.player.use_item(item)
        elif choice == '12':
            print("Thank you for playing!")
            exit()

    def explore(self):
        self.world.show_locations()
        choice = input("Where would you like to go? ")
        if choice in self.world.locations:
            self.player.move(choice)
            if choice == "Senaria":
                self.senaria_event()
            if choice == "Dark Amazon":
                self.forest_event()
            elif choice == "Senaria Dungeon":
                self.dungeon_event()
            elif choice == "Decaria Mountains":
                self.mountain_event()
            elif choice == "Crystal Caverns":
                self.cavern_event()
            elif choice == "Forgotten Swamp":
                self.swamp_event()
            elif choice == "Battle Coliseum":
                self.coliseum_event()
        else:
            print("Invalid location.")

    def senaria_event(self):
        print("You make it sefely to Senaria. The Only true safehaven in these lands.")

        print("\nYou meet some townsfolk and spark a conversation.")
        senaria_npcs[0].talk()

    def forest_event(self):
        print("You enter the Dark Amazon and hear eerie noises...")
        
        # Introduce the NPC interaction
        print("\nYou encounter an NPC:")
        dark_amazon_npcs[0].talk()

        # After NPC interaction, continue with the rest of the event
        roll = random.random()

        if roll < 0.3:
            print("A wild beast appears!")
            enemy = Enemy("Beast", 30, 10)
            self.combat(enemy)
        elif 0.3 <= roll < 0.6:
            print("A group of forest bandits ambushes you!")
            enemy = Enemy("Forest Bandit", 35, 12)
            self.combat(enemy)
        else:
            print("You find rare herbs and add them to your inventory.")
            self.player.inventory.append("Rare Herbs")

    def dungeon_event(self):
        print("The dungeon is cold and full of danger...")
        
        print("\nYou encounter an NPC:")

        senaria_dungeon_npcs[0].talk()
        
        roll = random.random()

        if roll < 0.3:
            print("A skeleton warrior charges at you!")
            enemy = Enemy("Skeleton", 40, 12)
            self.combat(enemy)
        elif 0.3 <= roll < 0.6:
            print("You encounter a deadly trap!")
            trap_damage = random.randint(10, 20)
            self.player.health -= trap_damage
            print(f"A trap goes off! You take {trap_damage} damage.")
        elif 0.6 <= roll < 0.8:
            print("You discover a treasure chest filled with gold!")
            gold_amount = random.randint(100, 300)
            self.player.gold += gold_amount
            print(f"You gained {gold_amount} gold. Current gold: {self.player.gold}")
        else:
            print("You find a magical scroll and add it to your inventory.")
            self.player.inventory.append("Magic Scroll")


    def mountain_event(self):
        print("You enter the Misty Mountains, the air is thick with fog...")
        
        print("\nYou encounter an NPC:")
        decaria_mountains_npcs[0].talk()
        
        roll = random.random()

        if roll < 0.3:
                print("A troll emerges from the mist!")
                enemy = Enemy("Troll", 50, 15)
                self.combat(enemy)
        elif 0.3 <= roll < 0.5:
                print("You hear the roar of a dragon in the distance. It's coming your way!")
                enemy = Enemy("Dragon", 80, 25)
                self.combat(enemy)
        elif 0.5 <= roll < 0.7:
                print("You stumble upon an ancient warrior's grave and find enchanted armor!")
                self.player.inventory.append("Enchanted Armor")
        else:
                print("You find a rare herb growing in the mist.")
                self.player.inventory.append("Rare Herb")

    def cavern_event(self):
            print("The Crystal Caverns glitter with gems, but danger lurks in the shadows...")
            
            print("\nYou encounter an NPC:")
            crystal_caverns_npcs[0].talk()
            
            roll = random.random()

            if roll < 0.3:
                print("An elemental creature attacks!")
                enemy = Enemy("Crystal Elemental", 60, 20)
                self.combat(enemy)
            elif 0.3 <= roll < 0.6:
                print("You are ambushed by a crystal spider!")
                enemy = Enemy("Crystal Spider", 55, 18)
                self.combat(enemy)
            elif 0.6 <= roll < 0.8:
                print("You find a shimmering gemstone that boosts your mana!")
                self.player.mana += 10
                print(f"Your mana increases by 10. Current mana: {self.player.mana}")
            else:
                print("You find a sparkling gemstone.")
                self.player.inventory.append("Gemstone")

    def swamp_event(self):
        print("The Forgotten Swamp is murky and filled with poisonous creatures...")
        
        print("\nYou encounter an NPC:")
        forgotten_swamp_npcs[0].talk()

        roll = random.random()

        if roll < 0.3:
            print("A swamp serpent strikes!")
            enemy = Enemy("Swamp Serpent", 40, 14)
            self.combat(enemy)
        elif 0.3 <= roll < 0.6:
            print("A swamp hag appears and tries to curse you!")
            enemy = Enemy("Swamp Hag", 45, 16)
            self.combat(enemy)
        elif 0.6 <= roll < 0.8:
            print("You find a hidden swamp treasure!")
            self.player.inventory.append("Swamp Treasure")
        else:
            print("You find an ancient relic buried in the mud.")
            self.player.inventory.append("Ancient Relic")

    def coliseum_event(self):
        print("\nYou enter the Battle Coliseum. An endless series of fights awaits you!")
        
        battle_count = 0
        enemy_base_health = 30
        enemy_base_attack = 10
        base_attack_power = 1

        # Player chooses to keep fighting or leave
        while True:
            battle_count += 1
            print(f"\n=== Battle {battle_count} ===")
            
            enemy_health = enemy_base_health + (battle_count * 10)  # Increases health by 10 for each battle
            enemy_attack = enemy_base_attack + (battle_count * 2)
            attack_power = base_attack_power + (battle_count * 2)
            enemy = Enemy(f"Coliseum Challenger {battle_count}", enemy_health, enemy_attack, attack_power)
            
            print(f"A fierce {enemy.name} appears with {enemy.health} health and {enemy.attack_power} attack power!")

            # Run combat and check for defeat
            if not self.combat(enemy):  # If combat returns False, the player was defeated
                print("You have been defeated in the Battle Coliseum!")
                break

            # Victory rewards
            gold_reward = 100 + (battle_count * 50)  # Rewards increase with each battle
            print(f"Victory! You earned {gold_reward} gold.")
            self.player.gold += gold_reward
            
            # Chance to win a unique item after every battle
            unique_item_chance = random.random()
            if unique_item_chance < 0.2:  # 20% chance for a unique item
                unique_item = f"Unique Item {battle_count}"
                print(f"You have obtained a {unique_item}!")
                self.player.inventory.append(unique_item)
            
            # Ask if player wants to continue
            choice = input("Do you want to fight the next challenger? (yes/no): ").lower()
            if choice != "yes":
                print(f"You leave the Battle Coliseum after {battle_count} victories, carrying your rewards.")
                break

    def combat(self, enemy):
        print(f"\nYou are fighting a {enemy.name}!")
        while self.player.health > 0 and enemy.is_alive():
            print("\nCombat Actions: [1] Attack [2] Use Item [3] Use Skills [4] Flee")
            combat_choice = input("Choose your action: ")

            if combat_choice == "1":
                self.player.attack(enemy)
                if enemy.is_alive():
                    enemy.attack(self.player)  # Enemy attacks using its attack_power
            elif combat_choice == "2":
                item = input("\nEnter the name of the item to use: ")
                self.player.use_item(item)
                if enemy.is_alive():
                    enemy.attack(self.player)
            elif combat_choice == "3":
                skill_name = input("\nSelect a skill to use: ").title()
                self.player.use_skill(skill_name, enemy)
                if enemy.is_alive():
                    enemy.attack(self.player)
            elif combat_choice == "4":
                print("You fled the battle!")
                return True  # Fleeing is not a defeat, so return True

            # After enemy's turn, check if the player is still alive
            if self.player.health <= 0:
                print("You were defeated!")
                return False  # Return False only when the player's health is 0

        # If the enemy is defeated, return True
        if enemy.health <= 0:
            print(f"You defeated the {enemy.name}!")
            self.player.gain_exp(random.randint(50, 150))
            return True

    def level_up(self):
        self.player.level += 1
        self.player.exp = 0
        self.player.health += 100
        self.player.skill_points += 2  # Earn skill points on level up
        print(f"\nYou leveled up! You are now Level {self.player.level}.")
        print(f"You have earned 2 skill points. Total Skill Points: {self.player.skill_points}\n")

    def upgrade_skills(self):
        self.player.skill_tree.display_skills()
        skill_name = input("Which skill would you like to upgrade? ").title()
        self.player.upgrade_skill(skill_name)

    def show_inventory(self):
        print("\n=== Inventory ===")
        if self.player.inventory:
            for item in self.player.inventory:
                print(f"- {item}")
        else:
            print("Your inventory is empty.")
        print()

    def save_game(self):
        player_data = {
            "name": self.player.name,
            "gold": self.player.gold,
            "health": self.player.health,
            "inventory": self.player.inventory,
            "location": self.player.location,
            "level": self.player.level,
            "exp": self.player.exp,
            "skill_points": self.player.skill_points,
            "skills": {skill: data["level"] for skill, data in self.player.skill_tree.skills.items()}
        }

        with open('save_game.json', 'w') as save_file:
            json.dump(player_data, save_file)
        print("\nGame saved successfully!\n")

    def load_game(self):
        try:
            with open('save_game.json', 'r') as save_file:
                player_data = json.load(save_file)
                self.player.name = player_data["name"]
                self.player.gold = player_data["gold"]
                self.player.health = player_data["health"]
                self.player.inventory = player_data["inventory"]
                self.player.location = player_data["location"]
                self.player.level = player_data["level"]
                self.player.exp = player_data["exp"]
                self.player.skill_points = player_data["skill_points"]

                # Load skills
                for skill, level in player_data["skills"].items():
                    self.player.skill_tree.skills[skill]["level"] = level

            print("\nGame loaded successfully!\n")
            self.player.show_status()
        except FileNotFoundError:
            print("\nNo saved game found!\n")


def create_character():
    print("=== Character Creation ===")
    name = input("Enter your character's name: ")

    # Select Race
    print("\nSelect your race:")
    for idx, race in enumerate(races.keys(), 1):
        print(f"{idx}. {race}")
    race_choice = int(input("\nChoose a race (1-4): ")) - 1
    race = list(races.keys())[race_choice]

    # Select Sub-Race
    print("\nSelect your sub-race:")
    for idx, sub_race in enumerate(sub_races.keys(), 1):
        print(f"{idx}. {sub_race}")
    sub_race_choice = int(input("\nChoose a sub-race (1-6): ")) - 1
    sub_race = list(sub_races.keys())[sub_race_choice]

    return Player(name, race, sub_race)

# Initialize game
player = create_character()
game = Game(player)

game.start()
