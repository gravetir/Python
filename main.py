from random import randint

class MixinHealth:
    def __init__(self, health):
        self.health = health

class MixinWeapon:
    def __init__(self, w_class, max_damage) -> None:
        self.w_class = w_class
        self.max_damage = max_damage
        self.durability = 10
    
    def attack(self, soldier):
        if self.durability > 0:
            dmg = randint(0, self.max_damage) 
        else:
            dmg = 0
        print(f"I attack {soldier} for {dmg} damage")
        soldier.take_damage(dmg)
        self.durability -= 1

class AliveSoldier(MixinHealth, MixinWeapon):
    def __init__(self, health, w_class, max_damage, team: str) -> None:
        MixinWeapon.__init__(self, w_class, max_damage)
        MixinHealth.__init__(self, health)
        self.team = team
    
    def take_damage(self, amount):
        print(f"I take {amount} damage")
        self.health -= amount
        print(f"I have {self.health} health left")
        if self.health <= 0:
            del self
    
class Army:
    def __init__(self, name, team, amount) -> None:
        self.name = name
        self.team = team
        self.soldiers = [
            AliveSoldier(100, ["Sword", "Bow", "Crossbow"][randint(0,2)], randint(10,50), team)
            for i in range(amount)
        ]

    def get_soldiers(self):
        return self.soldiers

    def update_soldiers(self, soldiers):
        self.soldiers = soldiers

    def __repr__(self) -> list:
        return self.soldiers

    def check_soldiers(self):
        if len(self.soldiers) > 0:
            return True
        else:
            return False

    def attack_army(self, other_army):
        for i in self.soldiers:
            i.attack(other_army.get_soldiers()[randint(0, len(other_army.get_soldiers())-1)])

def epic_battle(*armies):
    red_indexes = []
    blu_indexes = []
    for i in range(len(armies)):
        if armies[i].team == "red":
            red_indexes.append(i)
        else:
            blu_indexes.append(i)
    
    # while True:
    for i in range(20):
        for army in armies:
            if army.team == "red":
                army.attack_army(armies[blu_indexes[randint(0,len(blu_indexes)-1)]])
        armies_left = 0
        for army in armies:
            if army.check_soldiers:
                armies_left += 1
        if armies_left <= 1:
            break
        print(armies_left)
    print(f"_ Army with name _ wins!")


blu_1 = Army("Goblins", "blue", 10)
red_1 = Army("Orcs" , "red", 10)
blu_2 = Army("Space marines" ,"blue", 20)
red_2 = Army("Pirates", "red", 20)

epic_battle(blu_1, blu_2, red_1, red_2)