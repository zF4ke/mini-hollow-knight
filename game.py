import random

class Vessel:
    def __init__(self, health = 30, soul = 0, power = 5, chance = 30):
        self.health = health
        self.soul = soul
        self.power = power
        self.chance = chance

    def take_damage(self, damage):
        if random.randint(1, 100) <= self.chance:
            print("(Vessel dodged the attack!)")
            return self.health
        
        self.health -= damage
        return self.health
    
    def nail_attack(self):
        damage = self.power + random.randint(0, 2)
        if self.soul < 3:
            self.soul += 1
        print(f"\n- Vessel swings its nail and deals {damage} damage! Has {self.soul} soul")
        return damage, self.soul
    
    def soul_focus(self):
        if self.soul > 0:
            if self.health < 30:
                self.soul -= 1
                self.health += 7 + random.randint(0, 3)
                
                if self.health > 30:
                    self.health = 30 
                print(f"\n- Vessel focuses 1 soul and heals to {self.health}hp! {self.soul} soul left")
                return self.soul, self.health, False   
            else:
                self.soul -= 1
                print(f"\n- Vessel focuses 1 soul and heals to {self.health}hp! {self.soul} soul left")
                return self.soul, self.health, False
        else:
            print(f"\nNot enough soul to heal!")
            return self.soul, self.health, True
        
    def cast_spell(self, spell):
        spells = {
            "vengeful spirit": {"cost": 2, "damage": 15},
            "howling wraiths": {"cost": 3, "damage": 25},
        }

        if spell in spells:
            if self.soul >= spells[spell]["cost"]:
                self.soul -= spells[spell]["cost"]
                print(f"- Vessel casts {spell.title()}, dealing {spells[spell]['damage']} damage!")
                return spells[spell]["damage"]
            else:
                print("Not enough soul!")
                return 0
        else:
            print("Unknown spell!")
            return 0
    

class Enemy:
    def __init__(self, name, health, attack, chance, description):
        self.name = name
        self.health = health
        self.attack = attack
        self.chance = chance
        self.description = description

    def take_damage(self, damage):
        if random.randint(1, 100) <= self.chance:
            print(f"({self.name} dodged the attack!)")
            return self.health

        self.health -= damage

    def attack_player(self):
        damage = self.attack + random.randint(0, 2)
        int = random.randint(1, len(self.description)) - 1
        print(f"\n- {self.name} {self.description[int]}")
        return damage
    

def stats():
    print(f"\nVessel: {knight.health}hp | {knight.soul} soul")

knight = Vessel()
enemies = [
    Enemy("Lost Kin", health = 10, attack = 3, chance = 20, description = ["swings its nail around!", "spits a ball of radiance!"]),
    Enemy("Soul Tyrant", health = 15, attack = 5, chance = 30, description = ["desolate dives onto the ground!", "casts a soul orb!"]),
    Enemy("Nightmare King Grimm", health = 25, attack = 7, chance = 10, description = ["summons his dragons!", "dashes into the air!", "spawns fire from below!"])
]


def round():
    print("\nWelcome to mini Hollow Knight!")
    for enemy in enemies:
        print(f"〉A NEW CHALLENGER HAS APPEARED: {enemy.name}!! 〈")

        while knight.health > 0 and enemy.health > 0:
            def act():
                invalid = False
                print("\n - - - NEW TURN - - -")
                stats()

                action = input("Choose action [ attack / heal / spell ] : ").strip().lower()

                if action == "attack":
                    damage, _ = knight.nail_attack()
                    enemy.take_damage(damage)

                elif action == "heal":
                    s, h, k = knight.soul_focus()
                    if k == True:
                        act()
                        return

                elif action == "spell":
                    spell = input("Choose a spell [ Vengeful Spirit / Howling Wraiths ] : ")
                    damage = knight.cast_spell(spell)
                    enemy.take_damage(damage)
                
                else:
                    print("Invalid input!")
                    invalid = True

                if enemy.health > 0 and invalid == False:
                    enemy_damage = enemy.attack_player()
                    knight.take_damage(enemy_damage)

            act()

        if knight.health <= 0:
            print(f"\nYou were killed by {enemy.name}! May your shade find peace")
            break
        else:
            print(f"\n{enemy.name} has been defeated!")

    if knight.health > 0:
        print("\nYou killed all the enemies, and saved the kingdom! Well done, mighty Vessel.")

round()