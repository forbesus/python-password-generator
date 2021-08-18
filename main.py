#!/bin/bash

# Random password generator by Mohamed Tarek
# Program written by non-expert programmer just to try something
# All rights reserved © 2021

import logging as log
import random
from string import *
import hashlib
import binascii
import os
import colorama as cl

# Log file configuration
log.basicConfig(
    level=log.INFO,
    format="%(asctime)s -> %(message)s",
    filename="generatedPasswords.log"
)

# Colorama configuration1
cl.init(autoreset=True)
error = cl.Fore.RED
success = cl.Fore.GREEN
message = cl.Fore.LIGHTWHITE_EX
menu_heading = cl.Fore.YELLOW
choices = cl.Fore.BLUE
warn = cl.Fore.LIGHTYELLOW_EX


# Errors
class LengthError(Exception):
    pass


class EmptyCrap(Exception):
    pass


def exiting_app():
    # Holds the screen in case program ran as exe or other
    import time
    print(f"\n{success}Exiting...")
    time.sleep(1)
    exit()


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
        if __name__ == "__main__":
            exiting_app()
    else:
        for i in range(max_range_all):
            password += random.choice(chars)
        print(f"{message}Generated password: {success}{password}")
        log.info(f"Password: {password}\n")


def pass_gen_nocapitals(max_range_nocapitals):
    temp = ascii_lowercase + digits + punctuation  # Imported from string.
    chars = list(temp)
    chars.pop(59)
    password = ""
    max_range_nocapitals = int(max_range_nocapitals)
    if max_range_nocapitals == 0:
        if __name__ == "__main__":
            exiting_app()
        exit()
    else:
        for i in range(max_range_nocapitals):
            password += random.choice(chars)
        print(f"{message}Generated password: {success}{password}")
        log.info(f"Password: {password}\n")


def pass_gen_nosymbols(max_range_nosymbols):
    chars = list(printable)
    chars.pop(85)
    for s in range(37):
        chars.pop()
    password = ""
    max_range_nosymbols = int(max_range_nosymbols)
    if max_range_nosymbols == 0:
        if __name__ == "__main__":
            exiting_app()
    else:
        for i in range(max_range_nosymbols):
            password += random.choice(chars)
        print(f"{message}Generated password: {success}{password}")
        log.info(f"Password: {password}\n")


def int_length_checker(int_length):
    if int(int_length) < 9 or int(int_length) > 42:  # Editable
        raise LengthError(f"{error}Please enter a range between 9 and 42. Mostly passwords below or above that range are not usable.")


def file_checker(filename):
    if os.stat(filename).st_size == 0:
        raise EmptyCrap


def app_starter():
    print(f"""{message}
Random password generator by Mohamed Tarek.
All rights reserved © 2021
Enter 0 to exit the program.
""")


def main_menu():
    print(f"""{menu_heading}
Please select any of the below choices:
{choices}
1. Generate a random password
2. View all the generated passwords
3. Hash a password
4. View all the ASCII characters
5. Contact developer
6. Help
""")


def pass_options():
    print(f"""{menu_heading}
Select one of the below options:
{choices}
1. Include everything (Recommended)
2. Don't include symbols
3. Don't include Uppercase letters
""")


def hash_options():
    print(f"""{menu_heading}
Please choose one of the below hashing type:
{choices}
1. SHA256 (Recommended)
2. MD5
""")


# Extras & Details
def hash_details(salt_used, iteration_num):
    print(f"""{message}
Details {"-" * 100}
{message}-> Salt used: {success}{salt_used}
{message}-> Number of iterations: {success}{iteration_num}
""")


def contact_details():
    print(f"""{success}
Contact details ----------------------------------------------------------------
-> Email: mohdtarekelsayed2003@gmail.com
socials ------------------------------------------------------------------------
-> Instagram: _7amoodtarek
-> Discord: Shikabala#6224
""")


# Starting of program
if __name__ == "__main__":
    app_starter()
while True:  # Infinite loop - program won't stop unless an argument of 0
    try:
        if __name__ == "__main__":
            main_menu()
        choice_num = int(input("> "))
        if choice_num == 0:
            if __name__ == "__main__":
                exiting_app()
        if choice_num == 1:
            try:
                print(f"{menu_heading}Enter a range: ")
                max_range = int(input("> "))
                if max_range == 0:
                    if __name__ == "__main__":
                        exiting_app()
                if __name__ == "__main__":
                    int_length_checker(max_range)
                while True:
                    try:
                        if __name__ == "__main__":
                            pass_options()
                        password_opt = int(input("> "))
                        if password_opt == 0:
                            if __name__ == "__main__":
                                exiting_app()
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
                            print(f"{error}Option {password_opt} is not in the list.")
                    except ValueError:
                        print(
                            f"{error}We cannot process this with any non-integer argument. please enter a valid choice")
                    # EOFError and KeyboardInterrupt are errors that might occur when the user uses exiting shortcuts
                    except EOFError:
                        if __name__ == "__main__":
                            exiting_app()
                    except KeyboardInterrupt:
                        pass
                    # End of password menu
            except LengthError as e:  # Line 35
                print(e)
            except ValueError:
                print(f"{error}We cannot process this with any non-integer argument. please enter a valid range")
            except EOFError:
                if __name__ == "__main__":
                    exiting_app()
                exit()
            except KeyboardInterrupt:
                pass
        # Will return to main menu after procedure
        elif choice_num == 2:
            with open("generatedPasswords.log", "r") as f:
                if os.stat("generatedPasswords.log").st_size == 0:
                    print(f"{error}You haven't generated any password yet!")
                else:
                    print(f.read())
        elif choice_num == 3:
            try:
                with open("salts.txt", "r") as f:
                    file = f.readlines()
                    if os.stat("salts.txt").st_size == 0:
                        print(f"{warn}Warning: salts.txt is empty. Your password can still be hashed but it's always a good idea to add salt to it")
                    else:
                        salt = random.choice(file)
                if __name__ == "__main__":
                    hash_options()
                hash_type = int(input("> "))
                print(f"{menu_heading}Enter your password: ")
                user_pass = input("> ")
                iterations = random.randint(5000, 10000)
                if hash_type == 0:
                    if __name__ == "__main__":
                        exiting_app()
                if hash_type == 1:
                    try:
                        file_checker("salts.txt")
                        type_sha = hashlib.pbkdf2_hmac("sha256", user_pass.encode("utf-8"), salt.encode("utf-8"), iterations)
                        final_sha = str(binascii.hexlify(type_sha))
                        print(f"{message}Your hashed password: {success}{(final_sha[2 :]).rstrip(final_sha[-1])}")
                        if __name__ == "__main__":
                            hash_details(salt_used=salt, iteration_num=iterations)
                    except EmptyCrap:  # See line 37 & line
                        type_sha = hashlib.sha256(user_pass.encode("utf-8"))
                        print(f"{message}Your hashed password: {type_sha.hexdigest()}")
                        print(f"{warn}Warning: This is the original hash of your password and can be decrypted easily without a salt")
                elif hash_type == 2:
                    try:
                        file_checker("salts.txt")
                        type_md5 = hashlib.pbkdf2_hmac("md5", user_pass.encode("utf-8"), salt.encode("utf-8"), iterations)
                        final_md5 = str(binascii.hexlify(type_md5))
                        print(f"{message}Your hashed password: {success}{(final_md5[2 :]).rstrip(final_md5[-1])}")
                        if __name__ == "__main__":
                            hash_details(salt_used=salt, iteration_num=iterations)
                    except EmptyCrap:
                        type_md5 = hashlib.md5(user_pass.encode("utf-8"))
                        print(f"{message}Your hashed password: {type_md5.hexdigest()}")
                        print(f"{warn}Warning: This is the original hash of your password and can be decrypted easily without a salt")
                else:
                    print(f"{error}Wait a sec.. For goodness sake dude, please choose from the list!")
            except FileNotFoundError:
                print(f"{error}Oops! It looks like salts.txt is deleted or either you didn't install it properly lol. Please reinstall this repository and try again")
            except ValueError:
                print(f"{error}The choice list is displayed with numbers nothing else. Please choose a valid choice.")
            except EOFError:
                if __name__ == "__main__":
                    exiting_app()
            except KeyboardInterrupt:
                pass
        elif choice_num == 4:
            print(f"{success}{printable}")
        elif choice_num == 5:
            if __name__ == "__main__":
                contact_details()
        elif choice_num == 6:
            with open("README.md", "r") as f:
                print(f.read())
        else:
            print(
                f"{error}You don't see an option {choice_num} there don't you? please select the choices that are available.")
    except ValueError:
        print(
            f"{error}The choice list is displayed with numbers nothing else. Please choose depends on the choice list.")
    except EOFError:
        if __name__ == "__main__":
            exiting_app()
    except KeyboardInterrupt:
        if __name__ == "__main__":
            exiting_app()
# End of the script.
