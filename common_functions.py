#!/usr/bin/env python


import user_functions
import group_functions


def display_menu(menu_type):
    with open("texts/%s.txt" % menu_type, "r") as f:
        menu_content = f.read()
        f.close()
    print menu_content


def validate_choice(user_choice, input_type):
    return True


def get_user_input(prompt_string, var_type):
    user_choice = raw_input(prompt_string)
    if validate_choice(user_choice, var_type):
        return user_choice
    else:
        print ("Validation failed. Try again.")
        get_user_input(prompt_string, var_type)