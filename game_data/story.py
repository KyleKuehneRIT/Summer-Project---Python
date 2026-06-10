"""
This file contains all of the story/dialogue information for the game.
"""

from hero_class import Assassin, Brawler, Knight, SharpShooter, Sorcerer

# Displays the prologue of the game and allows the user to record their name of choosing.
def introduction():
    print()
    print("A long time ago, there was once a kingdom that prospered. " \
        "For centuries, the kingdom flourished under the royal family, who respected and cared for all of their citizens." \
        " Unfortunately, one day, the kingdom welcomed a evil being into it's walls, whose goal was to destroy everything that was built by the royal family." \
        " To save this kingdom, one hero must rise up and defeat this evil being before the throne is overthrown. \n")
    
    hero_name = input("This hero must be courageous, they must be pure-hearted, they must be strong. This hero's name is.....")
    print()
    print(hero_name + "! \n")

    return hero_name

# Allows the user to select their hero's class at the start of the game.
def character_settings():
    while True:

        hero_class = input("Please select your hero's class. \n\n" \
                            "Classes included: \n" \
                            "Assassin \n"
                            "Brawler \n"
                            "Knight \n"
                            "Sharp-Shooter \n"
                            "Sorcerer \n\n")


        if hero_class == "Assassin":
            hero = Assassin()
            break

        elif hero_class == "Brawler":
            hero = Brawler()
            break

        elif hero_class == "Knight":
            hero = Knight()
            break
        
        elif hero_class == "Sharp-Shooter":
            hero = SharpShooter()
            break
        
        elif hero_class == "Sorcerer":
            hero = Sorcerer()
            break
        
        else:
            print("Invalid class has been selected. Please try again!\n")
    
    print("You are now a(n) " + hero_class + "!")
    print()
    print("Your initial stats are:")
    print("Attack:", hero.attack)
    print("Defense:", hero.defense)
    print("Speed:", hero.speed)
    print("Endurance:", hero.endurance)
    print("Magic:", hero.magic)

    return hero

# Displays the hero's current stats.
def current_stats(hero_name, hero):
    print("\n")
    print("Hero Name:", hero_name)
    print("Hero Class:", hero.hero_class)
    print()
    print("Hero Class Stats:")
    hero.display_stats()


# Contains and runs all other functions defined in this file.
def main():
    hero_name = introduction()
    hero = character_settings()
    current_stats(hero_name, hero)
    
# Executes the main function to run the application.
if __name__ == "__main__":
    main()