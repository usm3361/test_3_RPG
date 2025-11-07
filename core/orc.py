import random
class Orc:
    def __init__(self, name):
        self.name = name
        self.hp = 50
        self.type = "orc"
        self.speed = random.randint(0, 5)
        self.power = random.randint(10, 15)
        self.armor_rating = random.randint(2, 8)
        self.weapon = random.choice(["knife", "sword", "axe"])
    
    def speak(self):
        print(f"`{self.type} {self.name}` is angry!")
        
    def attack(self, player):
        self.speak()
        impact = False
        
        orc_dice = self.roll_dice(20)
        print(f"result dice: {orc_dice}")
        result_orc = self.speed + orc_dice
        print(f"result speed: {result_orc}")
        if result_orc > player.armor_rating:
            print(f"armor player: {player.armor_rating}")
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
        return random.randint(1, sides)        
  
