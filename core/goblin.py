import random
class Goblin:
    def __init__(self, name):
        self.name = name
        self.hp = 20
        self.type = "goblin"
        self.speed = random.randint(5, 10)
        self.power = random.randint(10, 15)
        self.armor_rating = 1
        self.weapon = random.choice(["knife", "sword", "axe"])
    
    def speak(self):
        print(f"Beware, `{self.type} {self.name}` is coming!!")
        
    def attack(self, player):
        impact = False
        
        goblin_dice = self.roll_dice(20)  
        result_goblin = self.speed + goblin_dice      
        if result_goblin > player.armor_rating:
            print("Successful hit")
            impact = True
            damage =  self.roll_dice(6) + self.power
            if self.weapon == "knife":
                damage = damage * 0.5
            elif self.weapon == "sword":
                damage = damage * 1
            elif self.weapon == "axe":
                damage = damage * 1.5
            
            player.hp -= damage
            if player.hp <= 0:
                print("The Monster win, player is dead.")
                print("end game")

        return impact
    
    def roll_dice(self, sides):
        return random.randint(0, sides)        
  
