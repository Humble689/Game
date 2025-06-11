def combat(player, enemy):
    print(f"{player.name} enters combat with {enemy.name}!")
    while player.health > 0 and enemy.health > 0:
        action = input("Choose action: 1) Attack 2) Heal\n")
        if action == "1":
            player.attack(enemy)
            if enemy.health <= 0:
                print(f"{enemy.name} has been defeated!")
                player.experience += 10
                if player.experience >= 100:
                    player.level_up()
                break
            enemy.attack(player)
        elif action == "2":
            player.heal(10)
            enemy.attack(player)
        else:
            print("Invalid action. Try again.")
