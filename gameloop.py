def main():
    player_name = input("Enter your character's name: ")
    player = Player(player_name, 100, 15, 5)

    town = Location("Town", "A peaceful town with shops and people.")
    forest_enemy = Enemy("Goblin", 50, 10, 2)
    forest = Location("Forest", "A dark, mysterious forest.", forest_enemy)

    locations = [town, forest]

    print(f"\nWelcome to the game, {player.name}!")
    while player.health > 0:
        print(f"\n{player.name}'s Health: {player.health} | Level: {player.level}")
        print("Where would you like to go?")
        for idx, location in enumerate(locations):
            print(f"{idx + 1}. {location.name}")
        choice = input("Choose a location (1-2): ")

        if choice == "1":
            town.enter(player)
        elif choice == "2":
            forest.enter(player)
        else:
            print("Invalid choice. Try again.")

        if player.health <= 0:
            print(f"\n{player.name} has been defeated. Game Over.")
            break

if __name__ == "__main__":
    main()
