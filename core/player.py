import random
class Player:
    def __init__(self, name):
        
        self.name = name
        self.hp = 50
        self.speed = random.randint(5, 10)
        self.power = random.randint(5, 10)
        self.armor_rating = random.randint(5, 15)
        self.profession = random.choice(["Warrior", "Healer"])
        
    def speak(self):
        print(f"{self.name} coming to attack!!")
    
    def attack(self, monster):
        impact = False
        
        player_dice = self.roll_dice(20)  
        result_player =  self.speed + player_dice
        if result_player > monster.armor_rating:
            print("Successful hit")
            impact = True
            
        damage =  self.roll_dice(6) + self.power
        monster.hp -= damage
        if monster.hp <= 0:
            print("The player win, monster is dead.")
            print("end game")
        
        return impact

    def roll_dice(self, sides):
        return random.randint(0, sides)        
