from classes.ninja import Ninja
from classes.pirate import Pirate



def battle_game():
    ninja = Ninja(name="Michelanglo")
    pirate = Pirate(name="Jack Sparrow")

    print("Welcome to the Ninja vs. Pirate Battle Game!")
    print("The battle begins...\n")

    while ninja.health > 0 and pirate.health > 0:

        print("\n--- Ninja's Turn ---")
        action = input("Choose an action: (1) Attack (2) Super Power (3) Show Stats: ")
        if action == "1":
            ninja.attack(pirate)
        elif action == "2":
            ninja.superPower(pirate)
        elif action == "3":
            ninja.show_stats()
        else:
            print("Invalid choice. Skipping turn.")

        if pirate.health <= 0:
            print(f"\n{pirate.name} has been defeated! {ninja.name} wins!")
            break


        print("\n--- Pirate's Turn ---")
        action = input("Choose an action: (1) Attack (2) Super Power (3) Show Stats: ")
        if action == "1":
            pirate.attack(ninja)
        elif action == "2":
            pirate.superPower(ninja)
        elif action == "3":
            pirate.show_stats()
        else:
            print("Invalid choice. Skipping turn.")

        if ninja.health <= 0:
            print(f"\n{ninja.name} has been defeated! {pirate.name} wins!")
            break

    print("\nGame over! Thanks for playing!")


battle_game()
