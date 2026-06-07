"""
This file contains all of the story/dialogue information for the game.
"""

def introduction():
    print()
    print("A long time ago, there was once a kingdom that prospered. " \
        "For centuries, the kingdom flourished under the royal family, who respected and cared for all of their citizens." \
        " Unfortunately, one day, the kingdom welcomed a evil being into it's walls, whose goal was to destroy everything that was built by the royal family." \
        " To save this kingdom, one hero must rise up and defeat this evil being before the throne is overthrown. \n")
    
    user_input = input("This hero must be courageous, they must be pure-hearted, they must be strong. This hero's name is.....")
    print()
    print(user_input + "! \n")

def character_settings():
    user_input = input("Please select your hero's class. \n" \
                        "Classes included: \n" \
                        "Assassin \n"
                        "Brawler \n"
                        "Sharp-Shooter \n"
                        "Knight \n"
                        "Sorcerer \n")
    print()
    print("You are now a(n) " + user_input + "!")

def main():
    introduction()
    character_settings()

if __name__ == "__main__":
    main()