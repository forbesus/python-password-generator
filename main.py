#!/bin/bash

# Random password generator by Mohamed Tarek
# Program made by a non-expert programmer to try something
# Colour designs by Roopa Pabolu
# All rights reserved © 2021

import logging as log
import random
from string import *
import hashlib
import binascii
import colorama as cl


log.basicConfig(

    level=log.INFO,
    format="%(asctime)s:%(message)s",
    filename="generatedPasswords.log"

)

cl.init(autoreset=True)

Error = cl.Fore.RED
Success = cl.Fore.GREEN
Message = cl.Style.BRIGHT
menuHeading = cl.Fore.YELLOW
Choices = cl.Fore.BLUE


# Errors - LengthError
class LengthError(Exception):
    pass


# Password generating
def pass_gen_all(max_range_all):
    # Initializing - removing unwanted characters from the variable
    chars = list(printable)  # Imported from string - Has all the possible printable characters in the ASCII
    chars.pop(85)
    for p in range(6):
        chars.pop()
    password = ""
    max_range_all = int(max_range_all)
    if max_range_all == 0:
        print(f"{Success}Exited")
        exit()
    else:
        for i in range(max_range_all):
            password += random.choice(chars)
        print(f"{Message}Generated password: {Success}{password}")
        log.info(f"Password: {password}\n")


def pass_gen_nocapitals(max_range_nocapitals):
    temp = ascii_lowercase + digits + punctuation  # Imported from string
    chars = list(temp)
    chars.pop(59)
    password = ""
    max_range_nocapitals = int(max_range_nocapitals)
    if max_range_nocapitals == 0:
        print(f"{Success}Exited")
        exit()
    else:
        for i in range(max_range_nocapitals):
            password += random.choice(chars)
        print(f"{Message}Generated password: {Success}{password}")
        log.info(f"Password: {password}\n")


def pass_gen_nosymbols(max_range_nosymbols):
    chars = list(printable)
    chars.pop(85)
    for s in range(37):
        chars.pop()
    password = ""
    max_range_nosymbols = int(max_range_nosymbols)
    if max_range_nosymbols == 0:
        print(f"{Success}Exited")
        exit()
    else:
        for i in range(max_range_nosymbols):
            password += random.choice(chars)
        print(f"{Message}Generated password: {Success}{password}")
        log.info(f"Password: {password}\n")


def int_length_checker(int_length):
    if int(int_length) < 9 or int(int_length) > 42:  # Editable
        raise LengthError(
            f"{Error}Please enter a range between 9 and 42. Mostly passwords below or above that range are not usable.")


def app_starter():
    print(f"""{Message}

Random password generator by Mohamed Tarek.

All rights reserved © 2021

Enter 0 to exit the program.
""")


def main_menu():
    print(f"""{menuHeading}
Please select any of the below choices:

{Choices}
1. Generate a random password
2. View all the generated passwords
3. Hash a password
4. View all the ASCII characters
5. Contact developer
6. Help

""")


def pass_options():
    print(f"""{menuHeading}
Select one of the below options:
{Choices}
1. Include everything (Recommended)
2. Don't include symbols
3. Don't include Uppercase letters


""")


def hash_options():
    print(f"""{menuHeading}

Please choose one of the below hashing type:
{Choices}
1. SHA256 (Recommended)
2. MD5

""")


def contact_details():
    print(f"""{Success}

Contact details ----------------------------------------------------------------

-> Email: eaglechannel611@gmail.com

socials ------------------------------------------------------------------------

-> Instagram: _7amoodtarek

""")


if __name__ == "__main__":
    app_starter()
# Infinite loop - program won't stop unless an argument of 0
while True:
    try:
        if __name__ == "__main__":
            main_menu()
        choice_num = int(input("> "))
        if choice_num == 0:
            print(f"{Success}Exited")
            exit()
        if choice_num == 1:
            try:
                print(f"{menuHeading}Enter a range: ")
                max_range = int(input("> "))
                if max_range == 0:
                    print(f"{Success}Exited")
                    exit()
                if __name__ == "__main__":
                    int_length_checker(max_range)
                while True:
                    try:
                        if __name__ == "__main__":
                            pass_options()
                        password_opt = int(input("> "))
                        if password_opt == 0:
                            print(f"{Success}Exited")
                            exit("")
                        if password_opt == 1:
                            if __name__ == "__main__":
                                pass_gen_all(max_range)
                            break
                        elif password_opt == 2:
                            if __name__ == "__main__":
                                pass_gen_nosymbols(max_range)
                            break
                        elif password_opt == 3:
                            if __name__ == "__main__":
                                pass_gen_nocapitals(max_range)
                            break
                        else:
                            print(
                                f"{Error}Option {password_opt} is not in the list.")
                    except ValueError:
                        print(f"{Error}We cannot process this with any non-integer argument. please enter a valid choice")
                    # EOFError and KeyboardInterrupt are errors that might occur when the user uses exiting shortcuts
                    except EOFError:
                        print(f"\n{Success}Exited")
                        exit()
                    except KeyboardInterrupt:
                        pass
                    # End of password menu
            except LengthError as e:  # Line 84
                print(e)
            except ValueError:
                print(f"{Error}We cannot process this with any non-integer argument. please enter a valid range")
            except EOFError:
                print(f"\n{Success}Exited")
                exit()
            except KeyboardInterrupt:
                print(f"\n{Success}Exited")
        # Will return to main menu after procedure
        elif choice_num == 2:
            with open("generatedPasswords.log", "r") as f:
                file = f.read()
                print(file)
        elif choice_num == 3:
            try:
                with open("salts.txt", "r") as f:
                    file = f.readlines()
                    salt = random.choice(file)
                if __name__ == "__main__":
                    hash_options()
                hash_type = int(input("> "))
                print(f"{menuHeading}Enter your password: ")
                user_pass = input("> ")
                if hash_type == 0:
                    print(f"{Success}Exited")
                    exit()
                if hash_type == 1:
                    type_sha = hashlib.pbkdf2_hmac("sha256", user_pass.encode(), salt.encode(), random.randint(5000, 10000))
                    final_sha = str(binascii.hexlify(type_sha))
                    print(f"{Message}Your hashed password: {Success}{(final_sha[2 :]).rstrip(final_sha[-1])}")
                elif hash_type == 2:
                    type_md5 = hashlib.pbkdf2_hmac("md5", user_pass.encode(), salt.encode(), random.randint(5000, 10000))
                    final_md5 = str(binascii.hexlify(type_md5))
                    print(f"{Message}Your hashed password: {Success}{(final_md5[2:]).rstrip(final_md5[-1])}")
                else:
                    print(f"{Error}Wait a sec.. For goodness sake dude, please choose from the list!")
            except ValueError:
                print(f"{Error}The choice list is displayed with numbers nothing else. Please choose a valid choice.")
            except EOFError:
                print(f"\n{Success}Exited")
                exit()
            except KeyboardInterrupt:
                print(f"\n{Success}Exited")
        elif choice_num == 4:
            print(f"{Success}{printable}")
        elif choice_num == 5:
            if __name__ == "__main__":
                contact_details()
        elif choice_num == 6:
            with open("README.md", "r") as f:
                print(f.read())
        else:
            print(
                f"{Error}You don't see an option {choice_num} there don't you? please select the choices that are available.")
    except ValueError:
        print(f"{Error}The choice list is displayed with numbers nothing else. Please choose depends on the choice list.")
    except EOFError:
        print(f"\n{Success}Exited")
        exit()
    except KeyboardInterrupt:
        print(f"\n{Success}Exited")
        exit()
# End of the script.
