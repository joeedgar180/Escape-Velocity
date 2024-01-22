# Start: Game Start Code By: Maiwand Ayubi

import time
import sys
import random


def sprint(text, speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)

def aprint(text, speed=0.001):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)

intro_art = (r"""
( ___ )----------------------------------------------------------------------------------------------------------------------------------------------------------( ___ )
 |   |                                                                                                                                                            |   |
 |   |                                                                    Welcome to                                                                              |   | 
 |   |      _______     _______.  ______     ___      .______    _______    ____    ____  _______  __        ______     ______  __  .___________.____    ____     |   | 
 |   |     |   ____|   /       | /      |   /   \     |   _  \  |   ____|   \   \  /   / |   ____||  |      /  __  \   /      ||  | |           |\   \  /   /     |   | 
 |   |     |  |__     |   (----`|  ,----'  /  ^  \    |  |_)  | |  |__       \   \/   /  |  |__   |  |     |  |  |  | |  ,----'|  | `---|  |----` \   \/   /      |   | 
 |   |     |   __|     \   \    |  |      /  /_\  \   |   ___/  |   __|       \      /   |   __|  |  |     |  |  |  | |  |     |  |     |  |       \_    _/       |   | 
 |   |     |  |____.----)   |   |  `----./  _____  \  |  |      |  |____       \    /    |  |____ |  `----.|  `--'  | |  `----.|  |     |  |         |  |         |   | 
 |   |     |_______|_______/     \______/__/     \__\ | _|      |_______|       \__/     |_______||_______| \______/   \______||__|     |__|         |__|         |   | 
 |   |                                                                                                                                                            |   | 
 |___|                                                                                                                                                            |___| 
(_____)----------------------------------------------------------------------------------------------------------------------------------------------------------(_____)
""")

def print_intro_art():
    aprint(intro_art)

time.sleep(1)


def game_over():
    sprint("\nGame Over! Better luck next time.")
    aprint("""
 ██████   █████  ███    ███ ███████      ██████  ██    ██ ███████ ██████  
██       ██   ██ ████  ████ ██          ██    ██ ██    ██ ██      ██   ██ 
██   ███ ███████ ██ ████ ██ █████       ██    ██ ██    ██ █████   ██████  
██    ██ ██   ██ ██  ██  ██ ██          ██    ██  ██  ██  ██      ██   ██ 
 ██████  ██   ██ ██      ██ ███████      ██████    ████   ███████ ██   ██ 
                                                                          
                                                                          
""")
    game_credit()  
    retry = input("Do you want to try again? (yes/no): ")
    
    if retry.lower() == "yes":
        main()
    elif retry.lower() == "no":
        exit()
    else:
        sprint("Invalid choice. Exiting the game.")
        exit()

def game_win():
    sprint("\nYou Won! Amazing Work.")
    aprint("""
██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗    ██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║    ██║
 ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║    ██║
  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║    ╚═╝
   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║    ██╗
   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝    ╚═╝
                                                                                                                                      
""")
    game_credit()


def game_end():
    sprint("\nGame End!")
    aprint("""
 ██████╗  █████╗ ███╗   ███╗███████╗    ███████╗███╗   ██╗██████╗ 
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔════╝████╗  ██║██╔══██╗
██║  ███╗███████║██╔████╔██║█████╗      █████╗  ██╔██╗ ██║██║  ██║
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██╔══╝  ██║╚██╗██║██║  ██║
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ███████╗██║ ╚████║██████╔╝
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝    ╚══════╝╚═╝  ╚═══╝╚═════╝ 
                                                                                                                         
                                                                         
""")
    game_credit()

def game_credit():
    sprint("Credits:\n")
    sprint("    Story By:\n")
    sprint("        Finley Brown\n")
    sprint("    Team Lead By:\n")
    sprint("        Maiwand Ayubi\n")
    sprint("    Developed By:\n")
    sprint("        Maiwand Ayubi\n")
    sprint("        Fawaz Mohammed\n")
    sprint("        Joseph Edgar\n")
    sprint("        Finley Brown\n")
    sprint("        Osas Belinda Ogie\n")
    sprint("    Project Manager:\n")
    sprint("        Keira Jarvis\n")

def start_game():
    sprint("\nYou wake up in a room with a blaring red light.")
    sprint("You see three items:\n")
    sprint("1. Storage room key card\n")
    sprint("2. Broken laser pistol\n")
    sprint("3. Music box\n")

    choice = input("Choose one item (1/2/3): ")

    if choice == "1":
        keycard()
    elif choice == "2":
        broken_laser()
    elif choice == "3":
        music_box()
    else:
        print("\nInvalid choice. Try again.")
        start_game()

#Start: Keycard Code by: Joseph Edgar
def keycard():
    decision = ["1", "2"]
    userInput = ""
    death = random.random()
    attempts = 3

    sprint("You walk out of the room and see a monster around the corner\n")
    time.sleep(2)
    sprint("Do you want to run past the monster or go back for the broken laser pistol?\n1. Run past the monster\n2. Go Back\n")

    while userInput not in decision and attempts > 0:
        userInput = input().lower()
        attempts -= 1
        if attempts > 0 and userInput not in decision:
            sprint("Enter 1 or 2\n")
        elif attempts == 0:
            sprint("Invalid Choice, Exiting the game!\n")

    if userInput == "1" and death < 0.3:
        sprint("The monster chases after you\n")
        time.sleep(2)
        sprint("You can't escape from him... and he kills you...\n")
        time.sleep(2)
        game_over()
    
    elif userInput == "1":
        sprint("The monster chases after you\n")
        time.sleep(2)
        sprint("You survive and escape to a storage room\n")
        time.sleep(2)
        treasure_choice()
        
    elif userInput == "2":
        sprint("You walk back to the room and pick up the broken laser pistol\n")
        broken_laser()
    else:
        game_over()

path = ""

def treasure_choice():

    decision = ["yes", "no"]
    userInput = ""

    sprint("There is valuable treasure in the room. Do you want to take it?\n")
    while userInput not in decision:
        sprint("Enter Yes or No\n")
        userInput = input().lower()

    if userInput == "no":
        sprint("You leave the room and are mauled to death by the monster\n")
        game_over()
    elif userInput == "yes":
        sprint("You take the treasure and continue down the corridor\n")
        time.sleep(2)
        global path
        path = "treasure"
        green_house()
    else:
        sprint("Invalid choice. Please enter Yes or No\n")

#End: Keycard Code by: Joseph Edgar

#Start: Broken Laser Code by: Maiwand Ayubi
def broken_laser():
    sprint("You walk out of the room and hear a noise.\n")
    time.sleep(2)
    sprint("You see a monster and decide to shoot it with the broken laser pistol.\n")

    if random.random() < 0.8:
        sprint("The gun fires, and you successfully shoot the monster.\n")
        time.sleep(2)
        sprint("You continue onwards and see a room with lights still on.\n")
        time.sleep(2)
        green_house()
    else:
        sprint("The gun didn't fire! The monster attacks you, and you die.\n")
        game_over()

#End: Broken Laser Code by: Maiwand Ayubi

# Start: Music Box Code By: Finley Brown
def music_box():
    sprint("You pick up the music box and walk out of the room; it is pitch black.\n")
    time.sleep(2)

    if random.random() < 0.05:
        time.sleep(1)
    sprint("As you hold the music box, you hear a faint whisper in the darkness...\n")
    time.sleep(2)
    sprint(". . . . . . .\n")

    time.sleep(1)
    sprint("On the floor, you see a flashlight and a working laser pistol.\n")

    while True:
        game_decision = input("Do you pick them up? (Yes/No): \n").lower()

        if game_decision == "yes":
            sprint("You pick them up, and a monster drops down. You shoot it straight in the head.\n")
            time.sleep(1)
            if random.random() < 0.1:
                sprint("The monster survives and kills you!!!\n")
                game_over()
            else:
                sprint("You kill the monster!\n")
                green_house()
            break  # Exit the loop after a valid choice

        elif game_decision == "no":
            sprint("You decide not to pick them up, and the monster drops down and kills you.\n")
            time.sleep(1)
            game_over()
            break  # Exit the loop after a valid choice

        else:
            sprint("Invalid choice. Please enter 'Yes' or 'No'\n")

# End: Music Box Code By: Finley Brown

def green_house():
    sprint("You see a light down the corridor, you go towards it.\n")
    time.sleep(2)
    sprint("You make it to the greenhouse on the station.\n")
    time.sleep(2)
    sprint("You exit the greenhouse and there is a man standing down the hall...\n")
    time.sleep(2)
    if path == "treasure":
        treasure_path()
    else:
        laser_path()

def treasure_path():
    attempts = 3

    while attempts > 0:
        sprint("you have treasure, you can bribe the man to let you past\n")
        time.sleep(2)
        player_choice = input("Do you want to bribe him? (yes/no): \n")

        if player_choice.lower() == "yes":
            global man_status
            man_status = "befriended"
            sprint("You give him your treasure and he thanks you, he runs away\n")
            time.sleep(2)
            sprint("You continue going down the hall\n")
            lifepods()
            break
        elif player_choice.lower() == "no":
            man_status = "ranoff"
            sprint("He takes your treasure anyway and runs off\n")
            time.sleep(2)
            sprint("You continue going down the hall\n")
            time.sleep(2)
            lifepods()
            break
        else:
            attempts -= 1
            sprint(f"Invalid input! You have {attempts} attempts remaining.\n")

            if attempts == 0:
                sprint("Game over because you ran out of attempts.\n")
                game_over()

def fifty_fifty_scenario():
    result = random.choices([True, False], weights=[0.5, 0.5])[0]
    return result
    


def laser_path():
    for attempt in range(3):
        sprint("You have a laser pistol, you can shoot him\n")
        time.sleep(1)
        player_choice = input("Do you want to shoot him? (yes/no): \n").lower()

        if player_choice == "yes":
            sprint("Your gun jams, and he charges at you with a knife\n")
            time.sleep(2)
            outcome = fifty_fifty_scenario()
            
            if outcome:
                sprint("You survived! Continue down the hall\n")
                time.sleep(2)
                global man_status
                man_status = "dead"
                lifepods()
            else:
                sprint("He overpowered you, and you died from your injuries\n")
                time.sleep(2)
                game_over()
            break 

        elif player_choice == "no":
            sprint("You befriend the man and go your separate ways\n")
            time.sleep(2)
            man_status = "befriended"
            sprint("You continue going down the hall\n")
            time.sleep(2)
            lifepods()
            break

        else:
            sprint(f"Invalid input. Please enter 'yes' or 'no'. You have {2 - attempt} attempts remaining.\n")
            if attempt == 2:
                game_over()
                break

def lifepods():
    sprint("You make it to the Lifepod Bay, there are only two lifepods left.\n")
    time.sleep(2)

    attempts_remaining = 3

    while attempts_remaining > 0:
        sprint("Do you pick Lifepod 1 or Lifepod 2\n")
        choice = input("Enter '1' or '2':\n").lower()

        if choice == '1':
            lifepod_one()
            break
        elif choice == '2':
            lifepod_two()
            break
        else:
            attempts_remaining -= 1
            if attempts_remaining > 0:
                sprint(f"Invalid choice. Please enter '1' or '2'. {attempts_remaining} attempts remaining.\n")
            else:
                sprint("You've reached the maximum number of attempts. Exiting the game.")
                game_over()


def probability_scenario(h,l):
    result = random.choices([True, False], weights=[h, l])[0]
    return result

def lifepod_one():
    sprint("The door shuts and locks behind you...\n")
    time.sleep(1)
    sprint("The wires are faulty...\n")
    time.sleep(1)
    sprint("A fire starts...\n")
    time.sleep(1)
    sprint("The lifepod is now not functional and you get trapped...\n")
    time.sleep(2)

    if man_status=="dead":
        sprint("With no one else on the ship its really hard to get out...\n")
        time.sleep(2)
        sprint("You try your best to get out...\n")
        time.sleep(1)
        dead_pro=probability_scenario(20,80)
        if dead_pro==True:
            sprint("You manage to open the door and leave Lifepod 1\n")
            sprint("You move over to lifepod 2\n")
            lifepod_two()
            
        else:
            sprint("You tried hard but couldn't get out of the Lifepod...\n")
            game_end()

    elif man_status=="ranoff":
        sprint("The man who ran off with your treasure comes to your rescue...\n")
        time.sleep(2)
        sprint("He tries his best...\n")
        ranoff_pro=probability_scenario(0.5,.50)
        if ranoff_pro==True:
            sprint("He manages to open the door and you survive\n")
            time.sleep(2)
            sprint("You move over to lifepod two\n")
            lifepod_two()
            
        else:
            sprint("He tries to open the door but fails...\n")
            time.sleep(2)
            sprint("He tried hard but couldn't open the door for you...\n")
            game_over()

    elif man_status=="befriended":
        sprint("The man you befriended come to rescue...\n")
        time.sleep(2)
        sprint("He pushes the door and after a couple of tries he opens the door...\n")
        time.sleep(2)
        sprint("You move over ot lifepod two\n")
        time.sleep(2)
        lifepod_two()


def lifepod_two():
    sprint("You enter lifepod 2, there is some faulty wiring you quickly try to fix it\n")
    time.sleep(2)

    fix = random.random()
    sprint("You try to fix the wiring...\n")
    time.sleep(2)
    if fix < 0.2:
        sprint("You could not fix the wiring and you are trapped on the ship...\n")
        time.sleep(2)
        sprint("This is now your life...\n")
        time.sleep(2)
        game_end()
    else:
        print("You managed to fix the wiring and you escape the ship\n")
        game_win()

def main():
    print_intro_art()

    attempts_remaining = 3

    while attempts_remaining > 0:
        ready_to_start = input("\nAre you ready to escape the space station? (yes/no): ").lower()

        if ready_to_start == "yes":
            break
        elif ready_to_start == "no":
            reconsider_attempts = 2
            while reconsider_attempts > 0:
                reconsider_choice = input("\nAre you sure? Type 'yes' to continue or 'no' to reconsider: ").lower()
                if reconsider_choice == "yes":
                    break
                elif reconsider_choice == "no":
                    reconsider_attempts -= 1
                    if reconsider_attempts == 0:
                        print("\nYou've reached the maximum number of reconsideration attempts. Exiting the game.")
                        exit()
                    else:
                        print(f"\nInvalid choice. Please enter 'yes' or 'no'. {reconsider_attempts} attempts remaining.")
                else:
                    print(f"\nInvalid choice. Please enter 'yes' or 'no'. {reconsider_attempts} attempts remaining.")
            if reconsider_choice == "yes":
                break
        else:
            attempts_remaining -= 1
            if attempts_remaining == 0:
                print("\nYou've reached the maximum number of attempts. Exiting the game.")
                exit()
            else:
                print(f"\nInvalid choice. Please enter 'yes' or 'no'. {attempts_remaining} attempts remaining.")


    player_name = input("\nWhat's your name? ")
    sprint(f"\nWelcome, {player_name}!")

    start_game()

main()

# End: Game Start Code By: Maiwand Ayubi


# - ////////////////////////////////////////////////////////////////////
# - ////////////////////////////////////////////////////////////////////
# Credits:
#     Story By:
#         Finley Brown
#     Team Lead By:
#         Maiwand Ayubi
#     Developed By:
#         Maiwand Ayubi
#         Fawaz Mohammed
#         Joseph Edgar
#         Finley Brown
#         Osas Belinda Ogie
#     Project Manager:
#         Keira Jarvis