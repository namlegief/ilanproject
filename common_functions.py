#!/usr/bin/env python


import user_function
import group_functions


with open("texts/main_menu.txt", "r") as f:
    main_menu = f.read()
    f.close()

with open("texts/users_data_menu.txt", "r") as f:
    users_data_menu = f.read()
    f.close()

with open("texts/user_creation_methods.txt", "r") as f:
    user_creation_methods = f.read()
    f.close()


def display_menu(menu_type):
    if menu_type == "main_menu":
        print main_menu
    elif menu_type == "users_data_menu":
        print users_data_menu
    elif menu_type == "user_creation_methods":
        print user_creation_methods


def validate_choice(user_choice, input_type):
    return True


def get_user_choice(prompt_string, input_type="int"):
    user_choice = raw_input(prompt_string)
    # print user_choice
    if validate_choice(user_choice, input_type):
        return user_choice
    else:
        print ("Validation failed. Try again.")
        get_user_choice(prompt_string, input_type)


def get_user_input(prompt_string, input_type="str"):
    data = raw_input(prompt_string)
    return data



