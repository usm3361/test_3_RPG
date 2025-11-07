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
        print()    

        if choice == "1":
            print("You choice to play, now we'll roll the dice.")
            self.battle(self.create_player(), self.choose_random_monster())
            
        if choice == "2":
            self.exit_game()
            
        
    def exit_game(self):
        print("You chioce not to play, bye friend.")
            
    
    def create_player(self):
        p1 = Player("jef")
        return p1

    
    def choose_random_monster(self):
        self.monster  = random.choice(["orc", "goblin"])
        if self.monster == "orc":
            o1 = Orc("jooo")
            print(f"The type monster is: `orc`, the name is `jooo`.")
            print()
            return o1
        if self.monster == "goblin":
            g1 = Goblin("kokmor")
            print(f"The type monster is: `goblin`, the name is `kokmor.")
            print()
            return g1
    
    def battle(self, player, monster):
        miss = True
        while miss:
            pl_dice = self.roll_dice(6)
            print(f"{player.name} rolled a {pl_dice}")
            result_player = player.speed + pl_dice
            print(f"speed of {player.name} is: {result_player}")
            print()
            mon_dice = self.roll_dice(6)
            print(f"{monster.name} rolled a {mon_dice}")
            result_monster = monster.speed + mon_dice
            print(f"speed of {monster.name} is: {result_monster}")
            print()
            
            if result_player >= result_monster:
                print(f"{player.name} start play")
                player.attack(monster)
            elif result_player < result_monster:
                print(f"{monster.name} start play")
                monster.attack(player)
                
            if player.hp < 0 or monster.hp < 0:
                miss = False
        
        
    def roll_dice(self, sides):
        return random.randint(1, sides)        
        
     
    