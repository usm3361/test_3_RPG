import random
from core.player import Player
from core.orc import Orc
from core.goblin import Goblin

class Game:    
    def start(self):
        self.show_menu()
        
    def show_menu(self):
        print("\n=== Menu game ===")
        print("1) play run game")
        print("2) exit game")
        choice = input("Select an action (1 or 2): ").strip()    

        if choice == "1":
            self.battle(self.create_player(), self.choose_random_monster())
            
        if choice == "2":
            self.exit_game()
            
        
    def exit_game(self):
        print("You chose not to play, bye friend.")
            
    
    def create_player(self):
        p1 = Player("jef")
        return p1

    
    def choose_random_monster(self):
        self.monster  = random.choice(["orc", "goblin"])
        if self.monster == "orc":
            o1 = Orc("jooo")
            return o1
        if self.monster == "goblin":
            g1 = Goblin("kokmor")
            return g1
    
    def battle(self, player, monster):
        miss = True
        while miss:
            pl_dice = self.roll_dice(6)
            result_player = player.speed + pl_dice
            mon_dice = self.roll_dice(6)
            result_monster = monster.speed + mon_dice
            
            if result_player == result_monster:
                player.attack(monster)
            elif result_player > result_monster:
                player.attack(monster)
            elif result_player < result_monster:
                monster.attack(player)
                
            if player.hp < 0 or monster.hp < 0:
                miss = False
        
        
    def roll_dice(self, sides):
        return random.randint(0, sides)        
        
     
    