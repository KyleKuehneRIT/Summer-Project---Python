"""
The hero_class.py file contains all the operational logic and stats for the hero classes.
"""

# The main class that is the overall structure for each hero class.
class Hero:

    def __init__(self, hero_class, attack, defense, speed, endurance, magic):
        self.hero_class = hero_class
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.endurance = endurance
        self.magic = magic

    def display_stats(self):
        print("Class:", self.hero_class)
        print("Attack:", self.attack)
        print("Defense:", self.defense)
        print("Speed:", self.speed)
        print("Endurance:", self.endurance)
        print("Magic:", self.magic)

# The Assassin Hero Class.
class Assassin(Hero):

    def __init__(self):
        super().__init__("Assassin", 20, 10, 25, 15, 10)

# The Brawler Hero Class.   
class Brawler(Hero):

    def __init__(self):
        super().__init__("Brawler", 25, 15, 15, 20, 5)

# The Knight Hero Class.
class Knight(Hero):

    def __init__(self):
        super().__init__("Knight", 20, 20, 10, 15, 10)

# The Sharp-Shooter Hero Class.
class SharpShooter(Hero):

    def __init__(self):
        super().__init__("Sharp-Shooter", 15, 10, 20, 10, 15)

# The Sorcerer Hero Class.
class Sorcerer(Hero):

    def __init__(self):
        super().__init__("Sorcerer", 10, 15, 10, 10, 25)

