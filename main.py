import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='sqlzach01$',
    port='3306',
    database='pokedex_project'
)

if __name__ == '__main__':
    value = 0
    exit_program = False
    exit_search = False
    exit_pokemon = False
    valid_name = False
    valid_type = False

    mycursor = mydb.cursor()

    print("Welcome the Pokedex (GEN 1 Edition)! \n"
          "This is every the original 151 Gen 1 Pokemon updated to the newest Gen today (Gen 8)\n"
          "A lot of changes was made to these Pokemon over time so take and a look and see "
          "what changed was made since then.\n"
          "Please enter the number of the option below on what would you like to do:\n")

    while not exit_program:
        value = input("Main Menu of the Pokedex:\n"
                      "1: Search the name of the Pokemon or the Pokemon ID (Between 1 and 151) \n"
                      "2: Sort by Type\n"
                      "3: Display all available Pokemon and their elemental properties\n"
                      "4: Exit the Pokedex\n")

        # If Sort by Type
        if value == "1":
            exit_search = False
            # While loop until user exit the search for Pokemon or ID
            while not exit_search:
                user_input = input("Please input the name of the Pokemon or the ID: \n")

                # Checks if input is ID
                if user_input.isnumeric():
                    if 0 < int(user_input) < 152:
                        # mycursor = mydb.cursor()

                        mycursor.execute(
                            "SELECT Name, Height, Weight, Base_Total, HP, Attack, Defense, Special_Attack, "
                            "Special_Defense, Speed FROM pokemon WHERE ID=" + user_input)

                        users = mycursor.fetchall()

                        for user in users:
                            print("Pokemon: " + (user[0]) + "\nHeight: " + str(user[1]) + "m\nWeight: " + str(user[2]) +
                                  "kg\nHP: " + str(user[4]) + "\nAttack: " + str(user[5]) + "\nDefense: " + str(
                                user[6]) +
                                  "\nSpecial Attack: " + str(user[7]) + "\nSpecial Defense: " + str(user[8]) +
                                  "\nSpeed: " + str(user[9]) + "\nBase Total: " + str(user[3]))

                        print("\nPlease select one of the available options below on what else "
                              "you would like to know about this Pokemon:")

                        # while loop until the user want to search for a new Pokemon
                        exit_pokemon = False
                        while not exit_pokemon:

                            option = input("1: Type Advantage and Disadvantage\n"
                                           "2: Gender Rate\n"
                                           "3: Ability\n"
                                           "4: Species\n"
                                           "5: Search for another Pokemon\n"
                                           "6: Quit and return to Main Menu\n")

                            # If the user wants to view type
                            if option == "1":
                                mycursor.execute(
                                    'SELECT pokemon.Name, type.Type1, type.Type2, type.Strength, type.Weakness '
                                    'FROM pokemon INNER JOIN type ON pokemon.Type_ID = type.TYPE_ID WHERE ID='
                                    + user_input)

                                users = mycursor.fetchall()

                                for user in users:
                                    print(
                                        "Pokemon: " + (user[0]) + "\nType 1: " + (user[1]) + "\nType 2: " + (user[2]) +
                                        "\nStrength: " + (user[3]) + "\nWeakness: " + (user[4]) + "\n")

                            # If the user wants to view gender rates
                            elif option == "2":
                                mycursor.execute('SELECT pokemon.Name, gender.Male_Pct, gender.Female_Pct FROM pokemon '
                                                 'INNER JOIN gender ON pokemon.Gender_ID = gender.Gender_ID '
                                                 'WHERE ID=' + user_input)

                                users = mycursor.fetchall()

                                for user in users:
                                    print("Pokemon: " + (user[0]) + "\nMale Percentage: " + str((user[1])) +
                                          "\nFemale Percentage: " + str((user[2])) + "\n")

                            # check if user want to view ability
                            elif option == "3":
                                mycursor.execute('SELECT pokemon.Name, ability.Ability1, ability.Ability2, '
                                                 'ability.Hidden_Ability FROM pokemon INNER JOIN ability '
                                                 'ON pokemon.Ability_ID = ability.Ability_ID WHERE ID=' + user_input)

                                users = mycursor.fetchall()

                                for user in users:
                                    print("Pokemon: " + (user[0]) + "\nFirst Ability: " + (user[1]) +
                                          "\nSecond Ability: " + (user[2]) + "\nHidden Ability: " + (user[3]) + "\n")

                            # check if user want to view species
                            elif option == "4":
                                mycursor.execute('SELECT pokemon.Name, species.Name FROM pokemon INNER JOIN species '
                                                 'ON pokemon.Species_ID = species.Species_ID WHERE ID=' + user_input)

                                users = mycursor.fetchall()

                                for user in users:
                                    print("Pokemon: " + (user[0]) + "\nSpecies: " + (user[1]) + " Pokemon\n")

                            # check if user wants to search for another Pokemon
                            elif option == "5":
                                exit_pokemon = True

                            # check if user want to go back to main menu
                            elif option == "6":
                                exit_search = True
                                exit_pokemon = True

                            else:
                                print("That is not a valid input, please try again.\n")

                    else:
                        print("That is not a valid ID. Please try again")

                else:
                    valid_name = False
                    # Check the name of Pokemon to see if the input is valid
                    mycursor.execute('SELECT Name FROM pokemon')
                    users = mycursor.fetchall()

                    # capitalize the first letter
                    user_input = user_input.capitalize()

                    for user in users:
                        if (user[0]) == user_input:
                            valid_name = True

                    # Checks if input is a valid name

                    if valid_name:
                        mycursor.execute(
                            "SELECT Name, Height, Weight, Base_Total, HP, Attack, Defense, Special_Attack, "
                            "Special_Defense, Speed FROM pokemon WHERE Name=" + "'" + user_input + "'")

                        users = mycursor.fetchall()

                        for user in users:
                            print("Pokemon: " + (user[0]) + "\nHeight: " + str(user[1]) + "m\nWeight: " + str(
                                user[2]) +
                                  "kg\nHP: " + str(user[4]) + "\nAttack: " + str(user[5]) + "\nDefense: " + str(
                                user[6]) +
                                  "\nSpecial Attack: " + str(user[7]) + "\nSpecial Defense: " + str(user[8]) +
                                  "\nSpeed: " + str(user[9]) + "\nBase Total: " + str(user[3]))

                        print("\nPlease select one of the available options below on what else "
                              "you would like to know about this Pokemon:")

                        # while loop until the user want to search for a new Pokemon
                        exit_pokemon = False
                        while not exit_pokemon:

                            option = input("1: Type Advantage and Disadvantage\n"
                                           "2: Gender Rate\n"
                                           "3: Ability\n"
                                           "4: Species\n"
                                           "5: Search for another Pokemon\n"
                                           "6: Quit and return to Main Menu\n")

                            # If the user wants to view the Pokemon type weaknesses and strengths
                            if option == "1":
                                mycursor.execute(
                                    'SELECT pokemon.Name, type.Type1, type.Type2, type.Strength, type.Weakness '
                                    'FROM pokemon INNER JOIN type ON pokemon.Type_ID = type.TYPE_ID '
                                    'WHERE pokemon.Name=' + "'" + user_input + "'")

                                users = mycursor.fetchall()

                                for user in users:
                                    print("Pokemon: " + (user[0]) + "\nType 1: " + (user[1]) + "\nType 2: " + (
                                        user[2]) + "\nStrength: " + (user[3]) + "\nWeakness: " + (user[4]) + "\n")

                            # If the user wants to view the Pokemon's gender rates
                            elif option == "2":
                                mycursor.execute(
                                    'SELECT pokemon.Name, gender.Male_Pct, gender.Female_Pct FROM pokemon '
                                    'INNER JOIN gender ON pokemon.Gender_ID = gender.Gender_ID '
                                    'WHERE pokemon.Name=' + "'" + user_input + "'")

                                users = mycursor.fetchall()

                                for user in users:
                                    print("Pokemon: " + (user[0]) + "\nMale Percentage: " + str((user[1])) +
                                          "\nFemale Percentage: " + str((user[2])) + "\n")

                            # check if user want to view the Pokemon ability
                            elif option == "3":
                                mycursor.execute('SELECT pokemon.Name, ability.Ability1, ability.Ability2, '
                                                 'ability.Hidden_Ability FROM pokemon INNER JOIN ability '
                                                 'ON pokemon.Ability_ID = ability.Ability_ID '
                                                 'WHERE Pokemon.Name=' + "'" + user_input + "'")

                                users = mycursor.fetchall()

                                for user in users:
                                    print("Pokemon: " + (user[0]) + "\nFirst Ability: " + (user[1]) +
                                          "\nSecond Ability: " + (user[2]) + "\nHidden Ability: " + (
                                              user[3]) + "\n")

                            # check if user want to view the Pokemon species
                            elif option == "4":
                                mycursor.execute(
                                    'SELECT pokemon.Name, species.Name FROM pokemon INNER JOIN species '
                                    'ON pokemon.Species_ID = species.Species_ID '
                                    'WHERE pokemon.Name=' + "'" + user_input + "'")

                                users = mycursor.fetchall()

                                for user in users:
                                    print("Pokemon: " + (user[0]) + "\nSpecies: " + (user[1]) + " Pokemon\n")

                            # check if user wants to search for another Pokemon
                            elif option == "5":
                                exit_pokemon = True

                            # check if user want to go back to main menu
                            elif option == "6":
                                exit_search = True
                                exit_pokemon = True

                            else:
                                print("That is not a valid input, please try again.\n")

                    else:
                        print("That is not a valid Pokemon. Please try again")

        # check if user want to sort the list of Pokemon by type
        elif value == "2":
            valid_type = False
            print("There are 18 official type of Pokemon: Normal, Fire, Water Grass, Electric, Ice, Fighting, Poison, "
                  "\nGround, Flying, Psychic, Bug, Rock, Ghost, Dark, Dragon, Steel, and Fairy.\nIf the User wants "
                  "only to display Grass type, the input will be grass and will display all grass types in Gen 1.\n")

            # While loop until the user inputs a valid type name
            while not valid_type:

                user_input = input("Please enter what Pokemon Type element you would like to sort by: ")

                mycursor.execute('SELECT pokemon.ID, pokemon.name, type.Type1, type.Type2 FROM pokemon inner join type '
                                 'ON pokemon.Type_ID = type.Type_ID WHERE type.Type1=' + "'" + user_input + "'" +
                                 ' OR type.Type2 =' + "'" + user_input + "'" + 'GROUP BY pokemon.ID '
                                                                               'ORDER BY pokemon.ID ASC')

                users = mycursor.fetchall()

                user_input = user_input.capitalize()

                # Check if user input is a valid Pokemon type
                for user in users:
                    if (user[2]) == user_input:
                        valid_type = True

                if valid_type:
                    print("--------------------------------------------------\n"
                          "|   ID   |   Pokemon   |   Type 1   |   Type 2   |\n"
                          "|--------|-------------|------------|------------|")

                    for user in users:
                        print("|", str(user[0]), " " * (5 - len(str(user[0]))), "|", user[1], " " * (10 - len(user[1])),
                              "|",
                              user[2], " " * (9 - len(str(user[2]))), "|", user[3], " " * (9 - len(str(user[3]))), "|")

                    print("--------------------------------------------------")

                else:
                    print("That is not a valid Pokemon Type, please try again.")

        # shows the user a list of all available Pokemon
        elif value == "3":
            mycursor.execute('SELECT pokemon.ID, pokemon.name, type.Type1, type.Type2 FROM pokemon inner join type '
                             'ON pokemon.Type_ID = type.Type_ID GROUP BY pokemon.ID ORDER BY pokemon.ID ASC;')

            users = mycursor.fetchall()

            print("--------------------------------------------------\n"
                  "|   ID   |   Pokemon   |   Type 1   |   Type 2   |\n"
                  "|--------|-------------|------------|------------|")

            for user in users:
                print("|", str(user[0]), " " * (5 - len(str(user[0]))), "|", user[1], " " * (10 - len(user[1])), "|",
                      user[2], " " * (9 - len(str(user[2]))), "|", user[3], " " * (9 - len(str(user[3]))), "|")

            print("--------------------------------------------------")

        elif value == "4":
            print("Exiting...")

            exit_program = True
        else:
            print("That is not a valid input, please enter one of the option below\n")
